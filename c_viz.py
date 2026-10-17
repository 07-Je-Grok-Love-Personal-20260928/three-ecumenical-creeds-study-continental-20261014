# -*- coding: utf-8 -*-
"""可视化：计数器、柱状图、环形图、北美地图。所有数据在构建时由 data/*.json（CCI 原文）统计，不手填。"""
import html as H,re
from core import *
import json,re
import creedlib as CL
from quotes import BC,HC,DORT
from geo import mapsvg as gmap
PCOL={"总纲":"#d4af37","困苦":"#e07a5f","拯救":"#5aa9e6","感恩":"#81b29a"}
def stats(items):
    return '<div class="vst reveal">'+"".join(f'<div style="--c:{c}"><i>{i}</i><b data-count="{n}">{n}</b><small>{t}</small></div>' for i,n,t,c in items)+'</div>'
def colchart(id,title,items,note="",label_every=1,unit="",legend=None,H_=220):
    """items: (标签,数值,颜色,提示,链接,标记)。纵向柱；横向在窄屏滚动，不撑破页面。"""
    n=len(items); W=1040; pl,pr,pt,pb=40,8,16,36; bw=(W-pl-pr)/n; mx=max(v for _,v,*_ in items)
    s=f'<figure class="cchart reveal"><p class="shint">← 左右滑动看全部柱子 →</p><div class="cscroll"><svg viewBox="0 0 {W} {H_}" role="img" aria-label="{H.escape(title)}">'
    for k in (0,.5,1):
        y=H_-pb-k*(H_-pt-pb); s+=f'<line x1="{pl}" y1="{y:.0f}" x2="{W-pr}" y2="{y:.0f}" class="gr"/><text x="{pl-6}" y="{y+4:.0f}" text-anchor="end" class="ax">{round(mx*k)}</text>'
    for i,(lab,v,c,tip,href,mark) in enumerate(items):
        h=v/mx*(H_-pt-pb); x=pl+i*bw; y=H_-pb-h
        r=f'<g class="cb" style="--i:{i}"><rect x="{x+bw*.1:.1f}" y="{y:.1f}" width="{bw*.8:.1f}" height="{h:.1f}" rx="3" fill="{c}"><title>{H.escape(tip)}</title></rect>'
        if mark: r+=f'<circle cx="{x+bw/2:.1f}" cy="{y-7:.1f}" r="3.6" class="mk"/>'
        r+='</g>'
        s+=(f'<a href="{href}">{r}</a>' if href else r)
        if i%label_every==0 or i==n-1: s+=f'<text x="{x+bw/2:.1f}" y="{H_-pb+16}" text-anchor="middle" class="ax">{lab}</text>'
    s+='</svg></div>'
    lg="".join(f'<span class="lg2" style="--c:{c}"><i></i>{t}</span>' for t,c in (legend or []))
    return s+f'<figcaption><b>{title}</b>{"（"+unit+"）" if unit else ""}{note and "　"+note}{lg and "<br>"+lg}</figcaption></figure>'
def donut(id,title,parts,center,sub=""):
    """parts: (标签,数值,颜色,说明)。pathLength=100，逐段描边动画。"""
    tot=sum(v for _,v,_,_ in parts); off=0; seg=""; lg=""
    for lab,v,c,d in parts:
        p=v/tot*100
        seg+=f'<circle class="dseg" cx="60" cy="60" r="40" pathLength="100" stroke="{c}" stroke-dasharray="{p-0.8:.2f} {100-p+0.8:.2f}" stroke-dashoffset="{-off:.2f}" style="--da:{p-0.8:.2f} {100-p+0.8:.2f}"><title>{H.escape(lab)}：{v}（{p:.0f}%）</title></circle>'
        lg+=f'<li style="--c:{c}"><i></i><b>{lab}</b><span>{v}　{d}</span></li>'; off+=p
    return (f'<figure class="donutw reveal"><svg viewBox="0 0 120 120" role="img" aria-label="{H.escape(title)}"><g transform="rotate(-90 60 60)">{seg}</g>'
            f'<text x="60" y="58" text-anchor="middle" class="dc1">{center}</text><text x="60" y="74" text-anchor="middle" class="dc2">{sub}</text></svg>'
            f'<figcaption><b>{title}</b><ul class="dleg">{lg}</ul></figcaption></figure>')

C_=json.load(open("data/creeds.json",encoding="utf-8"))
def _n(s): return len(re.sub(r"\s|\d+\)","",s))
PC4=["#81b29a","#e07a5f","#5aa9e6","#d4af37","#b794f4"]
def _viz(id,title,intro,stat,items,legend,donut_parts,dcenter,dsub,tail,unit="字",le=1):
    return L2(id,"?",title,'<p>'+intro+'</p>'+stat+colchart(id+"c",title.split("：")[-1]+"的篇幅",items,legend=legend,unit=unit,label_every=le)+donut(id+"d","分段占比",donut_parts,dcenter,dsub)+tail)
def viz_ap():
    T=CL.apostles(C_); items=[]; parts=[]; leg=[]
    for i,(pn,pt,pico,nos) in enumerate(CL.AP_PARTS):
        c=PC4[i]; leg.append((f"第{pn}段 {pt}",c)); parts.append((f"第{pn}段 {pt}",len(nos),c,f"{len(nos)} 条"))
        for n in nos: items.append((str(n),_n(T[n]),c,f"第{n}条 · {CL.AP_TITLES[n][0]}：{_n(T[n])} 字",f"#apx-{n}",False))
    return _viz("ap-viz","数据图：使徒信经 12 条的篇幅与三段","字数由 CCI 中文本逐条统计（不含编号）。三段＝父（1）、子（2–7）、灵与教会末事（8–12）。",
      stats([("📜",12,"条","#81b29a"),("🧭",3,"段（父·子·灵）","#d4af37"),("📏",sum(_n(T[n]) for n in T),"字（全文）","#5aa9e6"),("✝️",6,"条讲圣子","#e07a5f")]),
      items,leg,parts,"12","条",key("<b>读图：</b>第二段（圣子）占 6 条、一半——使徒信经是一部“基督的叙事”；父与灵各自简短。记忆：<b>1 · 6 · 5</b>。"))
def viz_ni():
    T=CL.nicene(C_); items=[]; parts=[]; leg=[]
    for i,(pn,pt,pico,nos) in enumerate(CL.NI_PARTS):
        c=PC4[i]; leg.append((f"第{pn}段 {pt}",c)); parts.append((f"第{pn}段 {pt}",len(nos),c,f"{len(nos)} 节"))
        for n in nos: items.append((str(n),_n(T[n]),c,f"第{n}节 · {CL.NI_TITLES[n][0]}：{_n(T[n])} 字",f"#nix-{n}",n in (4,)))
    return _viz("ni-viz","数据图：尼西亚信经 13 节的篇幅与四段","金色圆点＝第 4 节（“与父同质”所在，即会议的焦点）。字数为 CCI 中文本。",
      stats([("🔥",13,"节","#e07a5f"),("🧭",4,"段（父·子·灵·教会）","#d4af37"),("📏",sum(_n(T[n]) for n in T),"字（全文）","#5aa9e6"),("⚖️",7,"节讲圣子","#81b29a")]),
      items,leg,parts,"13","节",key("<b>读图：</b>圣子一段占 7 节、过半（父与灵合共 3 节）——会议要防守的正是基督的神性；第 4 节只有 22 字，却是整场会议的焦点。"))
def viz_at():
    T=CL.athanasian(C_); items=[]; parts=[]; leg=[]
    colg={}
    for i,(pn,pt,pico,gs) in enumerate(CL.AT_PARTS):
        c=PC4[i]; leg.append((f"{pn} · {pt}",c)); parts.append((f"{pn} · {pt}",sum(CL.AT_GROUPS[g][2]-CL.AT_GROUPS[g][1]+1 for g in gs),c,"点"))
        for g in gs: colg[g]=c
    for g,(nm,lo,hi,gi) in CL.AT_GROUPS.items():
        for k in range(lo,hi+1): items.append((str(k),_n(T[k]),colg[g],f"第{k}点 · {nm}：{_n(T[k])} 字",f"#atx-{g}",False))
    return _viz("at-viz","数据图：亚他那修信经 42 点的篇幅与两大部分","42 点按本站的 11 组着色；第 3–28 点论三位一体，第 29–41 点论基督。编号以 CCI 为准（其他网站编到 43 或 44，见参考站互证）。",
      stats([("🛡️",42,"点（CCI 编号）","#5aa9e6"),("🧩",11,"组","#d4af37"),("📏",sum(_n(T[k]) for k in T),"字（全文）","#81b29a"),("🔢",44,"点：URCNA 与恩约教会页","#e07a5f")]),
      items,leg,parts,"42","点",key("<b>读图：</b>三位一体占 26 点（第 3–28），基督论 13 点；条目短而对仗，适合“一行一句”背诵。"),le=3)
def viz_overview():
    hcn=sum(len(HC[q][0])+len(HC[q][1]) for q in HC); bcn=sum(len(BC[n]) for n in BC); dn=sum(len(v) for v in DORT.values())
    cn={k:_n("".join(C_[k]["paras"])) for k in ("apostles","nicene","athanasian")}
    rows=[("使徒信经（12 条）",cn["apostles"],"#81b29a"),("尼西亚信经（13 节）",cn["nicene"],"#e07a5f"),("亚他那修信经（42 点）",cn["athanasian"],"#5aa9e6"),("比利时信条（37 条）",bcn,"#9ad1ff"),("海德堡要理问答（129 问）",hcn,"#a9d6bf"),("多特信经（含驳谬）",dn,"#d4af37")]
    mx=max(v for _,v,_ in rows)
    bh='<div class="lbars reveal" role="img" aria-label="六份文件字数对比">'+"".join(f'<div class="lbr" style="--c:{c};--w:{v/mx*100:.1f}%"><span class="lbn">{l}</span><span class="lbt"><i></i></span><b>{v} 字</b></div>' for l,v,c in rows)+'</div><p class="cn">字数＝CCI 中文本正文（不含脚注），由程序统计。</p>'
    pts=["阿纳海姆（洛杉矶）","费城","大急流城","汉密尔顿（安大略）","莱斯布里奇","林伍德（伊利诺伊）"]
    m=gmap("na","今天用这些信经与信条的机构：本站在参考页上读到的 6 个地点",pts,hl=("阿纳海姆（洛杉矶）","汉密尔顿（安大略）"),bbox=(-124,-68,28,54),rhine=False,
      off={"阿纳海姆（洛杉矶）":(14,6,'start'),"费城":(-14,18,'end'),"大急流城":(-14,-8,'end'),"汉密尔顿（安大略）":(14,-10,'start'),"莱斯布里奇":(14,6,'start'),"林伍德（伊利诺伊）":(-14,22,'end')},
      cap="。地点与出处：阿纳海姆＝恩约教会（ccreformed.org 页脚）；汉密尔顿＝加拿大归正教会神学院 1969 年开学（canadianreformedseminary.ca）；莱斯布里奇＝加拿大归正教会第一个教会 1950 年（canrc.org）；林伍德＝URCNA 1996 年首届总会（urcna.org）；大急流城＝Heritage Reformed 的神学院所在（heritagereformed.com）；费城＝威斯敏斯特神学院 1929 年创立（wts.edu）")
    return L2("cp-viz","?","数据图与地图：六份文件的篇幅，与今天谁在用",'<p>三份古代信经极短，三项联合信条长得多——这正是“先背信经、再读信条”的顺序。</p>'
      +stats([("📜",3,"份古代信经","#81b29a"),("📘",3,"份联合信条","#d4af37"),("🔗",3,"份信经被 BC 第 9 条接受","#e07a5f"),("🗺️",6,"个读到的地点","#5aa9e6")])+bh+m
      +note("地图只标本站在参考页文字里<b>真实读到</b>的地点；北美以外的教会此处不绘。"))
