import time,json
from playwright.sync_api import sync_playwright
errs=[]
now=int(time.time()*1000); D=86400000
log=[]
for d in range(0,80):
    for j in range((d*7)%5):
        log.append([now-d*D-j*1000,['diff1','quer','psy'][(d+j)%3 if (d+j)%3!=2 else 0],'x%d'%j,1 if (d+j)%2 else 0])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    ctx.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({v:1,log:%s}))"%json.dumps(log))
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8765/index.html#/verlauf'); pg.wait_for_selector('.chart')
    for r in ['w','m','j']:
        pg.click(f'#vseg button[data-r={r}]'); print(r, pg.locator('.chart .day').count(), pg.evaluate("document.documentElement.scrollWidth"))
        pg.click('.chart .day >> nth=-2'); print(' detail:', pg.inner_text('.daydet').replace('\n',' | ')[:120]); pg.screenshot(path=f'/tmp/b3_{r}.png')
    pg.click('.chart .day.sel'); print('abgewählt', pg.locator('.daydet').count())
    b.close()
print('errs',errs)
