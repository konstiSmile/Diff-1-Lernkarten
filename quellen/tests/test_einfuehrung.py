# v50/v65: Einführung beim ersten Öffnen, Statistik Opt-out
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
    # 1 neu: alle Seiten, keine Statistik-Frage (v65)
    pg=ctx(b); pg.goto(B); pg.wait_for_selector('.ob'); pg.wait_for_timeout(400)
    ok(len(pg.query_selector_all('.obpage'))==3,'neu: 3 Seiten'); ok(pg.query_selector('#stYes') is None,'keine Ja/Nein-Frage')
    pg.fill('#obName','Anna'); pg.click('#obNext'); pg.wait_for_timeout(400); pg.click('#obNext'); pg.wait_for_timeout(400); pg.screenshot(path='/tmp/ob3.png')
    ok(not pg.is_visible('#obSkip') and pg.is_visible('#obGo'),'letzte Seite: Los geht’s')
    pg.click('#obPriv'); pg.wait_for_timeout(300); ok(pg.is_visible('.pvcard'),'Datenschutz über Einführung'); pg.click('.pvx')
    pg.click('#obGo'); pg.wait_for_timeout(500)
    d=db(pg)['settings']; ok(pg.query_selector('.ob') is None and d['stats']==1 and d['obDone'] and d['name']=='Anna','fertig, Statistik an, Name Anna')
    pg.reload(); pg.wait_for_timeout(2500); ok(pg.query_selector('.ob') is None,'kommt nicht wieder')
    # 2 neu: Überspringen -> letzte Seite
    pg=ctx(b); pg.goto(B+'#/f/diff1'); pg.wait_for_selector('.ob'); pg.click('#obSkip'); pg.wait_for_timeout(400)
    ok(pg.is_visible('#obGo'),'Überspringen führt ans Ende')
    # 3 alt mit „Nein“ -> keine Einführung, Statistik einmalig an
    pg=ctx(b,{'settings':{'stats':0,'statsAsked':1},'log':[[1,'diff1','x',1]]}); pg.goto(B); pg.wait_for_timeout(2500)
    d=db(pg)['settings']; ok(pg.query_selector('.ob') is None and d['stats']==1 and d['st65']==1,'alt mit Nein: nichts, Statistik an')
    # 4 alt nie gefragt -> nichts, an; danach Ausschalten bleibt
    pg=ctx(b,{'settings':{'statsAsked':0},'log':[[1,'diff1','x',1]]}); pg.goto(B); pg.wait_for_timeout(2500)
    d=db(pg)['settings']; ok(pg.query_selector('.ob') is None and d['stats']==1,'alt ohne Antwort: nichts, an')
    pg.evaluate("()=>{const d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.stats=0;localStorage.setItem('lernkiste-v1',JSON.stringify(d))}")
    pg.reload(); pg.wait_for_timeout(1500); ok(db(pg)['settings']['stats']==0,'Ausschalten bleibt nach Neustart')
    # 5 Wischen
    pg=ctx(b); pg.goto(B); pg.wait_for_selector('.ob')
    pg.evaluate("""()=>{const w=document.querySelector('.ob');const t=(type,x)=>{const tc=new Touch({identifier:1,target:w,clientX:x,clientY:400});w.dispatchEvent(new TouchEvent(type,{touches:type=='touchend'?[]:[tc],changedTouches:[tc],bubbles:true}))};t('touchstart',300);t('touchend',100)}""")
    pg.wait_for_timeout(400); ok(pg.get_attribute('.obpage:nth-child(2)','aria-hidden')=='false','Wischen blättert')
    b.close()
print('errs',errs)
