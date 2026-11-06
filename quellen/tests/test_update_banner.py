from playwright.sync_api import sync_playwright
import re
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width':390,'height':780}); pg = ctx.new_page(); errs=[]
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://localhost:8767/index.html'); pg.wait_for_selector('.tile'); pg.evaluate("navigator.serviceWorker.ready"); pg.wait_for_timeout(1500)
    pg.reload(); pg.wait_for_selector('.tile')   # jetzt von SW kontrolliert
    print('controller', pg.evaluate("!!navigator.serviceWorker.controller"), 'banner', pg.locator('.updbar.on').count())
    # "neue Version" veröffentlichen
    s = open('/tmp/srv/sw.js').read().replace('lernkiste-v6','lernkiste-v7'); open('/tmp/srv/sw.js','w').write(s)
    # mitten im Test starten
    pg.goto('http://localhost:8767/index.html#/f/quer/k10'); pg.wait_for_selector('.mode'); pg.click('.mode >> nth=0'); pg.wait_for_selector('.opt')
    pg.evaluate("localStorage.removeItem('lernkiste-upd'); document.dispatchEvent(new Event('visibilitychange'))")
    pg.wait_for_timeout(2500)
    print('im Test: banner sichtbar?', pg.locator('.updbar').is_visible())
    pg.click('#quit'); pg.wait_for_selector('.mode'); pg.wait_for_timeout(300)
    print('nach Test: banner sichtbar?', pg.locator('.updbar').is_visible()); pg.screenshot(path='/tmp/upd.png', clip={'x':0,'y':560,'width':390,'height':220})
    pg.click('#updGo'); pg.wait_for_selector('.mode'); print('nach Neu laden:', pg.locator('.updbar.on').count(), 'cache', pg.evaluate("caches.keys()"))
    print(errs); b.close()
