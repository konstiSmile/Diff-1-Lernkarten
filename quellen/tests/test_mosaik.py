# Mosaik je Kapitel und Abzeichen (v37)
# Aufruf: python3 test_mosaik.py [URL] [Screenshot]
import sys
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
SHOT = sys.argv[2] if len(sys.argv) > 2 else None
# pp-mc-01 an 3 Tagen 4 Punkte → gemeistert (Krone); pp-tf-01 richtig, dann falsch → Ø 50 %
SEED = """
(function(){if(sessionStorage.seeded)return;sessionStorage.seeded=1;
var D=function(k){var d=new Date();d.setHours(12,0,0,0);d.setDate(d.getDate()-k);return d.getTime();};
var log=[[D(5),'psy','pp-mc-01',1,4],[D(4),'psy','pp-mc-01',1,4],[D(3),'psy','pp-tf-01',1],[D(2),'psy','pp-tf-01',0],[D(1),'psy','pp-mc-01',1,4]];
localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1},log:log}));})();
"""

def ok(cond, msg):
    print(('OK   ' if cond else 'FAIL ') + msg)
    if not cond: ok.fail = True
ok.fail = False

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    for theme in ['dark', 'light']:
        ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block', color_scheme=theme)
        ctx.add_init_script(SEED)
        pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        def go(h):
            pg.goto(URL + '#/leer'); pg.wait_for_timeout(100); pg.goto(URL + h); pg.wait_for_timeout(250)
        if theme == 'light':
            pg.goto(URL); pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.theme='light';localStorage.setItem('lernkiste-v1',JSON.stringify(d))"); pg.reload()
        go('#/')
        if theme == 'dark': ok('Abzeichen' in (pg.inner_text('.toast') if pg.locator('.toast').count() else ''), theme + ': Toast für neue Abzeichen')
        go('#/f/psy/k1'); pg.wait_for_selector('.mgrid')
        n = pg.evaluate("window.CONTENT.subjects.filter(s=>s.id==='psy')[0].chapters.filter(c=>c.id==='k1')[0].items.length")
        ok(pg.locator('.mt').count() == n, theme + ': eine Kachel pro Frage (%d)' % n)
        ok(pg.locator('.mt .crown').count() == 1 and pg.locator('.mt.h2').count() == 1 and pg.locator('.mt.hn').count() == n - 2, theme + ': Krone, Ø-Farbe, Rest grau')
        ok('2 / %d geübt · 1 gemeistert' % n in pg.inner_text('.mhead'), theme + ': Kopfzeile ' + pg.inner_text('.mhead span'))
        ok(pg.evaluate('document.documentElement.scrollWidth') <= 390, theme + ': kein Überlauf')
        pg.click('.mt:has(.crown)')
        info = pg.inner_text('#minfo')
        ok('3× beantwortet' in info and 'zuletzt 4/4' in info and 'gemeistert' in info, theme + ': Infozeile ' + info.replace('\n', ' | '))
        if SHOT and theme == 'dark': pg.locator('.mosaic').screenshot(path=SHOT)
        if SHOT and theme == 'light': pg.locator('.mosaic').screenshot(path=SHOT.replace('.png', '_hell.png'))
        pg.click('#mGo'); pg.wait_for_selector('.mopt')
        mt = ' | '.join(pg.locator('.meta').all_inner_texts())
        ok('EINZELFRAGE · 1 / 1' in mt.upper(), theme + ': Einzelfrage üben (' + mt.replace('\n', ' ') + ')')
        go('#/verlauf'); pg.wait_for_selector('.badges')
        ok(pg.locator('.bdg').count() == 10 and pg.locator('.bdg.got').count() >= 1, theme + ': Abzeichen im Verlauf (%d erreicht)' % pg.locator('.bdg.got').count())
        got = pg.locator('.bdg.got').all_inner_texts()
        ok(any('Erste Antwort' in g for g in got) and not any('Alle Fächer' in g for g in got), theme + ': richtige Abzeichen')
        ok(pg.evaluate('document.documentElement.scrollWidth') <= 390, theme + ': Verlauf ohne Überlauf')
        # Abschalten
        go('#/einstellungen')
        if not pg.locator('.group.open .ghead:has-text("Motivation")').count(): pg.click('.ghead:has-text("Motivation")')
        pg.click('.seg[data-k=mMosaic] button[data-v="0"]'); pg.click('.seg[data-k=mBadges] button[data-v="0"]')
        go('#/f/psy/k1'); ok(pg.locator('.mosaic').count() == 0, theme + ': Mosaik abschaltbar')
        go('#/verlauf'); ok(pg.locator('.badges').count() == 0, theme + ': Abzeichen abschaltbar')
        # Gemischt und Heute fällig ohne Mosaik
        pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.mMosaic=1;localStorage.setItem('lernkiste-v1',JSON.stringify(d))"); pg.reload()
        go('#/mix/tests'); pg.wait_for_selector('.mode'); ok(pg.locator('.mosaic').count() == 0, theme + ': kein Mosaik in Gemischt')
        # Backup-Zusammenführen: Abzeichen bleiben erhalten
        bd = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).badges")
        ok(isinstance(bd, dict) and 'first' in bd, theme + ': Abzeichen gespeichert')
        ok(not errs, theme + ': keine JS-Fehler ' + str(errs))
        ctx.close()
    b.close()
print('FERTIG', 'mit Fehlern' if ok.fail else 'alles ok')
sys.exit(1 if ok.fail else 0)
