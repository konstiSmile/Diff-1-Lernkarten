# Psycho 2 · Persönlichkeit Kap. 5a/5b (v39), Vermerk „Voraussichtlich nicht klausurrelevant“: Hub, echtes MC mit allen Fragen, Lesemodus, Karten, Suche, Überlauf
from playwright.sync_api import sync_playwright
import json
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
    pg.goto(B + '#/f/psy/u/pers'); pg.wait_for_selector('.tile')
    tiles = pg.locator('.tile').all_inner_texts()
    ok(any('5a' in t for t in tiles) and any('5b' in t for t in tiles), 'Kapitel 5a und 5b in der Gruppe')
    ok(sum('Voraussichtlich nicht klausurrelevant' in t for t in tiles) == 2, 'Vermerk auf genau zwei Kacheln')
    pg.screenshot(path='/tmp/p5_liste.png', full_page=True)
    for k in ('k5a', 'k5b'):
        ch = pg.evaluate("(function(){var s=CONTENT.subjects.filter(function(x){return x.id==='psy'})[0];return s.chapters.filter(function(c){return c.id==='%s'})[0]})()" % k)
        mcs = [i for i in ch['items'] if i['type'] == 'mc']
        ok(all(len(i['options']) == 4 for i in mcs), k + ': alle MC mit 4 Optionen')
        ok(any(isinstance(i['correct'], list) for i in mcs), k + ': MC mit mehreren richtigen')
        pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/' + k); pg.wait_for_selector('.mode'); ovf('Hub ' + k)
        ok('1 bis 4 richtig' in pg.inner_text('.modes'), k + ': Hub-Text echtes MC')
        ok('Voraussichtlich nicht klausurrelevant' in pg.inner_text('#view'), k + ': Vermerk im Hub')
        if k == 'k5a': pg.screenshot(path='/tmp/p5_hub.png')
        # alle MC-Fragen durchgehen: je ein Kreuz, prüfen, weiter
        pg.click('.mode >> nth=1'); n = 0
        for _ in range(len(mcs)):
            pg.wait_for_selector('.mopt'); ovf(f'MC {k} #{n}')
            ok(pg.locator('.mopt').count() == 4, f'{k} MC #{n}: 4 Kästchen') if n < 2 else None
            pg.click('.mopt >> nth=0'); pg.click('#mcheck'); pg.wait_for_selector('.mlab'); n += 1
            pass
            nx = pg.locator('#next')
            if nx.count() == 0: break
            nx.click()
        ok(n == len(mcs), f'{k}: alle {len(mcs)} MC-Fragen durchlaufen ({n})')
        pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/' + k); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext')
        for _ in range(len(ch['items']) + 2):
            ovf('Lesen ' + k) if _ % 15 == 0 else None
            nx = pg.locator('#rNext')
            if nx.count() == 0 or nx.is_disabled(): break
            nx.click()
        ovf('Lesen Ende ' + k)
        pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + '#/f/psy/' + k + '?mode=cards'); pg.wait_for_selector('#card')
        ok(str(len(ch['cards'])) in pg.inner_text('.status'), f'{k}: {len(ch["cards"])} Karten')
        ok('Voraussichtlich nicht klausurrelevant' in pg.inner_text('#view'), k + ': Vermerk bei Karten')
    # breite Karten (Tabellen) auf Überlauf prüfen
    for cid in ('psy-pers-k5a-iq-matrix', 'psy-pers-k5a-meeus', 'psy-pers-k5a-korrelationen', 'psy-pers-k5a-umwelten', 'psy-pers-k5a-kovarianz', 'psy-pers-k5a-lebensereignisse', 'psy-pers-k5a-methoden', 'psy-pers-k5b-verbal', 'psy-pers-k5b-positionen', 'psy-pers-k5b-mayr-erfolg', 'psy-pers-k5b-lpa', 'psy-pers-k5b-karikaturen'):
        k = cid.split('-')[2]
        pg.goto(B + '#/'); pg.wait_for_timeout(100); pg.goto(B + f'#/f/psy/{k}?c={cid}'); pg.wait_for_selector('#card')
        pg.click('#card'); pg.wait_for_timeout(250); ovf('Karte ' + cid)
        if cid.endswith('korrelationen'): pg.screenshot(path='/tmp/p5_card.png')
    pg.goto(B + '#/suche?q=Kovarianz'); pg.wait_for_selector('.hit')
    ok(any('Teil 5' in h for h in pg.locator('.hit').all_inner_texts()), 'Suche findet Teil 5')
    pg.goto(B + '#/f/psy/u/pers'); pg.wait_for_selector('.tile')
    ok(not any('Voraussichtlich' in t for t in pg.locator('.tile').all_inner_texts()[:6]), 'Kap. 1–4b ohne Vermerk')
    b.close()
print('errs', errs)
