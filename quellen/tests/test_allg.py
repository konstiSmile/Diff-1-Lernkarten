# v48: „Allgemein“ als Gruppe mit vier Unterbereichen (v43: gemeinsamer Pool) (Mathe) – gemeinsamer Pool für Querschnitt und Diff 1
import json, re, time
from playwright.sync_api import sync_playwright
errs=[]; B='http://localhost:8765/index.html'
C=json.loads(re.sub(r'^window\.CONTENT = |;\s*$','',open('../../content.js',encoding='utf-8').read()))
S={s['id']:s for s in C['subjects']}
def pool(sid):
    chs=[c for c in S[sid]['chapters'] if c.get('group')=='allg']
    return chs, dict(cards=[x for c in chs for x in c['cards']], items=[x for c in chs for x in c['items']], group='allg')
qchs,qa=pool('quer'); dchs,da=pool('diff1')
print('Bereiche quer:',[(c['title'],len(c['cards']),len(c['items'])) for c in qchs]); print('Bereiche diff1:',[(c['title'],len(c['cards']),len(c['items'])) for c in dchs])
if [c['id'] for c in qchs]!=['allg-f','allg-s','allg-b','allg-r'] or [c['id'] for c in dchs]!=['allg-f','allg-s','allg-b','allg-r']: errs.append('bereiche')
ids=[x['id'] for c in qchs for x in c['cards']+c['items']]
if len(ids)!=len(set(ids)): errs.append('doppelt in Bereichen')
print('quer allg:',len(qa['cards']),'Karten',len(qa['items']),'Fragen · diff1 allg:',len(da['cards']),'Karten',len(da['items']),'Fragen')
qids={x['id'] for x in qa['cards']+qa['items']}; dids={x['id'] for x in da['cards']+da['items']}
# ab v47 gibt es auch reine Diff-1-Inhalte (subj D); geteilt = Schnittmenge
shared=dids&qids
if not shared or not (dids-qids): errs.append('diff1-Teilmenge')
if qa.get('group')!='allg': errs.append('gruppe')
raw=json.dumps(C)
for ch in (qa,da):
    for x in ch['cards']+ch['items']:
        if re.search(r'\\\\[(\[]', json.dumps(x)): errs.append('TeX roh '+x['id'])
# Karten/Fragen gesamt (für Gemischt mit beiden Fächern)
def tot(key): return sum(len(c.get(key) or []) for s in ('quer','diff1') for c in S[s]['chapters'] if not c.get('placeholder'))
uc=tot('cards')-len([x for x in da['cards'] if x['id'] in shared]); ui=tot('items')-len([x for x in da['items'] if x['id'] in shared])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block'); ctx.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,obDone:1}}))"); pg=ctx.new_page()
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'#/f/quer'); pg.reload(); pg.wait_for_selector('.tile')
    hrefs=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('quer:',hrefs)
    if hrefs!=['#/f/quer/k10','#/f/quer/k11','#/f/quer/u/allg']: errs.append('quer tiles '+str(hrefs))
    pg.screenshot(path='/tmp/allg_quer.png')
    pg.click('.tile[href="#/f/quer/u/allg"]'); pg.wait_for_selector('.tile')
    uh=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('quer/allg:',uh)
    if uh!=['#/f/quer/allg-f','#/f/quer/allg-s','#/f/quer/allg-b','#/f/quer/allg-r']: errs.append('unterbereiche '+str(uh))
    pg.screenshot(path='/tmp/allg_bereiche.png')
    pg.click('.tile[href="#/f/quer/allg-r"]'); pg.wait_for_selector('.mode')
    if pg.get_attribute('.nav a','href')!='#/f/quer/u/allg': errs.append('zurück quer '+str(pg.get_attribute('.nav a','href')))
    # alte Links auf „allg“ leiten weiter
    pg.goto(B+'#/f/quer/allg'); time.sleep(0.4)
    if pg.evaluate('location.hash')!='#/f/quer/u/allg': errs.append('redirect allg '+pg.evaluate('location.hash'))
    pg.goto(B+'#/f/diff1/allg?c=allg-induktion'); time.sleep(0.4)
    if pg.evaluate('location.hash')!='#/f/diff1/allg-b?c=allg-induktion': errs.append('redirect karte '+pg.evaluate('location.hash'))
    pg.goto(B+'#/f/diff1/allg?q=allg-mc-68'); time.sleep(0.4)
    if pg.evaluate('location.hash')!='#/f/diff1/allg-r?q=allg-mc-68': errs.append('redirect frage '+pg.evaluate('location.hash'))
    pg.goto(B+'#/f/diff1'); pg.reload(); pg.wait_for_selector('.tile')
    dh=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('diff1:',dh)
    if dh!=['#/f/diff1/k1','#/f/diff1/k2','#/f/diff1/u/allg']: errs.append('diff1 tiles '+str(dh))
    pg.screenshot(path='/tmp/allg_diff1.png')
    # Karte mit Tabelle öffnen
    pg.goto(B+'#/f/quer/allg-f?c=allg-sin-cos-werte'); pg.wait_for_selector('.card'); pg.click('.card')
    time.sleep(0.3); pg.screenshot(path='/tmp/allg_karte.png')
    # Gemischt: beide Fächer gewählt → geteilte Inhalte nur einmal
    pg.evaluate("()=>{var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.mixSubs=['quer','diff1'];localStorage.setItem('lernkiste-v1',JSON.stringify(d))}")
    pg.goto(B+'#/mix'); pg.reload(); pg.wait_for_selector('#mxC')
    t1,t2=pg.inner_text('#mxC'),pg.inner_text('#mxT'); print('Gemischt:',t1,t2,'erwartet',uc,ui)
    if t1!=f'Karteikarten ({uc})' or t2!=f'Tests ({ui})': errs.append('mix '+t1+' '+t2)
    # Heute fällig: geteilte Frage nur einmal
    old=int((time.time()-3*86400)*1000)
    pg.evaluate("t=>{var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.log=[[t,'quer','allg-mc-11',1],[t,'diff1','allg-mc-11',1],[t,'quer','allg-mc-01',1]];localStorage.setItem('lernkiste-v1',JSON.stringify(d))}",old)
    pg.goto(B+'#/'); pg.reload(); pg.wait_for_selector('.hello')
    td=pg.inner_text('.hello span').replace('\n',' '); print('fällig:',td)
    if not re.search(r'\b2 Fragen warten',td): errs.append('due '+td)
    # Suche: unter „Alle“ einmal, je Fach einmal
    pg.goto(B+'#/suche'); pg.wait_for_selector('input'); pg.fill('input','Additionstheoreme Sinus Cosinus Summe')
    time.sleep(0.4); fl=pg.inner_text('.filters'); print('Suche:',fl.replace('\n',' '))
    hits=pg.eval_on_selector_all('.hit','els=>els.map(e=>e.getAttribute("href"))')
    n=sum(1 for h in hits if 'c=allg-additionstheoreme' in h)
    if n!=1: errs.append('suche alle '+str(n))
    b.close()
print('FEHLER' if errs else 'OK', errs)
