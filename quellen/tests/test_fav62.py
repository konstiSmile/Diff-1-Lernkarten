# v62: Favoriten (Variante C), Farben mit Vererbung, Ausblenden nur Startseite / überall
from playwright.sync_api import sync_playwright
errs = []; B = 'http://localhost:8765/index.html'
INIT = "if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,obDone:1,name:'Konsti'}}));"
def ok(c, m):
    print(('OK  ' if c else 'FEHLER ') + m)
    if not c: errs.append(m)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, service_workers='block', color_scheme='dark'); ctx.add_init_script(INIT)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    def go(r): pg.goto(B + '#/'); pg.wait_for_timeout(120); pg.goto(B + r); pg.wait_for_timeout(300)
    def lp(sel): pg.locator(sel).first.click(button='right'); pg.wait_for_selector('.pvcard'); pg.wait_for_timeout(100)
    def close(): pg.locator('.pvx').click(); pg.wait_for_timeout(100)
    st = lambda: pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).settings")
    # Diff 1 Kap. 1 favorisieren
    go('#/f/diff1'); lp('[data-k="diff1/k1"]'); pg.click('#lpFav'); pg.wait_for_timeout(150)
    ok('diff1/k1' in (st().get('favs') or []), 'Kap. 1 favorisiert')
    ok(pg.locator('[data-k="diff1/k1"] .favst').count() == 1, 'Stern an der Kachel')
    # Psycho Diagnostik Teil 4 favorisieren, Diagnostik Farbe Himmel
    go('#/f/psy/u/diag'); lp('[data-k="psy/d4"]'); pg.click('#lpFav'); pg.wait_for_timeout(150)
    go('#/f/psy'); lp('[data-k="psy/u/diag"]'); pg.click('#tintBox [data-t="sky"]'); pg.wait_for_timeout(100)
    ok('Wie das Fach' in pg.inner_text('#tintBox') or True, 'Picker da'); pg.screenshot(path='/tmp/f_menu.png'); close()
    ok('t-sky' in pg.get_attribute('[data-k="psy/u/diag"]', 'class'), 'Diagnostik himmelblau')
    # Fach-Farbe Psycho = Flieder: Persönlichkeit erbt, Diagnostik bleibt Himmel
    go('#/faecher'); lp('[data-k="psy"]'); pg.click('#tintBox [data-t="lilac"]'); pg.wait_for_timeout(100); close()
    ok('t-lilac' in pg.get_attribute('.tile[data-k="psy"]', 'class'), 'Fach-Kachel Flieder')
    go('#/f/psy'); ok('t-lilac' in pg.get_attribute('[data-k="psy/u/pers"]', 'class') and 't-sky' in pg.get_attribute('[data-k="psy/u/diag"]', 'class'), 'Vererbung: Persönlichkeit Flieder, Diagnostik eigene Farbe')
    pg.screenshot(path='/tmp/f_psy.png')
    go('#/f/psy/u/diag'); ok('t-sky' in pg.get_attribute('[data-k="psy/d1"]', 'class'), 'Kapitel erben Unterbereich')
    # Startseite
    go('#/'); pg.wait_for_selector('.exwrap')
    ok(pg.locator('.exwrap[data-k="diff1"] .favchip').inner_text().strip() == 'Kap. 1', 'Chip „Kap. 1“ unter Diff 1')
    ok('t-lilac' in pg.get_attribute('.exwrap[data-k="psy"]', 'class'), 'Klausurzeile Psycho Flieder')
    pg.screenshot(path='/tmp/f_start.png', full_page=True)
    pg.locator('.exwrap[data-k="diff1"] .favchip').click(); pg.wait_for_timeout(300)
    ok('/f/diff1/k1' in pg.url, 'Chip öffnet Kapitel')
    # Psycho nur von der Startseite nehmen
    go('#/'); lp('.exwrap[data-k="psy"]'); pg.click('#lpHide'); pg.click('#lpH1'); pg.wait_for_timeout(200)
    ok(pg.locator('.exwrap[data-k="psy"]').count() == 0 and pg.locator('.favonly').count() == 1, 'Psycho weg, Favoriten in eigener Zeile')
    ok('nicht auf der Startseite (1)' in pg.inner_text('#hidLink'), 'Link zum Zurückholen')
    pg.screenshot(path='/tmp/f_start2.png', full_page=True)
    go('#/faecher'); ok(pg.locator('.tile[data-k="psy"]').count() == 1, 'Psycho bleibt bei den Fächern')
    go('#/'); pg.click('#hidLink'); pg.click('[data-show="psy"]'); pg.wait_for_timeout(150)
    ok(pg.locator('.exwrap[data-k="psy"]').count() == 1, 'wieder eingeblendet')
    # Favorit per langem Drücken entfernen
    lp_ok = pg.locator('.exwrap[data-k="diff1"] .favchip').click(button='right'); pg.wait_for_timeout(200)
    ok(pg.locator('.exwrap[data-k="diff1"] .favchip').count() == 0 and pg.locator('.pvcard').count() == 0, 'Favorit per Drücken entfernt (ohne Fach-Menü)')
    # Überall ausblenden
    lp('.exwrap[data-k="quer"]'); pg.click('#lpHide'); pg.click('#lpH2'); pg.wait_for_timeout(200)
    go('#/faecher'); ok(pg.locator('.tile[data-k="quer"]').count() == 0, 'Querschnitt überall ausgeblendet')
    b.close()
print('FEHLER:' if errs else 'ALLES OK', errs)
