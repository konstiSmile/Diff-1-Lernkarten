# v50: Einführung beim ersten Öffnen + Pflichtfrage Statistik
import json
from playwright.sync_api import sync_playwright
B='http://localhost:8765/index.html'; errs=[]; pings=[]
ok=lambda c,m: print(('OK   ' if c else 'FAIL ')+m)
IOS='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
def ctx(b, init=None):
    c=b.new_context(viewport={'width':390,'height':780},service_workers='block',user_agent=IOS,has_touch=True)
    if init is not None: c.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify(%s))"%json.dumps(init))
    c.route('https://script.google.com/**', lambda r:(pings.append(r.request.post_data), r.fulfill(status=200,body='ok')))
    pg=c.new_page(); pg.on('pageerror',lambda e:errs.append(str(e))); return pg
def db(pg): return json.loads(pg.evaluate("localStorage.getItem('lernkiste-v1')"))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    # 1 neu: alle Seiten
    pg=ctx(b); pg.goto(B); pg.wait_for_selector('.ob'); pg.wait_for_timeout(400)
    ok(len(pg.query_selector_all('.obpage'))==4,'neu: 4 Seiten'); pg.screenshot(path='/tmp/ob1.png')
    pg.fill('#obName','Anna'); pg.click('#obNext'); pg.wait_for_timeout(400); pg.screenshot(path='/tmp/ob2.png')
    pg.click('#obNext'); pg.wait_for_timeout(400); pg.screenshot(path='/tmp/ob3.png')
    pg.click('#obNext'); pg.wait_for_timeout(400); pg.screenshot(path='/tmp/ob4.png')
    ok(not pg.is_visible('#obSkip') and pg.is_visible('#stYes') and pg.is_visible('#stNo'),'letzte Seite: nur Ja/Nein')
    pg.click('#obPriv'); pg.wait_for_timeout(300); ok(pg.is_visible('.pvcard'),'Datenschutz über Einführung'); pg.click('.pvx')
    pg.keyboard.press('Escape'); ok(pg.query_selector('.ob') is not None,'Escape schließt nicht')
    pg.click('#stYes'); pg.wait_for_timeout(500)
    d=db(pg)['settings']; ok(pg.query_selector('.ob') is None and d['stats']==1 and d['statsAsked'] and d['obDone'] and d['name']=='Anna','Ja gespeichert, Name Anna')
    pg.reload(); pg.wait_for_timeout(2500); ok(pg.query_selector('.ob') is None,'kommt nicht wieder')
    # 2 neu: Überspringen -> Statistik-Seite
    pg=ctx(b); pg.goto(B+'#/f/diff1'); pg.wait_for_selector('.ob'); pg.click('#obSkip'); pg.wait_for_timeout(400)
    ok(pg.is_visible('#stNo'),'Überspringen führt zur Frage'); pg.click('#stNo'); pg.wait_for_timeout(300)
    d=db(pg)['settings']; ok(d['stats']==0 and d['statsAsked'],'Nein gespeichert')
    # 3 alt ohne Antwort -> nur Frage, sofort
    pg=ctx(b,{'settings':{'statsAsked':0},'log':[[1,'diff1','x',1]]}); pg.goto(B); pg.wait_for_selector('.ob',timeout=3000)
    ok(len(pg.query_selector_all('.obpage'))==1 and pg.is_visible('#stYes') and not pg.is_visible('#obSkip'),'alt ohne Antwort: nur Frage'); pg.screenshot(path='/tmp/ob5.png')
    # 4 alt mit Antwort -> nichts
    pg=ctx(b,{'settings':{'statsAsked':1},'log':[[1,'diff1','x',1]]}); pg.goto(B); pg.wait_for_timeout(2500); ok(pg.query_selector('.ob') is None,'alt mit Antwort: nichts')
    # 5 Wischen
    pg=ctx(b); pg.goto(B); pg.wait_for_selector('.ob')
    pg.evaluate("""()=>{const w=document.querySelector('.ob');const t=(type,x)=>{const tc=new Touch({identifier:1,target:w,clientX:x,clientY:400});w.dispatchEvent(new TouchEvent(type,{touches:type=='touchend'?[]:[tc],changedTouches:[tc],bubbles:true}))};t('touchstart',300);t('touchend',100)}""")
    pg.wait_for_timeout(400); ok(pg.get_attribute('.obpage:nth-child(2)','aria-hidden')=='false','Wischen blättert')
    b.close()
print('errs',errs)
