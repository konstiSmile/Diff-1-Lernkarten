# Begriffe v61: Füllwörter, nur aktuelles Fach, Wortgrenzen, Ersatz aus Tests
import json
from playwright.sync_api import sync_playwright
errs = []; B = 'http://localhost:8765/index.html'
T = {'quer:niveaumenge': {'t': 'Niveaumenge', 's': 'quer', 'q': 'q-tf-07', 'src': '', 'm': 0, 'ts': 3},
     'quer:leer': {'t': 'leer', 's': 'quer', 'q': 'q-tf-07', 'src': '', 'm': 0, 'ts': 2},
     'quer:hessematrix': {'t': 'Hessematrix', 's': 'quer', 'q': 'q-tf-07', 'src': '', 'm': 0, 'ts': 1}}
INIT = "if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,obDone:1},terms:%s}));" % json.dumps(T)
STOP = ['zum', 'ist', 'der', 'die', 'das', 'von', 'und', 'eine', 'ein', 'den', 'mit', 'für', 'nicht', 'wird', 'im', 'in']
def ok(c, m):
    print(('OK  ' if c else 'FEHLER ') + m)
    if not c: errs.append(m)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block'); ctx.add_init_script(INIT)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    def sheet():
        pg.wait_for_selector('#kwAdd'); pg.wait_for_timeout(150)
        return pg.evaluate("document.querySelector('#kwAdd').closest('[class*=tile], [class*=sheet], [role=dialog]') ? document.querySelector('#kwAdd').closest('[class*=tile], [class*=sheet], [role=dialog]').innerText : document.body.innerText")
    def close(): pg.locator('.pvok').first.click(); pg.wait_for_timeout(200)
    # Liste „Meine Begriffe“ in Querschnitt
    pg.goto(B + '#/begriffe'); pg.wait_for_selector('.kwopen')
    names = pg.evaluate("[...document.querySelectorAll('.kwopen')].map(b=>b.closest('li,div,a').innerText)")
    def openTerm(t):
        i = [n for n, x in enumerate(names) if t in x][0]; pg.locator('.kwopen').nth(i).click(); return sheet()
    t = openTerm('Niveaumenge'); pg.screenshot(path='/tmp/kw_niveau.png')
    ok('psycho' not in t.lower() and 'diff 1' not in t.lower(), 'Niveaumenge: nichts aus anderen Fächern')
    ok('aus den tests' in t.lower() and 'def. 10.1' in t.lower(), 'Niveaumenge: Ersatz aus Kap. 10 (Def. 10.1)')
    close(); t = openTerm('leer'); pg.screenshot(path='/tmp/kw_leer.png')
    ok('psycho' not in t.lower() and 'diff 1' not in t.lower(), 'leer: nichts aus anderen Fächern')
    close(); t = openTerm('Hessematrix')
    ok('querschnitt' in t.lower() and 'psycho' not in t.lower(), 'Hessematrix: Querschnitt')
    close()
    # Live im Test: Füllwort ohne Erklärungsknopf, Fachwort nur aus dem Fach
    for sid, ch in [('quer', 'k10'), ('quer', 'k11'), ('psy', 'd4'), ('diff1', 'k1')]:
        pg.goto(B + '#/'); pg.wait_for_timeout(150); pg.goto(B + '#/f/%s/%s' % (sid, ch)); pg.wait_for_selector('.mode')
        pg.locator('.mode').nth(1).click(); pg.wait_for_selector('.kwbtn'); pg.click('.kwbtn'); pg.wait_for_selector('.kw')
        ws = pg.evaluate("[...document.querySelectorAll('.card .kw')].map(x=>x.textContent)")
        sw = [w for w in ws if w.lower() in STOP]
        if sw:
            pg.locator('.card .kw').nth(ws.index(sw[0])).click(); pg.wait_for_timeout(80)
            ok(pg.locator('#kwExpl').count() == 0 and 'Allgemeines Wort' in pg.inner_text('.kwbar'), f'{sid}/{ch} „{sw[0]}“: kein Erklärungsknopf')
            pg.locator('.card .kw').nth(ws.index(sw[0])).click(); pg.wait_for_timeout(80)
        lw = [w for w in ws if len(w) >= 8]
        if lw:
            pg.locator('.card .kw').nth(ws.index(lw[0])).click(); pg.wait_for_timeout(80); pg.click('#kwExpl'); t = sheet()
            other = {'quer': ['Psycho', 'Diff 1'], 'psy': ['Querschnitt', 'Diff 1'], 'diff1': ['Psycho', 'Querschnitt']}[sid]
            ok(not any(o.lower() + ' ·' in t.lower() for o in other), f'{sid}/{ch} „{lw[0]}“: nur eigenes Fach')
            pg.screenshot(path='/tmp/kw_%s_%s.png' % (sid, ch)); close()
    b.close()
print('FEHLER:' if errs else 'ALLES OK', errs)
