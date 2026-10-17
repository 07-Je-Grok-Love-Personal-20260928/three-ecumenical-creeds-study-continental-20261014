# -*- coding: utf-8 -*-
"""共用构件：目录登记、L1/L2、卡片、表格、时间线、地图。"""
from content import *
from extra import *
import html as H
V = "v20261017-9"
CUR = {"f": None, "n": 0, "c2": 0}
PEND = []
PEND3 = []
TOC = []  # (l1id, l1title, [(id,title)])

def L1(id, num, title, ico, lead, body):
    TOC.append((id, f"{num}、{title}", PEND[:], CUR["f"])); PEND.clear()
    return f'<section class="l1" id="{id}"><header class="l1h reveal"><span class="ico">{ic(ico,"ic big")}</span><div><div class="kick">第{num}部分</div><h2>{num}、{title}</h2><p class="lead">{lead}</p></div></header>{body}</section>'
def L2(id, num, title, body):
    CUR["c2"] += 1; num = f'{CUR["n"]}.{CUR["c2"]}'
    kids = PEND3[:]; PEND3.clear()
    PEND.append((id, f"{num} {title}", kids))
    return f'<section class="l2 reveal" id="{id}"><h3><span class="n">{num}</span>{ic(l2icon(title))}{title}</h3>{body}</section>'
def L3(id, title, body, icon="cross", tag="", cls="", sub="", bar=None):
    """三级标题：编号 = 所属二级编号 + 序号（所属二级尚未登记，故用 c2+1）。返回 <section class=l3>。"""
    k = len(PEND3) + 1; num = f'{CUR["n"]}.{CUR["c2"]+1}.{k}'
    PEND3.append((id, f"{num} {title}"))
    t = f'<span class="l3t">{tag}</span>' if tag else ""
    s = f'<small class="l3s">{sub}</small>' if sub else ""
    return f'<section class="l3 reveal {cls}" id="{id}"><h4 class="l3h"><span class="n3">{num}</span>{ic(icon,"ic sm")}<span class="l3x">{title}</span>{s}{t}</h4>{body}</section>'
def key(t): return f'<div class="call key"><b>🔑 重点</b>{t}</div>'
def hard(t): return f'<div class="call hard"><b>⚠️ 难点</b>{t}</div>'
def note(t): return f'<div class="call note"><b>📌 说明</b>{t}</div>'
def app(t): return f'<div class="call app"><b>🌱 应用</b>{t}</div>'
def cards(items, cls="g3"):
    return f'<div class="grid {cls}">' + "".join(f'<div class="card" style="--c:{c}"><div class="ct"><span>{i}</span>{t}</div><p>{p}</p></div>' for i,t,p,c in items) + '</div>'
def table(head, rows, cls=""):
    if head and head[0]=="异端": rows=[[ic("alert","ic sm hz")+r[0]]+list(r[1:]) for r in rows]
    return f'<div class="tw"><table class="{cls}"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows) + "</tbody></table></div>"
def timeline(items):
    return '<ol class="tl reveal">' + "".join(f'<li class="reveal" style="--c:{c}"><div class="yr">{ic("church" if "会议" in t else "clock","ic sm")}{y}</div><div class="tb"><b>{t}</b><p>{p}</p></div></li>' for y,t,p,c in items) + "</ol>"
def story(items):
    return '<div class="story">' + "".join(f'<div class="st reveal"><div class="sn">{n+1}</div><b>{t}</b><p>{p}</p></div>' for n,(t,p) in enumerate(items)) + "</div>"
def flow(steps):
    return '<div class="flow">' + '<span class="arr">➜</span>'.join(f'<div class="fs" style="--c:{c}"><b>{t}</b><small>{s}</small></div>' for t,s,c in steps) + "</div>"
def exeg(rows):
    out = '<div class="exeg">'
    for ph, mean, scr, conf, k, h in rows:
        out += f'<details class="ex reveal"><summary><span class="q">“{ph}”</span></summary><div class="exb"><p><i>释义</i>{mean}</p><p><i>经文</i>{scr}</p><p><i>信条</i>{conf}</p>' + (f'<p class="k"><i>重点</i>{k}</p>' if k else "") + (f'<p class="h"><i>难点</i>{h}</p>' if h else "") + '</div></details>'
    return out + '</div><div class="exctl"><button class="btn" data-open=".exeg">全部展开</button><button class="btn ghost" data-close=".exeg">全部收起</button></div>'

# ---------- 地图 ----------
CITY = {"罗马":(12.5,41.9),"尼西亚":(29.7,40.4),"君士坦丁堡":(29.0,41.0),"亚历山大":(29.9,31.2),"安提阿":(36.2,36.2),
"阿尔勒":(4.6,43.7),"勒兰岛":(7.0,43.5),"托莱多":(-4.0,39.9),"以弗所":(27.3,37.9),"迦克墩":(29.6,40.6),"阿奎莱亚":(13.4,45.8),
"迦太基":(10.3,36.85),"老底嘉":(35.8,35.5),"耶路撒冷":(35.2,31.8),"里昂":(4.8,45.75),"米兰":(9.2,45.5),"希坡":(7.75,36.9),"该撒利亚(卡帕多家)":(35.5,38.7)}
def xy(n):
    lon,lat = CITY[n]; return (lon+10)*18+20, (48-lat)*24+20
OFF={'君士坦丁堡':(-12,-12,'end'),'尼西亚':(12,22,'start'),'迦克墩':(14,2,'start'),'老底嘉':(12,16,'start'),'安提阿':(12,-4,'start'),'勒兰岛':(10,20,'start'),'阿尔勒':(-12,-8,'end'),'里昂':(-12,4,'end')}
def mapsvg(id, title, pts, routes=(), hl=()):
    s = f'<figure class="map reveal"><svg viewBox="0 0 1040 470" role="img" aria-label="{title}"><defs><linearGradient id="g{id}" x1="0" x2="1"><stop offset="0" stop-color="#2a3f7a" stop-opacity=".55"/><stop offset=".53" stop-color="#2a3f7a" stop-opacity=".25"/><stop offset=".53" stop-color="#7a4e2a" stop-opacity=".25"/><stop offset="1" stop-color="#7a4e2a" stop-opacity=".5"/></linearGradient></defs>'
    s += f'<rect x="0" y="0" width="1040" height="470" rx="18" fill="url(#g{id})"/>'
    for gx in range(0,1040,90): s += f'<line x1="{gx}" y1="0" x2="{gx}" y2="470" class="gr"/>'
    for gy in range(0,470,72): s += f'<line x1="0" y1="{gy}" x2="1040" y2="{gy}" class="gr"/>'
    dx = (19+10)*18+20
    s += f'<line x1="{dx}" y1="10" x2="{dx}" y2="460" class="div"/><text x="{dx-12}" y="34" text-anchor="end" class="rg">拉丁西方 · Latin West</text><text x="{dx+12}" y="34" class="rg">希腊东方 · Greek East</text>'
    for a,b in routes:
        (x1,y1),(x2,y2) = xy(a),xy(b); mx,my=(x1+x2)/2,(y1+y2)/2-60
        s += f'<path d="M{x1:.0f},{y1:.0f} Q{mx:.0f},{my:.0f} {x2:.0f},{y2:.0f}" class="route"/>'
    for n in pts:
        x,y = xy(n); big = n in hl
        ox,oy,an=OFF.get(n,(12,5,'start')); s += f'<g class="pt{" hl" if big else ""}"><circle cx="{x:.0f}" cy="{y:.0f}" r="{9 if big else 5}"/><text x="{x+ox:.0f}" y="{y+oy:.0f}" text-anchor="{an}">{n}</text></g>'
    s += f'</svg><figcaption>{title}（示意图：按经纬度投影的城市位置，不绘海岸线；虚线≈395年东西罗马分治线，约在东经19°）</figcaption></figure>'
    return s
