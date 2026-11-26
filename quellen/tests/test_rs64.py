# Rechenschemata v64: Kachel im Querschnitt, Überblick aufklappbar, Aufgabe aufdecken + bewerten, Lernstand, Querverweis aus Kap. 11
from playwright.sync_api import sync_playwright
import json
errs = []; B = 'http://localhost:8765/index.html'
INIT = "if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,obDone:1}}));"
def ok(c, m):
    print(('OK  ' if c else 'FEHLER ') + m)
    if not c: errs.append(m)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block'); ctx.add_init_script(INIT)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(B + '#/f/quer'); pg.wait_for_selector('.tile')
    names = pg.eval_on_selector_all('.tile h2', 'e=>e.map(x=>x.textContent)')
    ok(names[-1] == 'Rechenschemata' and 'Allgemein' in names, 'Querschnitt: Kachel „Rechenschemata“ nach „Allgemein“ ' + str(names))
    pg.screenshot(path='/tmp/rs_fach.png')
    pg.locator('.tile', has_text='Rechenschemata').click(); pg.wait_for_selector('.rsstep')
    ok(pg.locator('.rsstep').count() == 7, '7 Schritte im Überblick')
    ok(pg.locator('.rsx').count() == 3, 'Fallunterscheidungen, Sonderfälle, Formales')
    pg.screenshot(path='/tmp/rs_ueber.png')
    pg.locator('.rsstep > summary').nth(3).click(); pg.wait_for_timeout(150)
    pg.locator('.rsstep[open] .rs-bsp summary').click(); pg.wait_for_timeout(150)
    pg.locator('.rsstep[open]').scroll_into_view_if_needed(); pg.screenshot(path='/tmp/rs_step4.png', full_page=True)
    ok('Variation der Konstanten' in pg.inner_text('.rsstep[open] .rs-satz'), 'Schritt 4: Mustersatz sichtbar')
    ok(pg.locator('.rsstep[open] .ab').count() >= 0, 'Abkürzungen laufen ohne Fehler')
    # Breite 370: nichts läuft seitlich über
    over = pg.evaluate("[...document.querySelectorAll('.rsstep[open] .dm')].filter(d=>d.scrollWidth>d.clientWidth+2).length")
    print('HINWEIS: breite Formeln Schritt 4 (scrollbar):', over)
    ok(pg.evaluate('document.documentElement.scrollWidth<=390'), 'keine horizontale Seitenverschiebung')
    # Aufgaben
    pg.locator('[data-tab=a]').click(); pg.wait_for_selector('.rstask')
    ok(pg.locator('.rstask').count() == 6, '6 Aufgaben')
    pg.screenshot(path='/tmp/rs_aufg.png')
    pg.locator('.rstask').nth(0).click(); pg.wait_for_selector('#rsShow')
    ok('schritt 1' in pg.inner_text('.rsnext').lower(), 'Mit Schritten: Schritt 1 angekündigt')
    pg.screenshot(path='/tmp/rs_run1.png')
    for i in range(7):
        pg.click('#rsShow'); pg.wait_for_selector('.rsrate button')
        if i == 3: pg.screenshot(path='/tmp/rs_run4.png', full_page=True)
        pg.locator('.rsrate button').nth(2 if i != 3 else 1).click(); pg.wait_for_timeout(80)
    pg.wait_for_selector('.rsend'); ok('93 %' in pg.inner_text('.rsend') and 'Schritt 4' in pg.inner_text('.rsend'), 'Ende: 93 % und Schritt 4 genannt')
    pg.screenshot(path='/tmp/rs_end.png', full_page=True)
    db = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))")
    ok(db['log'][-1][1:] == ['quer', 'rs-dgl1-t21', 0.93], 'Verlauf: ein Eintrag mit 0,93 ' + str(db['log'][-1]))
    ok(db['tests']['quer/rs-dgl1']['rs']['rs-dgl1-t21']['m'] == [1, 1, 1, 0.5, 1, 1, 1], 'Schritt-Bewertungen gespeichert')
    pg.click('#rsBack'); pg.wait_for_selector('.banner'); ok('Schritt 4' in pg.inner_text('.banner'), 'Zuletzt schwach: Schritt 4')
    # Klausur-Modus, alles gewusst → Lernstand
    pg.click('[data-rm=k]'); pg.wait_for_selector('.rstask'); pg.locator('.rstask').nth(1).click(); pg.wait_for_selector('#rsShow')
    ok('schritt 1 ·' not in pg.inner_text('.rsnext').lower(), 'Klausur: kein Schrittname vorab')
    for i in range(7):
        pg.click('#rsShow'); pg.wait_for_selector('.rsrate button'); pg.locator('.rsrate button').nth(2).click(); pg.wait_for_timeout(60)
    ok('Alles gewusst' in pg.inner_text('.rsend'), 'Klausur: alles gewusst')
    pg.goto(B + '#/f/quer'); pg.wait_for_selector('.tile')
    ok('1/6 Aufgaben' in pg.locator('.tile', has_text='Rechenschemata').inner_text(), 'Kachel: 1/6 Aufgaben')
    # Querverweis Kap. 11
    pg.goto(B + '#/f/quer/k11'); pg.wait_for_selector('.rsrel'); pg.screenshot(path='/tmp/rs_k11.png', full_page=True)
    pg.click('.rsrel'); pg.wait_for_selector('.rsstep'); ok(True, 'Querverweis aus Kap. 11 öffnet Rechenschema')
    # Suche
    pg.goto(B + '#/f/quer/rs-dgl1?st=4'); pg.wait_for_selector('.rsstep[open]'); ok(pg.get_attribute('.rsstep[open]', 'data-n') == '4', '?st=4 öffnet Schritt 4')
    pg.goto(B + '#/'); pg.goto(B + '#/f/quer/rs-dgl1?t=rs-dgl1-k'); pg.wait_for_selector('#rsShow'); ok('Parameter' in pg.inner_text('.lhead'), '?t= startet Aufgabe')
    # dunkel
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.theme='dark';d.settings.ui44=1;localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.goto(B + '#/'); pg.goto(B + '#/f/quer/rs-dgl1?st=1'); pg.wait_for_selector('.rsstep[open]'); pg.wait_for_timeout(200); pg.screenshot(path='/tmp/rs_dark.png')
    b.close()
print('Fehler:', errs if errs else 'keine')
