from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8765/index.html#/einstellungen'); pg.wait_for_selector('.ghead')
    print('Gruppen',pg.locator('.ghead').count(),'offen',pg.locator('.group.open').count(), 'sichtbare setrows', pg.locator('.setrow:visible').count())
    pg.screenshot(path='/tmp/set_zu.png')
    pg.click('.ghead >> nth=1'); pg.click('#view .seg[data-k=theme] button >> nth=1')
    print('nach Wahl offen',pg.locator('.group.open').count(), pg.evaluate("document.documentElement.dataset.theme"))
    pg.click('.ghead >> nth=0'); pg.fill('#uname','Anna'); print(pg.inner_text('#view .sub'))
    pg.screenshot(path='/tmp/set_auf.png'); print('sw',pg.evaluate("document.documentElement.scrollWidth"))
    b.close()
print('errs',errs)
