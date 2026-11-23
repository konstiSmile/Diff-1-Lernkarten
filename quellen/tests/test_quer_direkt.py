# v42: Bereiche mit genau einem Kapitel öffnen direkt das Kapitel
from playwright.sync_api import sync_playwright
errs=[]; B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_context(viewport={'width':390,'height':780},service_workers='block').new_page()
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(B+'#/f/quer'); pg.reload(); pg.wait_for_selector('.tile')
    hrefs=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('quer:',hrefs)
    if hrefs!=['#/f/quer/k10','#/f/quer/k11','#/f/quer/u/allg']: errs.append('hrefs '+str(hrefs))
    for h,want in (('#/f/quer/k10','#/f/quer'),('#/f/quer/k11','#/f/quer')):
        pg.click(f'.tile[href="{h}"]'); pg.wait_for_selector('.mode')
        back=pg.get_attribute('.nav a','href'); print(h,'zurück:',back, pg.inner_text('.nav a'))
        if back!=want: errs.append('back '+h+' '+str(back))
        pg.click('.nav a'); pg.wait_for_selector('.tile')
    for g,k in (('mv','k10'),('dgl','k11')):
        pg.goto(B+'#/f/quer/u/'+g); pg.wait_for_selector('.mode')
        if pg.evaluate('location.hash')!='#/f/quer/'+k: errs.append('redirect '+g)
    # Psycho: Bereiche mit mehreren Kapiteln bleiben unverändert
    pg.goto(B+'#/f/psy'); pg.wait_for_selector('.tile')
    ph=pg.eval_on_selector_all('.tile','els=>els.map(e=>e.getAttribute("href"))'); print('psy:',ph)
    if ph!=['#/f/psy/u/pers','#/f/psy/u/entw','#/f/psy/u/diag']: errs.append('psy '+str(ph))
    pg.goto(B+'#/f/psy/d3'); pg.wait_for_selector('.mode')
    if pg.get_attribute('.nav a','href')!='#/f/psy/u/diag': errs.append('psy back')
    pg.goto(B+'#/f/quer'); pg.wait_for_selector('.tile'); pg.screenshot(path='/tmp/quer_direkt.png')
    b.close()
print('FEHLER' if errs else 'OK', errs)
