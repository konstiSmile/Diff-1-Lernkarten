from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block',has_touch=True)
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8765/index.html'); pg.wait_for_selector('.tile')
    print('tiles',pg.locator('.tilewrap').count(), 'hiddenlink', pg.locator('#hidLink').count())
    # Menü
    pg.click('.tilewrap[data-sid=quer] .tilemenu'); pg.screenshot(path='/tmp/b2_menu.png'); pg.click('.tilepop button')
    print('nach Menü', pg.locator('.tilewrap').count(), pg.inner_text('#hidLink'), pg.inner_text('.toast'))
    pg.screenshot(path='/tmp/b2_hidden.png')
    pg.click('.toastact'); print('undo', pg.locator('.tilewrap').count(), pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).hidden"))
    # Wischen per CDP
    cdp=ctx.new_cdp_session(pg)
    def swipe(sel,dx):
        bb=pg.locator(sel).bounding_box(); x=bb['x']+bb['width']*0.7; y=bb['y']+bb['height']/2
        cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        for i in range(1,9): cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x-dx*i/8,'y':y}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    swipe('.tilewrap[data-sid=psy] .tile',30); pg.wait_for_timeout(400); print('kurz gewischt',pg.locator('.tilewrap').count())
    swipe('.tilewrap[data-sid=psy] .tile',200); pg.wait_for_timeout(500); print('weit gewischt',pg.locator('.tilewrap').count(), pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).hidden"))
    # Link, Einblenden
    pg.click('#hidLink'); pg.screenshot(path='/tmp/b2_list.png'); pg.click('[data-show=psy]'); print('wieder',pg.locator('.tilewrap').count(), pg.locator('#hidLink').count())
    # Suche blendet aus
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.hidden=['diff1'];localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.goto('http://localhost:8765/index.html#/suche?q=folge'); pg.reload(); pg.wait_for_selector('.hit,.filters')
    print('such-filter', pg.locator('.filters button').all_inner_texts())
    pg.goto('http://localhost:8765/index.html#/'); pg.reload(); pg.wait_for_selector('.tile')
    print('sw',pg.evaluate("document.documentElement.scrollWidth"))
    # Tap öffnet Fach trotz Wisch-Code
    pg.click('.tilewrap[data-sid=quer] .tile'); pg.wait_for_selector('h1'); print(pg.url)
    b.close()
print('errs',errs)
