import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    pg.goto('http://localhost:8765/index.html'); pg.wait_for_selector('.tile')
    print('mixtile',pg.locator('.mixtile').count()); ovf('home'); pg.screenshot(path='/tmp/b4_home.png')
    pg.click('.mixtile'); pg.wait_for_selector('.mixrow'); print('rows',pg.locator('.mixrow').count(), pg.inner_text('.row').replace('\n',' ')); ovf('hub'); pg.screenshot(path='/tmp/b4_hub.png')
    # Karten
    pg.click('#mxC'); pg.wait_for_selector('#card'); print(pg.inner_text('h1'), '|', pg.inner_text('.nav a'))
    pg.click('#card'); pg.click('#bKnown'); pg.wait_for_selector('#card')
    db=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('log',db['log'][-1][1:3])
    pg.click('.nav a'); pg.wait_for_selector('.mixrow')
    # Tests
    pg.click('#mxT'); pg.wait_for_selector('.mode'); print(pg.inner_text('h1'),'|',pg.inner_text('.mode >> nth=0').replace('\n',' '))
    pg.click('.mode >> nth=1'); pg.wait_for_selector('.card'); pg.locator('.opt').first.click(); pg.click('#next')
    db=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('log2',db['log'][-1][1:3]); ovf('test')
    pg.click('#quit'); pg.click('.nav a'); pg.wait_for_selector('.mixrow')
    # Fach abwählen
    pg.uncheck('.mixrow input >> nth=1'); print('nach Abwahl', pg.inner_text('.row').replace('\n',' '), pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).settings.mixSubs"))
    pg.click('[data-mm=rand]'); print('mode', pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).settings.mixMode"))
    # Fach verstecken -> Kachel weg
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.hidden=['quer'];localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.goto('http://localhost:8765/index.html#/'); pg.reload(); pg.wait_for_selector('.tile'); print('mixtile bei 1 sichtbarem Fach',pg.locator('.mixtile').count())
    b.close()
print('errs',errs)
