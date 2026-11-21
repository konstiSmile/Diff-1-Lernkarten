# Psycho 2 · Diagnostik Teil 3 (v40): Gruppe, Hub, echtes MC mit allen Fragen, Lesemodus, Karten, Tabellen-Karten, Suche, Überlauf
from playwright.sync_api import sync_playwright
errs = []; B = 'http://localhost:8765/index.html'
INIT = "if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,testN:0}}));"
def ok(c, m):
    print(('OK  ' if c else 'FEHLER ') + m)
    if not c: errs.append(m)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block')
    ctx.add_init_script(INIT)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    ovf = lambda t: ok(pg.evaluate("document.documentElement.scrollWidth") <= 390, 'kein Überlauf ' + t)
    pg.goto(B + '#/f/psy/u/diag'); pg.wait_for_selector('.tile')
    tiles = pg.locator('.tile').all_inner_texts()
    ok(len(tiles) == 3 and 'Teil 3' in tiles[2], 'Teil 3 als drittes Kapitel in Diagnostik')
    ok(not any('Voraussichtlich' in t for t in tiles), 'kein Vermerk in Diagnostik')
    pg.screenshot(path='/tmp/d3_liste.png', full_page=True)
    k = 'd3'
    ch = pg.evaluate("(function(){var s=CONTENT.subjects.filter(function(x){return x.id==='psy'})[0];return s.chapters.filter(function(c){return c.id==='d3'})[0]})()")
    mcs = [i for i in ch['items'] if i['type'] == 'mc']
    ok(len(ch['cards']) == 26 and len(ch['items']) == 70, f"26 Karten, 70 Fragen ({len(ch['cards'])}/{len(ch['items'])})")
    ok(all(len(i['options']) == 4 for i in mcs), 'alle MC mit 4 Optionen')
    ok(any(isinstance(i['correct'], list) for i in mcs), 'MC mit mehreren richtigen')
    pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/d3'); pg.wait_for_selector('.mode'); ovf('Hub')
    ok('1 bis 4 richtig' in pg.inner_text('.modes'), 'Hub-Text echtes MC')
    pg.screenshot(path='/tmp/d3_hub.png')
    pg.click('.mode >> nth=1'); n = 0
    for _ in range(len(mcs)):
        pg.wait_for_selector('.mopt'); ovf(f'MC #{n}') if n % 5 == 0 else None
        pg.click('.mopt >> nth=0'); pg.click('#mcheck'); pg.wait_for_selector('.mlab'); n += 1
        nx = pg.locator('#next')
        if nx.count() == 0: break
        nx.click()
    ok(n == len(mcs), f'alle {len(mcs)} MC-Fragen durchlaufen ({n})')
    pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/d3'); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext')
    for i in range(len(ch['items']) + 2):
        ovf('Lesen') if i % 15 == 0 else None
        nx = pg.locator('#rNext')
        if nx.count() == 0 or nx.is_disabled(): break
        nx.click()
    ovf('Lesen Ende')
    pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/d3?mode=cards'); pg.wait_for_selector('#card')
    ok('26' in pg.inner_text('.status'), '26 Karten in der Kartenansicht')
    for key in ('iq-gruppen', 'vierfelder', 'streudiagramm', 'koerperfett', 'wisc', 'skalen', 'normalverteilung', 'entsprechung'):
        cid = 'psy-diag-d3-' + key
        pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + f'#/f/psy/d3?c={cid}'); pg.wait_for_selector('#card')
        pg.click('#card'); pg.wait_for_timeout(250); ovf('Karte ' + key)
        if key in ('koerperfett', 'entsprechung'): pg.screenshot(path=f'/tmp/d3_{key}.png')
    pg.goto(B + '#/suche?q=Spezifität'); pg.wait_for_selector('.hit')
    ok(any('Teil 3' in h for h in pg.locator('.hit').all_inner_texts()), 'Suche findet Teil 3')
    b.close()
print('errs', errs)
