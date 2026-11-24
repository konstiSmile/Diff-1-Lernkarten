import json
from playwright.sync_api import sync_playwright
errs=[]; got=[]
B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    ctx.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1}}))")
    ctx.route('https://script.google.com/**', lambda r: (got.append(json.loads(r.request.post_data)), r.fulfill(status=200, body='ok')))
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'#/einstellungen'); pg.reload(); pg.wait_for_selector('.shead')
    pg.wait_for_selector('#fbText')
    print('button disabled leer:', pg.is_disabled('#fbSend'))
    pg.fill('#fbText','Test: Karten super, bitte mehr Psycho'); pg.click('#fbSend'); pg.wait_for_timeout(800)
    print('gesendet:', got, '| toast:', pg.inner_text('.toast') if pg.query_selector('.toast') else '-')
    ctx.set_offline(True); pg.fill('#fbText','Offline-Nachricht'); pg.click('#fbSend'); pg.wait_for_timeout(500)
    print('offline info:', pg.inner_text('#fbInfo'), '| queue', pg.evaluate("localStorage.getItem('lernkiste-fbq')")[:60], '| gesendet', len(got))
    ctx.set_offline(False); pg.wait_for_timeout(1500)
    print('nach online gesendet:', len(got), got[-1]['text'], '| queue', pg.evaluate("localStorage.getItem('lernkiste-fbq')"))
    pg.fill('#fbWeb','spam'); pg.fill('#fbText','bot'); pg.click('#fbSend'); pg.wait_for_timeout(500); print('honeypot gesendet:', len(got))
    print('backup enthält dev?', 'lernkiste-dev' in pg.evaluate("localStorage.getItem('lernkiste-v1')"))
    print('ovf', pg.evaluate("document.documentElement.scrollWidth"))
    pg.fill('#fbWeb',''); pg.fill('#fbText','Hier steht ein Beispieltext.'); pg.screenshot(path='/tmp/fb.png')
    b.close()
print('errs',errs)
