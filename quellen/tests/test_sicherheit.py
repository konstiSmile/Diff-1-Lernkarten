# Sicherheit (v23): CSP ohne Verstöße, präpariertes Backup ohne Codeausführung, offene \mathbb{-Formel hängt nicht
import json
from playwright.sync_api import sync_playwright
errs=[]; con=[]; dlg=[]; B='http://localhost:8765/index.html'
bad='<img src=x onerror="window.HACK=1">'
backup={'app':'lernkiste','data':{'v':1,'settings':{'name':bad,'theme':'light'},'recent':[bad],
  'custom':{'folders':[{'id':'f1','name':bad,'icon':bad,'cards':[{'id':'c1','q':'Formel $\\mathbb{R$ und '+bad,'a':'$\\frac{1}{2'+bad+'$'}]}]},
  'progress':{bad:'known'},'log':[[1,bad,bad,1]],'tests':{'psy/k1':{'best':{},'wrong':[bad]}}}}
open('/tmp/bad.json','w').write(json.dumps(backup))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: con.append(m.text) if m.type=='error' else None); pg.on('dialog',lambda d:(dlg.append(d.message),d.dismiss()))
    pg.goto(B+'#/einstellungen'); pg.reload(); pg.wait_for_selector('#file', state='attached')
    pg.set_input_files('#file','/tmp/bad.json'); pg.wait_for_selector('#iRepl', state='attached'); pg.eval_on_selector('#iRepl','e=>e.click()'); pg.wait_for_timeout(300)
    print('theme:', pg.evaluate("document.documentElement.getAttribute('data-theme')"))
    for r in ['#/neu','#/neu/f1','#/suche','#/verlauf','#/einstellungen','#/f/psy/k1']:
        pg.goto(B+r); pg.wait_for_timeout(400)
    fid=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).custom.folders[0].id")
    pg.goto(B+'#/neu/'+fid); pg.wait_for_timeout(500)
    print('ordnerseite:', pg.inner_text('#view')[:120].replace('\n',' '))
    print('HACK:', pg.evaluate('window.HACK'), '| img x:', pg.evaluate("document.querySelectorAll('img[src=x]').length"), '| dialoge:', dlg)
    print('gespeichert sauber:', '<' not in json.dumps({k:v for k,v in pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))").items() if k!='custom'}))
    b.close()
print('csp/console errors:', [c for c in con if 'Content Security' in c or 'Refused' in c][:3]); print('errs', errs)
