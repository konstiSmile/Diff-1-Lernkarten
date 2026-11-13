# Nutzungsstatistik (Opt-in, ohne Geräte-ID), einmalige Frage und Datenschutz-Kachel
import json
from playwright.sync_api import sync_playwright
errs=[]; got=[]
B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    ctx.route('https://script.google.com/**', lambda r: (got.append(json.loads(r.request.post_data)), r.fulfill(status=200, body='ok')))
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    # 1) Frage erscheint, ✕ = keine Antwort -> beim nächsten Start erneut
    pg.goto(B); pg.wait_for_selector('#stYes', timeout=4000); print('frage da, pings:', got)
    pg.click('.pvx'); pg.goto(B+'#/f/psy'); pg.wait_for_timeout(2000); print('gleiche Sitzung nicht erneut:', pg.locator('#stYes').count()==0)
    pg.reload(); pg.wait_for_selector('#stYes', timeout=4000); print('nach Neustart erneut: True')
    # 2) Nein -> nie wieder, keine Pings
    pg.click('#stNo'); pg.wait_for_timeout(300)
    st=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).settings"); print('nein:', st['stats'], st['statsAsked']>1e12)
    pg.reload(); pg.wait_for_timeout(2200); print('nach nein keine frage:', pg.locator('#stYes').count()==0, 'pings:', got)
    # 3) Schalter an in Einstellungen, Kachel
    pg.goto(B+'#/einstellungen'); pg.wait_for_selector('.ghead'); pg.click('.ghead:has-text("App")')
    pg.click('.seg[data-k=stats] button[data-v="1"]'); pg.wait_for_timeout(200)
    print('keys:', pg.evaluate("Object.keys(localStorage)"))
    pg.click('#privRow'); pg.wait_for_selector('.pvcard'); pg.click('.pvok'); print('kachel zu:', pg.locator('.pvcard').count()==0)
    pg.click('#bPriv'); pg.keyboard.press('Escape'); print('esc zu:', pg.locator('.pvcard').count()==0)
    pg.reload(); pg.wait_for_timeout(600); pg.goto(B+'#/f/psy'); pg.goto(B+'#/f/psy/u/pers'); pg.goto(B+'#/f/diff1'); pg.wait_for_timeout(300)
    print('an – pings:', [(x['art'],x['fach']) for x in got], 'felder:', sorted(got[0].keys()) if got else None)
    # 4) Ja in der Frage (neuer Kontext)
    ctx2=b.new_context(viewport={'width':390,'height':780},service_workers='block'); got2=[]
    ctx2.route('https://script.google.com/**', lambda r: (got2.append(json.loads(r.request.post_data)), r.fulfill(status=200, body='ok')))
    p2=ctx2.new_page(); p2.on('pageerror',lambda e:errs.append(str(e)))
    p2.goto(B+'#/f/quer'); p2.wait_for_selector('#stYes', timeout=4000); p2.locator('.pvcard').screenshot(path='/home/claude/patch/frage.png'); p2.click('#stYes'); p2.wait_for_timeout(300)
    print('ja – pings:', [(x['art'],x['fach']) for x in got2], 'ovf', p2.evaluate('document.documentElement.scrollWidth'))
    print('errs', errs)
    b.close()
