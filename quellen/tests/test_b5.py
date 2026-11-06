import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('dialog',lambda d:d.accept('Neu Name'))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    pg.goto('http://localhost:8765/index.html#/neu'); pg.wait_for_selector('#fname'); ovf('neu')
    pg.fill('#fname','Analysis Formeln'); pg.click('#fadd'); pg.wait_for_selector('#qIn'); print(pg.url)
    pg.click('#qIn'); pg.keyboard.type('Grenzwert von ')
    pg.click('[data-cat=hb]'); pg.wait_for_selector('.symtile')
    print('Frage nach Wechsel:', pg.input_value('#qIn'))
    pg.click('.symtile >> nth=2'); pg.keyboard.type('1'); print('nach Bruch:', pg.input_value('#qIn'))
    pg.click('#aIn'); pg.fill('#aIn','$\\lim_{n \\to \\infty} \\frac{1}{n} = 0$ und \\alpha_{n}^{2}')
    pg.fill('#aIn','Es gilt $\\lim_{n \\to \\infty} \\frac{1}{n} = 0$ und $x_{n}^{2}$ mit $\\sqrt{x}$')
    pg.click('[data-cat=gr]'); pg.click('#aIn'); pg.click('.symtile >> nth=0'); print('A:', pg.input_value('#aIn')[-12:])
    print('Vorschau math:', pg.locator('#pvA math').count(), pg.locator('#pvA mfrac').count(), pg.locator('#pvQ mfrac').count()); ovf('editor'); pg.screenshot(path='/tmp/b5_ed.png')
    pg.click('#esave'); pg.wait_for_selector('.ownrow'); print('Karten', pg.locator('.ownrow').count())
    pg.click('#imp'); pg.fill('#impTx','Was ist 2+2 ; 4\nHauptstadt von Frankreich ; Paris\nkaputt ohne trenner'); print(pg.inner_text('#impInfo')); pg.click('#impGo'); print('Karten', pg.locator('.ownrow').count())
    pg.click('#learn'); pg.wait_for_selector('#card'); print(pg.inner_text('h1'),'|',pg.inner_text('#seg').replace('\n',' ')); pg.click('#card'); pg.click('#bKnown'); ovf('learn'); pg.screenshot(path='/tmp/b5_learn.png')
    db=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('log',db['log'][-1][1], list(db['progress'].keys())[-1][:3], len(db['custom']['folders'][0]['cards']))
    pg.goto('http://localhost:8765/index.html#/verlauf'); pg.wait_for_selector('.legend'); print('legend', pg.inner_text('.legend').replace('\n',' '))
    pg.goto('http://localhost:8765/index.html#/neu'); pg.wait_for_selector('.tile'); print('Kachel', pg.inner_text('.tile').replace('\n',' | ')); ovf('neu2'); pg.screenshot(path='/tmp/b5_neu.png')
    pg.click('.tile'); pg.click('[data-edit] >> nth=0'); print('edit q:', pg.input_value('#qIn')[:20]); pg.click('#ecancel')
    pg.click('#fdel'); pg.click('#fdel'); pg.wait_for_selector('#fname'); print('gelöscht', pg.locator('.tile').count())
    b.close()
print('errs',errs)
