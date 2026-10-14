# -*- coding: utf-8 -*-
P = {
"book":'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/><path d="M9 7h6"/>',
"dove":'<path d="M3 13c4 0 6-3 7-7 2 3 5 4 9 4-1 5-5 9-11 9H5l2-3"/><circle cx="16" cy="8" r=".8"/>',
"flame":'<path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-4 3-6 1 2 2 3 3 3 0-3-1-5 0-8z"/>',
"shield":'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
"scale":'<path d="M12 3v18M6 21h12M4 7h16"/><path d="M6 7l-3 6a3 3 0 0 0 6 0zM18 7l-3 6a3 3 0 0 0 6 0z"/>',
"scroll":'<path d="M7 4h11a2 2 0 0 1 2 2v1h-4"/><path d="M16 7v11a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-1h10"/><path d="M8 9h5M8 13h5"/>',
"brain":'<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 3 5 3 3 0 0 0 5 1V5a3 3 0 0 0-3-1zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-3 5 3 3 0 0 1-5 1"/>',
"library":'<path d="M4 4h4v16H4zM10 4h4v16h-4z"/><path d="M16 5l3.5-1 3 15-3.5 1z"/>',
"clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
"map":'<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
"alert":'<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.5"/>',
"key":'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
"leaf":'<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>',
"users":'<circle cx="9" cy="8" r="3"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c3 0 5 2 5 5"/>',
"church":'<path d="M12 2v4M10 4h4"/><path d="M6 21V11l6-5 6 5v10z"/><path d="M10 21v-5h4v5"/>',
"cross":'<path d="M12 3v18M7 8h10"/>',
"link":'<path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/>',
"heart":'<path d="M12 20s-8-5-8-11a4 4 0 0 1 8-2 4 4 0 0 1 8 2c0 6-8 11-8 11z"/>',
"quill":'<path d="M20 4c-8 0-13 6-14 14l-2 2"/><path d="M8 14h6"/>',
"tri":'<path d="M12 3l9 16H3z"/><circle cx="12" cy="13" r="2"/>',
}
def ic(n, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{P[n]}</svg>'
def l2icon(title):
    for k,v in [("时间线","clock"),("故事","scroll"),("地理","map"),("异端","alert"),("为什么","key"),("解读","book"),("信条","scale"),("应用","leaf"),("人物","users"),("误解","alert"),("牧养","heart"),("词义","quill"),("三一","tri"),("改革者","church"),("对照","scale"),("圣约","link"),("三约","link"),("礼仪","church"),("诵读","scroll"),("信经","scroll"),("口诀","brain"),("导图","brain"),("翻卡","brain"),("自测","key"),("总结","book")]:
        if k in title: return v
    return "cross"

def people(items):
    return '<div class="people">' + "".join(f'<div class="pp reveal" style="--c:{c}"><div class="pa">{n[0]}</div><div><b>{n}</b><small>{d}</small><p>{t}</p></div></div>' for n,d,t,c in items) + '</div>'
def myths(items):
    return '<div class="myths">' + "".join(f'<div class="my reveal"><p class="mx">✗ {m}</p><p class="mo">✓ {r}</p></div>' for m,r in items) + '</div>'

TRINITY = '''<figure class="trid reveal"><svg viewBox="0 0 420 380" role="img" aria-label="三一图：父、子、圣灵各是神，彼此不是对方">
<g class="edges"><path d="M210 40 L60 300" /><path d="M210 40 L360 300"/><path d="M60 300 L360 300"/></g>
<g class="spokes"><path d="M210 40 L210 205"/><path d="M60 300 L210 205"/><path d="M360 300 L210 205"/></g>
<text x="118" y="160" class="lb no" transform="rotate(-60 118 160)">不是</text><text x="302" y="160" class="lb no" transform="rotate(60 302 160)">不是</text><text x="210" y="322" class="lb no">不是</text>
<text x="222" y="125" class="lb yes">是</text><text x="128" y="262" class="lb yes">是</text><text x="284" y="262" class="lb yes">是</text>
<g class="nd f"><circle cx="210" cy="40" r="30"/><text x="210" y="47">父</text></g>
<g class="nd s"><circle cx="60" cy="300" r="30"/><text x="60" y="307">子</text></g>
<g class="nd g"><circle cx="360" cy="300" r="30"/><text x="360" y="307">灵</text></g>
<g class="nd c"><circle cx="210" cy="205" r="36"/><text x="210" y="213">神</text></g></svg>
<figcaption>三一图（传统“信仰之盾”的结构）：中心“神”与每一位格之间是“是”（各是神）；位格彼此之间是“不是”（不混淆）。中心只有一个（不分割本质）。对应亚他那修信经第3–6、15–16句。</figcaption></figure>'''

AP_WORDS = [["Credo in Deum","我信（入）上帝","in＋宾格：信靠、投靠；对教会只说 credo ecclesiam（信有），不用 in（鲁菲努已注意此区分，约）"],
 ["unicum Filium","独生子","对应约1:14、18 monogenēs：独一无二的儿子，本性之子"],
 ["conceptus de Spiritu Sancto","因圣灵感孕","受孕的主动者是圣灵；不是圣灵作“父亲”，而是创造性的能力（路1:35）"],
 ["passus sub Pontio Pilato","在彼拉多手下受难","sub＝在……任内：历史日期标记"],
 ["descendit ad inferos（inferna）","降在阴间","textus receptus 用 inferos；鲁菲努所载阿奎莱亚本作 inferna（约）"],
 ["sanctam ecclesiam catholicam","圣而公之教会","catholica＝“按整体的”，普世、完整"],
 ["sanctorum communionem","圣徒相通","sanctorum 可作阳性（圣徒）或中性（圣物/圣礼）；改革宗（海德堡问55）取“与基督及彼此相交”"],
 ["carnis resurrectionem","身体（肉身）复活","拉丁原文是 caro（肉身），强调就是这身体复活，非抽象灵体"]]
NI_WORDS = [["pisteuomen","我们信","会议的集体认信；西方礼仪后改单数 credo（约）"],
 ["monogenē","独生","约1:14、18；3:16"],
 ["gennēthenta pro pantōn tōn aiōnōn","在万世以前受生","永恒受生（eternal generation），否认“曾有一时他不存在”"],
 ["homoousion tō Patri","与父同质","ousia＝本质；与 homoiousios（类质）只差一个 i"],
 ["sarkōthenta … enanthrōpēsanta","成肉身……成为人","两个动词：取肉身＋成为完全的人（对阿波利拿里）"],
 ["to Kyrion, to zōopoion","主，赐生命的","Kyrios 是七十士译本译“耶和华”的词；zōopoios 见约6:63、林后3:6"],
 ["ek tou Patros ekporeuomenon","从父而出","直接取自约15:26；西方拉丁加 Filioque"],
 ["katholikēn kai apostolikēn","公与使徒的","大公：普世完整；使徒：建立在使徒根基上（弗2:20）"]]
