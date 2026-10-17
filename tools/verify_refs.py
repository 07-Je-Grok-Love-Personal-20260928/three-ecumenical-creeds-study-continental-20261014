"""经文参考逐条核对：页面中每个 .refs2 行内的 .rf1 文本序列 == data/*.json 中 ref 块的列表（顺序与文字完全一致）。"""
import json,re,html,sys
def blocks(f,key):
    d=json.load(open(f'data/{f}.json',encoding='utf-8'))
    if f=='bc': it=[b for a in d['articles'] for b in a['blocks']]
    elif f=='hc': it=[b for l in d['lds'] for b in l['blocks']]
    else: it=[b for h in d['heads'] for i in h['items'] for b in i['blocks']]
    return [b['x'] for b in it if b['t']=='ref']
bad=0
for f,page in (('bc','bc.html'),('hc','hc.html'),('dort','dort.html')):
    h=open(page,encoding='utf-8').read()
    got=[[html.unescape(x) for x in re.findall(r'<span class="rf1" role="listitem"><b class="nb">\d+</b>(.*?)</span>',m)] for m in re.findall(r'<div class="refs2"[^>]*>(.*?)</div>',h,flags=re.S)]
    want=blocks(f,None); ok=got==want; bad+=not ok
    print(page,'ref blocks',len(got),'items',sum(map(len,got)),'OK' if ok else f'MISMATCH want {len(want)}')
# --- 信经页中的紧凑经文行：每行 == 对应主日问的 ref 块 ---
d=json.load(open('data/hc.json',encoding='utf-8'))
def ldrows(n): return [b['x'] for b in d['lds'][n-1]['blocks'] if b['t']=='ref']
def rows(page):
    h=open(page,encoding='utf-8').read()
    return [[html.unescape(x) for x in re.findall(r'<span class="rf1" role="listitem"><b class="nb">\d+</b>(.*?)</span>',m)] for m in re.findall(r'<div class="refs2 rq"[^>]*>(.*?)</div>',h,flags=re.S)]
for page,lds in (('apostles.html',range(7,23)),('nicene.html',[8,11,13,14,20,21,22])):
    want=[x for n in lds for x in ldrows(n)]; got=rows(page); ok=got==want; bad+=not ok
    print(page,'creed-page rows',len(got),'items',sum(map(len,got)),'OK' if ok else f'MISMATCH got {len(got)} want {len(want)}')
sys.exit(1 if bad else 0)
