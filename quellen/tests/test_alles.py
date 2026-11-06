import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width':390,'height':780}, service_workers='block')
    ctx.add_init_script("if(!localStorage.getItem('seeded')){localStorage.setItem('seeded','1');localStorage.setItem('dif1-k1-status',JSON.stringify({0:'known',3:'again',5:'known'}));localStorage.setItem('quer-k10',JSON.stringify({best:{mc:80},wrong:['q-mc-01'],n:5,min:30,exn:8}));}")
    pg = ctx.new_page()
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
    def ovf(tag):
        w = pg.evaluate("document.documentElement.scrollWidth")
        if w>390: errs.append(f'OVERFLOW {tag} {w}')
    pg.goto('http://localhost:8765/index.html'); pg.wait_for_selector('.tile')
    db = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))")
    print('migrated progress', db['progress'], db['tests'], db['settings'])
    print('tiles', pg.locator('.tile').count(), pg.inner_text('.tile >> nth=0')[:80].replace('\n',' | '))
    ovf('home'); pg.screenshot(path='/tmp/s_home.png')
    # Fach & Karten
    pg.click('.tile >> nth=0'); pg.wait_for_selector('.tile'); ovf('fach'); pg.click('.tile >> nth=0'); pg.wait_for_selector('#card')
    print('deck', pg.inner_text('.status').replace('\n',' '))
    pg.click('#card'); pg.click('#bKnown'); pg.wait_for_selector('#card'); ovf('card'); pg.screenshot(path='/tmp/s_card.png')
    db = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('log', len(db['log']), db['log'][-1])
    pg.click('#seg button[data-f=all]'); print(pg.inner_text('.status').replace('\n',' '))
    # Suche
    pg.click('.tab[data-t=suche]'); pg.fill('#q','schrankenlemma'); pg.wait_for_selector('.hit'); print('hits', pg.locator('.hit').count()); ovf('search'); pg.screenshot(path='/tmp/s_search.png')
    pg.click('.hit >> nth=0'); pg.wait_for_selector('#card'); print('deeplink', pg.url, pg.locator('mark.hl').count(), 'marks', pg.locator('#card.back').count())
    pg.goto('http://localhost:8765/index.html#/suche?q=niveaumenge'); pg.wait_for_selector('.hit'); pg.click('.hit >> nth=0'); pg.wait_for_selector('.card'); print('quer single', pg.inner_text('.meta')[:60].replace('\n',' '), pg.locator('mark.hl').count()); ovf('single')
    # Tests
    pg.goto('http://localhost:8765/index.html#/f/quer/k10'); pg.wait_for_selector('.mode'); print('best chips', pg.inner_text('.mode >> nth=0').replace('\n',' '), '| chip on:', pg.inner_text('.chip.on')); ovf('hub'); pg.screenshot(path='/tmp/s_hub.png')
    for m in range(3):
        pg.click(f'.mode >> nth={m}')
        for i in range(5):
            pg.wait_for_selector('.card')
            if pg.locator('input.gap').count():
                pg.locator('input.gap').first.fill('x'); pg.click('#check')
            else: pg.locator('.opt').first.click()
            pg.click('#next')
        pg.wait_for_selector('.score'); print('mode',m, pg.inner_text('.score .big'), 'tabbar hidden?', pg.evaluate("getComputedStyle(document.querySelector('#tabbar')).display")); ovf('result'); pg.click('#menu')
    # Exam
    pg.click('.mode >> nth=3'); pg.click('#go'); pg.wait_for_selector('.clock'); ovf('exam'); pg.screenshot(path='/tmp/s_exam.png')
    print('imm', pg.evaluate("document.body.classList.contains('immersive')"))
    pg.click('#submit'); pg.click('#submit'); pg.wait_for_selector('.score'); print('exam', pg.inner_text('.score').replace('\n',' '), pg.evaluate("document.body.classList.contains('immersive')"))
    # Verlauf, Neu, Einstellungen
    pg.click('.tab[data-t=verlauf]'); pg.wait_for_selector('.chart'); ovf('verlauf'); print(pg.inner_text('.stats').replace('\n',' ')); pg.screenshot(path='/tmp/s_verlauf.png')
    pg.click('.tab[data-t=neu]'); ovf('neu')
    pg.click('.tab[data-t=set]'); pg.wait_for_selector('.group'); ovf('set'); pg.screenshot(path='/tmp/s_set.png', full_page=True)
    pg.click('[data-k=theme] button[data-v=light]'); print('theme', pg.evaluate("document.documentElement.dataset.theme")); pg.screenshot(path='/tmp/s_light.png')
    pg.click('[data-k=font] button[data-v="1.15"]'); print('fs', pg.evaluate("document.documentElement.style.fontSize"))
    # Backup roundtrip
    txt = pg.evaluate("(function(){return JSON.stringify({app:'lernkiste',v:1,data:JSON.parse(localStorage.getItem('lernkiste-v1'))})})()")
    pg.evaluate("localStorage.removeItem('lernkiste-v1')"); pg.reload(); pg.wait_for_selector('.group')
    db = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('after wipe progress (re-migrated from old keys)', len(db['progress']), len(db['log']))
    pg.click('.tab[data-t=set]'); pg.click('#bPaste'); pg.fill('#impText', txt); pg.click('#impGo'); pg.wait_for_selector('#iMerge'); print(pg.inner_text('#impbox')[:70].replace('\n',' ')); pg.click('#iRepl'); pg.wait_for_selector('.group')
    db = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))"); print('after import', len(db['progress']), len(db['log']), db['settings']['theme'])
    pg.fill if False else None
    b.close()
print('ERRORS', errs)
