# -*- coding: utf-8 -*-
from core import *
from c_core import HC_CORE,BC_CORE,DORT_CORE,AP_CORE,NI_CORE,AT_CORE,core_tbl
PC={"总纲":"0","困苦":"1","拯救":"2","感恩":"3"}
def core_l2():
    from c_core import HC_CORE,BC_CORE,DORT_CORE,AP_CORE,NI_CORE,AT_CORE,core_tbl
    from c_titles import PART_RANGE,BC_GROUPS,HC52,BC37
    import json
    _dt=json.load(open('data/dort.json',encoding='utf-8'))
    import creedlib as CL
    x=('<p>每个主日、每条信条、每项教义和每个信经条目各配一组：<b>🎯 核心一句</b>（抓住本质）、<b>🧠 记忆钩</b>（口诀、数字、前后对比）、<b>💡 为何重要</b>。这些是本站撰写的学习用语，不是 CCI 原文；每行编号可点回深读页。</p>'
       +'<div class="legend"><span class="cwk k1">🎯 核心</span><span class="cwk k2">🧠 记忆钩</span><span class="cwk k3">💡 为何重要</span></div>')
    for k,lab,lo,hi in PART_RANGE:
        rows=[(f"主日{n}",HC52[n][0],HC_CORE[n],f"hc.html#ld{n}") for n in range(lo,hi+1)]
        x+=L3(f"mr-hc{PC[k]}",f"HC 核心速记 · {lab}（主日{lo}"+(f"–{hi}" if hi!=lo else "")+"）",core_tbl(rows),"list",cls="mmg")
    for g,lab,col,lo,hi,ico in BC_GROUPS:
        rows=[(f"第{n}条",BC37[n][0],BC_CORE[n],f"bc.html#bc-{n}") for n in range(lo,hi+1)]
        x+=L3(f"mr-bc{g}",f"BC 核心速记 · {lab}（第{lo}–{hi}条）",core_tbl(rows),ico,cls="mmg")
    rows=[(f"第{h['num']}项",h["title"].split(" ",1)[-1],DORT_CORE[h["id"]],f"dort.html#dt-{h['id']}") for h in _dt["heads"]]
    x+=L3("mr-dt","Dort 核心速记 · 四项",core_tbl(rows),"shield",cls="mmg")
    rows=[(f"第{n}条",CL.AP_TITLES[n][0],AP_CORE[n],f"creeds.html#ap-a{n}") for n in range(1,13)]
    x+=L3("mr-ap","使徒信经核心速记 · 12 条",core_tbl(rows),"scroll",cls="mmg")
    rows=[(f"第{n}节",CL.NI_TITLES[n][0],NI_CORE[n],f"creeds.html#ni-a{n}") for n in range(1,14)]
    x+=L3("mr-ni","尼西亚信经核心速记 · 13 节",core_tbl(rows),"scroll",cls="mmg")
    rows=[(f"第{lo}–{hi}点" if hi!=lo else f"第{lo}点",nm,AT_CORE[g],f"creeds.html#at-g{g}") for g,(nm,lo,hi,gi) in CL.AT_GROUPS.items()]
    x+=L3("mr-at","亚他那修信经核心速记 · 11 组",core_tbl(rows),"scroll",cls="mmg")
    return L2("mem-core","11.7","核心速记总表：核心一句 · 记忆钩 · 为何重要",x)
