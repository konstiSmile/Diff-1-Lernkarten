# v43: „Allgemein“ (Mathe) – gemeinsamer Pool für Querschnitt und Diff 1
import json, re, time
from playwright.sync_api import sync_playwright
errs=[]; B='http://localhost:8765/index.html'
C=json.loads(re.sub(r'^window\.CONTENT = |;\s*$','',open('../../content.js',encoding='utf-8').read()))
S={s['id']:s for s in C['subjects']}
qa=[c for c in S['quer']['chapters'] if c['id']=='allg'][0]; da=[c for c in S['diff1']['chapters'] if c['id']=='allg'][0]
print('quer allg:',len(qa['cards']),'Karten',len(qa['items']),'Fragen · diff1 allg:',len(da['cards']),'Karten',len(da['items']),'Fragen')
qids={x['id'] for x in qa['cards']+qa['items']}; dids={x['id'] for x in da['cards']+da['items']}
if not dids or not dids<=qids: errs.append('diff1-Teilmenge')
if qa.get('group')!='allg': errs.append('gruppe')
raw=json.dumps(C)
for ch in (qa,da):
    for x in ch['cards']+ch['items']:
        if re.search(r'\\\\[(\[]', json.dumps(x)): errs.append('TeX roh '+x['id'])
# Karten/Fragen gesamt (für Gemischt mit beiden Fächern)
def tot(key): return sum(len(c.get(key) or []) for s in ('quer','diff1') for c in S[s]['chapters'] if not c.get('placeholder'))
uc=tot('cards')-len(da['cards']); ui=tot('items')-len(da['items'])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block'); pg=ctx.new_page()
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'#/f/quer'); pg.reload(); pg.wait_for_selector('.tile')
    hrefs=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('quer:',hrefs)
    if hrefs!=['#/f/quer/k10','#/f/quer/k11','#/f/quer/allg']: errs.append('quer tiles '+str(hrefs))
    pg.screenshot(path='/tmp/allg_quer.png')
    pg.click('.tile[href="#/f/quer/allg"]'); pg.wait_for_selector('.mode')
    if pg.get_attribute('.nav a','href')!='#/f/quer': errs.append('zurück quer')
    pg.screenshot(path='/tmp/allg_kapitel.png')
    pg.goto(B+'#/f/quer/u/allg'); pg.wait_for_selector('.mode')
    if pg.evaluate('location.hash')!='#/f/quer/allg': errs.append('redirect allg')
    pg.goto(B+'#/f/diff1'); pg.wait_for_selector('.tile')
    dh=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('diff1:',dh)
    if '#/f/diff1/allg' not in dh: errs.append('diff1 tile')
    # Karte mit Tabelle öffnen
    pg.goto(B+'#/f/quer/allg?c=allg-sin-cos-werte'); pg.wait_for_selector('.card'); pg.click('.card')
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
