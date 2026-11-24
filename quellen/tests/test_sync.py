# v49: Sync-Code mit Supabase-Mock (zwei Geräte = zwei Browser-Kontexte, gemeinsamer Speicher)
import json, hashlib
from playwright.sync_api import sync_playwright
B='http://localhost:8765/index.html'; store={}; errs=[]; calls=[]
def handler(route):
    req=route.request; fn=req.url.rsplit('/',1)[-1]; body=json.loads(req.post_data or '{}')
    assert req.headers.get('apikey','').startswith('sb_publishable_')
    h=hashlib.sha256(body['p_code'].encode()).hexdigest(); calls.append(fn)
    if fn=='lk_get': r=store.get(h); route.fulfill(status=200,content_type='application/json',body=json.dumps(r))
    elif fn=='lk_put': store[h]={'data':body['p_data'],'updated_at':'x'}; route.fulfill(status=200,content_type='application/json',body='"x"')
    elif fn=='lk_delete': store.pop(h,None); route.fulfill(status=204,body='')
def dev(b, prog, ptime, name):
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    ctx.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify(%s))" % json.dumps({'settings':{'statsAsked':1,'name':name},'progress':prog,'ptime':ptime}))
    ctx.route('https://qbdpzamygonpruaafcrt.supabase.co/**', handler)
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e))); return pg
def db(pg): return json.loads(pg.evaluate("localStorage.getItem('lernkiste-v1')"))
def opensync(pg):
    pg.goto(B+'#/einstellungen'); pg.wait_for_selector('.shead')
    if pg.get_attribute('.shead:has-text("Daten und App")','aria-expanded')!='true': pg.click('.shead:has-text("Daten und App")')
ok=lambda c,m: print(('OK   ' if c else 'FAIL ')+m)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    A=dev(b,{'k1-a':'known','k1-b':'again'},{'k1-a':1000,'k1-b':1000},'Konsti')
    opensync(A); A.click('#sNew'); A.wait_for_timeout(800)
    code=A.inner_text('.synccode'); ok(len(code)==24 and code.count('-')==4, 'Code-Format '+code)
    ok(len(store)==1, 'Upload nach Code erzeugen')
    up=list(store.values())[0]['data']; ok('name' not in up['settings'] and 'custom' not in up, 'Name/eigene Karten nicht hochgeladen')
    ok('Zuletzt abgeglichen heute' in A.inner_text('#syncStat'), 'Status: '+A.inner_text('#syncStat'))
    Bd=dev(b,{'k1-b':'known','k1-c':'known'},{'k1-b':2000,'k1-c':500},'Anna')
    opensync(Bd); Bd.click('#sJoin'); Bd.fill('#sIn','falsch-code-1234-5678-abcd'); Bd.click('#sGo'); Bd.wait_for_timeout(500)
    ok(Bd.query_selector('#sNow') is None, 'falscher Code wird abgelehnt')
    Bd.fill('#sIn',code.lower()); Bd.click('#sGo'); Bd.wait_for_timeout(1000)
    d=db(Bd)['progress']; ok(d=={'k1-a':'known','k1-b':'known','k1-c':'known'}, 'B zusammengeführt '+str(d))
    ok(db(Bd)['settings']['name']=='Anna', 'Name auf B bleibt')
    A.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); A.wait_for_timeout(1000)
    ok(db(A)['progress']=={'k1-a':'known','k1-b':'known','k1-c':'known'}, 'A übernimmt neuere Bewertung von B '+str(db(A)['progress']))
    # Lernstand auf A zurücksetzen -> B verliert ihn
    A.goto(B+'#/einstellungen'); A.wait_for_selector('.shead'); A.click('.shead:has-text("Daten und App")') if A.get_attribute('.shead:has-text("Daten und App")','aria-expanded')!='true' else None; A.click('#bProg'); A.click('#bProg')
    A.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); A.wait_for_timeout(1000)
    Bd.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); Bd.wait_for_timeout(1000)
    ok(db(Bd)['progress']=={}, 'Reset gilt auf B '+str(db(Bd)['progress']))
    # Karte auf B bewerten über echte UI
    Bd.goto(B+'#/f/diff1/allg-b?c=allg-induktion'); Bd.wait_for_timeout(800)
    btn=Bd.query_selector('#bKnown')
    if btn: btn.click(); Bd.wait_for_timeout(300)
    Bd.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); Bd.wait_for_timeout(1000)
    A.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); A.wait_for_timeout(1000)
    ok(btn is not None and len(db(A)['progress'])==1 and len(db(A)['log'])>=1, 'Bewertung von B kommt auf A an '+str(db(A)['progress']))
    # Beenden/Löschen
    opensync(A); A.click('#sDel'); A.click('#sDel'); A.wait_for_timeout(600)
    ok(not store and A.query_selector('#sNew'), 'Online-Kopie gelöscht, A ohne Sync')
    A.screenshot(path='/tmp/sync_aus.png'); opensync(Bd); Bd.screenshot(path='/tmp/sync_an.png')
    ok(Bd.evaluate("document.documentElement.scrollWidth")<=390,'kein Überlauf')
    b.close()
print('errs',errs)
