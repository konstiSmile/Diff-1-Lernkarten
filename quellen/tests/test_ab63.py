# Abkürzungen v63: unterstrichen, Antippen zeigt Langform oben, nicht in Formeln, MC per langem Drücken
from playwright.sync_api import sync_playwright
errs = []; B = 'http://localhost:8765/index.html'
INIT = "if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,obDone:1}}));"
def ok(c, m):
    print(('OK  ' if c else 'FEHLER ') + m)
    if not c: errs.append(m)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block', has_touch=False); ctx.add_init_script(INIT)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    # Lesemodus Querschnitt Kap. 11
    pg.goto(B + '#/f/quer/k11?read=1'); pg.wait_for_selector('.ab'); pg.wait_for_timeout(200)
    seen = set()
    for i in range(26):
        seen |= set(pg.evaluate("[...document.querySelectorAll('.ab')].map(x=>x.dataset.ab)"))
        if pg.locator('.ab[data-ab=AWP]').count(): break
        pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(120)
    ok('DGL' in seen and 'AWP' in seen, 'Lesemodus k11: DGL und AWP markiert')
    ok(pg.evaluate("!document.querySelector('math .ab, .meta .ab, a .ab')"), 'nicht in Formeln/Meta/Links')
    pg.locator('.ab[data-ab=AWP]').first.click(); pg.wait_for_selector('.abtip')
    ok(pg.inner_text('.abtip').strip() == 'AWP = Anfangswertproblem', 'Leiste zeigt „AWP = Anfangswertproblem“')
    pg.screenshot(path='/tmp/ab_read.png')
    pg.mouse.click(200, 700); pg.wait_for_timeout(100)
    ok(pg.locator('.abtip').count() == 0, 'Tipp daneben schließt Leiste')
    # Karteikarte: Antippen dreht nicht um
    pg.goto(B + '#/'); pg.goto(B + '#/f/quer/k11'); pg.wait_for_selector('.mode'); pg.locator('.mode').nth(0).click(); pg.wait_for_selector('#card')
    for i in range(30):
        if pg.locator('#card .ab').count(): break
        pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(80)
    if pg.locator('#card .ab').count():
        cls = pg.get_attribute('#card', 'class'); pg.locator('#card .ab').first.click(); pg.wait_for_timeout(150)
        ok(pg.get_attribute('#card', 'class') == cls and pg.locator('.abtip').count() == 1, 'Karteikarte: Leiste, kein Umdrehen')
    else: print('HINWEIS: keine Karte mit Abkürzung auf der Vorderseite gefunden')
    # Psycho: Mittelwert nur vor „=“, UCS, WISC (Lesemodus durchblättern)
    def scan(sid, ch, n):
        pg.goto(B + '#/'); pg.goto(B + '#/f/%s/%s?read=1' % (sid, ch)); pg.wait_for_timeout(300); ks = set(); ms = []
        for i in range(n):
            ks |= set(pg.evaluate("[...document.querySelectorAll('.ab')].map(x=>x.dataset.ab)"))
            ms += pg.evaluate("[...document.querySelectorAll('.ab[data-ab=M]')].map(x=>x.nextSibling&&x.nextSibling.nodeValue||'')")
            pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(60)
        return ks, ms
    ks, ms = scan('psy', 'd1', 43)
    ok(ms and all(x.lstrip().startswith('=') for x in ms), 'M nur vor „=“ (%d)' % len(ms))
    ok('WISC' in ks and 'IQ' in ks, 'd1: WISC, IQ markiert')
    ok(not ks & {'DGL', 'AWP'}, 'Psycho ohne Mathe-Kürzel')
    ks, ms = scan('psy', 'k3b', 35)
    ok({'UCS', 'CS', 'NS'} <= ks, 'k3b: UCS, CS, NS markiert')
    # Mathe-Kürzel nicht in Psycho und umgekehrt
    pg.goto(B + '#/f/quer/k11?read=1'); pg.wait_for_selector('.ab'); pg.wait_for_timeout(200)
    ok(pg.evaluate("[...document.querySelectorAll('.ab')].every(x=>['DGL','AWP','ZWS','o. E.'].includes(x.dataset.ab))"), 'Querschnitt nur Mathe-Kürzel')
    # Tests: MC-Knopf mit Abkürzung – Klick wählt, Rechtsklick erklärt
    found = qd = False
    for sid, ch in [('quer', 'k11'), ('psy', 'd1'), ('psy', 'd3')]:
      if found and qd: break
      pg.goto(B + '#/'); pg.goto(B + '#/f/%s/%s' % (sid, ch)); pg.wait_for_selector('.mode'); pg.locator('.mode').nth(1).click(); pg.wait_for_selector('.card')
      for i in range(70):
          pg.wait_for_timeout(120)
          if pg.locator('button.opt .ab').count():
              found = True; o = pg.locator('button.opt .ab').first
              o.click(button='right'); pg.wait_for_timeout(120)
              ok(pg.locator('.abtip').count() == 1 and pg.locator('#fb .fb').count() == 0, 'MC: Rechtsklick zeigt Langform, keine Antwort')
              pg.screenshot(path='/tmp/ab_mc.png'); pg.mouse.click(200,760); break
          if not qd and pg.locator('.qtext .ab, .stmt .ab').count():
              qd = True
              pg.locator('.qtext .ab, .stmt .ab').first.click(); pg.wait_for_timeout(100)
              ok(pg.locator('.abtip').count() == 1 and pg.locator('#fb .fb').count() == 0, 'Frage: Antippen zeigt Langform, keine Antwort')
              pg.screenshot(path='/tmp/ab_q.png')
          sk = pg.locator('text=Überspringen')
          if not sk.count(): break
          sk.first.click()
    if not qd: print('HINWEIS: keine Frage mit Abkürzung gefunden')
    if not found: print('HINWEIS: keine MC-Option mit Abkürzung gefunden')
    # Begriffe-Modus übernimmt das Antippen
    b.close()
print('\nFEHLER:', errs if errs else 'keine')
