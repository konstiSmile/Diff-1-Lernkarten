from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    pg.goto('http://localhost:8765/index.html'); pg.wait_for_selector('.tile')
    print('home tiles', [t.split('\n')[0] for t in pg.locator('.tile').all_inner_texts()], 'mix', pg.locator('.mixtile').count())
    pg.click('.tilewrap[data-sid=psy] .tile'); pg.wait_for_selector('.tile'); print('fach:', pg.inner_text('h1'), [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()]); ovf('fach'); pg.screenshot(path='/tmp/psy_fach.png')
    pg.click('.tile >> nth=0'); pg.wait_for_selector('.tile'); print('gruppe:', pg.inner_text('h1'), [t.split('\n')[0] for t in pg.locator('.tile').all_inner_texts()]); ovf('gruppe'); pg.screenshot(path='/tmp/psy_grp.png')
    pg.click('.tile >> nth=0'); pg.wait_for_selector('#card'); print('karten:', pg.inner_text('.status').replace('\n',' '), '| seg:', pg.inner_text('#seg').replace('\n',' '), '| back:', pg.inner_text('.nav a'))
    pg.click('#card'); ovf('karte'); pg.screenshot(path='/tmp/psy_card.png'); pg.click('#bKnown')
    pg.click('.nav a'); pg.wait_for_selector('.tile'); print('zurück:', pg.inner_text('h1'))
    pg.click('.tile >> nth=2'); pg.wait_for_selector('.mode'); print('tests:', pg.inner_text('h1'), pg.inner_text('.mode >> nth=0').replace('\n',' '), '|', pg.inner_text('.mode >> nth=3').replace('\n',' '))
    pg.click('.nav a'); pg.wait_for_selector('.tile')
    pg.goto('http://localhost:8765/index.html#/f/psy/u/entw'); pg.wait_for_selector('.note'); print('entw:', pg.inner_text('.note'))
    pg.goto('http://localhost:8765/index.html#/suche?q=Faktorladung'); pg.reload(); pg.wait_for_selector('.hit'); print('Suche hits', pg.locator('.hit').count()); pg.click('.hit >> nth=0'); pg.wait_for_selector('#card,.card'); print(pg.url)
    pg.goto('http://localhost:8765/index.html#/mix'); pg.reload(); pg.wait_for_selector('.mixrow'); print('mix:', pg.inner_text('.group').replace('\n',' '), '|', pg.inner_text('.row').replace('\n',' ')); ovf('mix')
    pg.goto('http://localhost:8765/index.html#/psycho2.html'); 
    b.close()
print('errs',errs)
