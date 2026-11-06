from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width':390,'height':780}, service_workers='block'); pg = ctx.new_page(); errs=[]
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://localhost:8768/index.html#/suche'); pg.wait_for_selector('.sugchip')
    print('häufig:', pg.locator('.sugchip').all_inner_texts()); pg.screenshot(path='/tmp/sg1.png')
    pg.fill('#q','grenzw'); pg.wait_for_timeout(200); print('prefix:', pg.locator('.sugchip').all_inner_texts())
    pg.locator('.sugchip').first.click(); print('nach Klick:', repr(pg.input_value('#q')), pg.locator('.hit').count(), 'Treffer'); pg.screenshot(path='/tmp/sg2.png')
    pg.press('#q','Enter')
    pg.fill('#q','grenzwrt'); pg.wait_for_timeout(200); print('tippfehler:', pg.locator('.sugnote').all_inner_texts(), pg.locator('.sugchip').all_inner_texts()); pg.screenshot(path='/tmp/sg3.png')
    pg.locator('.sugchip').first.click(); print('korrigiert:', repr(pg.input_value('#q')), pg.locator('.hit').count())
    pg.fill('#q','schranken lemm'); pg.wait_for_timeout(200); print('mehrwort:', pg.locator('.sugchip').all_inner_texts())
    pg.goto('http://localhost:8768/index.html#/suche'); pg.wait_for_selector('.sughead'); print('recent:', pg.locator('.sughead').all_inner_texts(), pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).recent"))
    pg.click('#clrRecent'); print('nach Löschen:', pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).recent"))
    # Name
    pg.click('.tab[data-t=set]'); pg.fill('#uname','Anna'); print(pg.inner_text('#view .sub'), '|', pg.title())
    pg.fill('#uname','Max'); print(pg.inner_text('#view .sub'))
    pg.click('.tab[data-t=start]'); print('home:', pg.inner_text('h1'), '| reload:', end=' '); pg.reload(); pg.wait_for_selector('h1'); print(pg.inner_text('h1'), pg.title())
    pg.click('.tab[data-t=set]'); pg.fill('#uname',''); print('leer:', pg.inner_text('#view .sub')); pg.screenshot(path='/tmp/sg4.png', clip={'x':0,'y':0,'width':390,'height':300})
    print(errs); b.close()
