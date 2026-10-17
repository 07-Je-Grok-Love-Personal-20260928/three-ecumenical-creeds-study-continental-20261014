# -*- coding: utf-8 -*-
"""原文库页面：信经全文（第七）、比利时信条（第八）、海德堡要理问答（第九）、多特信经（第十）。
正文全部由 data/*.json（逐字取自 ccifellowship.org《赞美手册》中文版）生成，不改写。"""
import json,re,html as H
from core import *
from c_titles import HC52
import creedlib as CL
def J(n): return json.load(open(f"data/{n}.json",encoding="utf-8"))
CCI="https://ccifellowship.org"
def fn(s): return re.sub(r"⟦(\d+)⟧",r'<sup class="fn">\1</sup>',H.escape(s,quote=False))
def src_link(url,label="CCI 原文页"): return f'<a class="srcl" href="{url}" target="_blank" rel="noopener">{label} ↗</a>'
def exact_note(extra=""):
    return f'<p class="exn"><b>原文说明：</b>下列正文<b>逐字取自</b>华人改革宗《赞美手册》（基督教华人网络团契 CCI）中文版；本站未改动一字，脚注上标 ¹²³ 与“经文参考”按原页面保留。每一小节附原文链接。{extra}</p>'
def chips(items):
    return '<nav class="chips" aria-label="快速跳转">'+"".join(f'<a href="#{i}" title="{t}">{l}</a>' for i,l,t in items)+'</nav>'
def refs_ol(lst):
    if not lst: return ""
    return "".join(f'<span class="rf1" role="listitem"><b class="nb">{i}</b>{H.escape(x)}</span>' for i,x in enumerate(lst,1))
def blocks_html(bl):
    out=""
    for b in bl:
        if b["t"]=="p": out+=f'<p class="ex">{fn(b["x"])}</p>'
        elif b["t"]=="ref": out+='<div class="refs2" role="list" aria-label="经文参考"><span class="fnh">📖 经文参考</span>'+refs_ol(b["x"])+'</div>'
        elif b["t"]=="h4": out+=f'<h4 class="qh">{H.escape(b["x"])}</h4>'
    return out

# ===== 七、信经全文与诵读 =====
def reader(id, num, title, zh, groups, src, sub):
    body=""
    for gt,c,a,b_ in groups:
        body += f'<div class="vg" style="--c:{c}"><div class="vgh">{gt}<small>第{a}–{b_}句</small></div><ol class="verses" start="{a}">'
        for k in range(a-1,b_):
            z=zh[k]; body += f'<li><span class="vn">{k+1}</span><span class="zh" data-cue="{H.escape(z[:1])}">{z}</span></li>'
        body += '</ol></div>'
    return L2(id, num, title, f'<div class="reader" data-reader><div class="rbar"><button class="btn" data-mode="all">全文</button><button class="btn ghost" data-mode="cue">提示首字</button><button class="btn ghost" data-mode="hide">隐藏全部</button><span class="rhint">点任一句可单独显示／遮盖</span></div>{body}</div><p class="src">{src}</p><p class="sub">{sub}</p>')

def part_creeds():
    C=J("creeds")
    b = L2("cr-intro","7.1","总览：三份信经与本页的用法",
      f'<p class="ex">{H.escape(C["index_intro"])}</p><p class="src">{src_link(C["index_url"],"CCI《赞美手册》普世信经总目 ccifellowship.org/books/book-of-praise/creeds")}</p>'
      + exact_note('上面这一段同为 CCI 原文。')
      + '<div class="grid g3">'
      + ''.join(f'<a class="pg" href="#{i}" style="--c:{c}"><b>{t}</b><small>{s}</small></a>' for i,t,s,c in [("cr-ap","使徒信经","12 条 · 3 段 · 西方 · 洗礼","#81b29a"),("cr-ni","尼西亚信经","13 节 · 4 段 · 东西共用","#e07a5f"),("cr-at","亚他那修信经","42 点 · 11 组（CCI 编号）","#5aa9e6")])
      + '</div>'
      + key('<b>每部信经两层：</b>①<b>背诵版</b>——按条（使徒信经 12 条）、按节（尼西亚 13 节）、按主题分组（亚他那修 11 组），一行一句，带编号、图标与背诵工具（全显／首字提示／全遮／逐行跟读）；②<b>CCI 整段原文</b>——每部信经最后一个小节，逐字收录。两层文字完全相同（tools/verify_recite.py 核对）。深度讲解见第二、三、四部分。')
      + note('三项联合信条的原文库见第八（比利时信条）、第九（海德堡要理问答）、第十（多特信经）部分。'))
    def block(key_,ztitle):
        d=C[key_]
        return f'<h4 class="qh">CCI 导言（原文）</h4><p class="ex">{H.escape(d["intro"])}</p><h4 class="qh">{H.escape(ztitle)}（原文）</h4>'+"".join(f'<p class="ex cr">{H.escape(p)}</p>' for p in d["paras"])+f'<p class="src">{src_link(d["url"])}</p>'
    def parted(parts,titles,texts,pref):
        x=CL.TOOL+'<div class="rc" data-recite>'
        for pn,pt,pico,nos in parts:
            x+=f'<h4 class="rpart">{ic(pico,"ic sm")}第{pn}段 · {pt}</h4>'
            for n in nos:
                t,ico,sub=titles[n]
                x+=L3(f"{pref}-a{n}",t,CL.art(n,CL.lines(texts[n])),ico,sub=sub,cls="ldc rcs")
        return x+'</div>'
    x=parted(CL.AP_PARTS,CL.AP_TITLES,CL.apostles(C),"ap")
    x+=L3("ap-txt","CCI 导言与原文整段（逐字）",block("apostles","使徒信经")+note("CCI 中文本把“降在阴间”接在“被埋葬”之后（见原文）。"),"scroll",cls="tx")
    b += L2("cr-ap","7.2","使徒信经 · 12 条 · 3 段（背诵版）",x)
    x=parted(CL.NI_PARTS,CL.NI_TITLES,CL.nicene(C),"ni")
    x+=L3("ni-txt","CCI 导言与原文整段（逐字）",block("nicene","尼西亚信经")+note("CCI 文本含“圣灵……从父和子而出”（西方文本，含 filioque）；CCI 导言自己说明东方教会至今不接受这一句。"),"scroll",cls="tx")
    b += L2("cr-ni","7.3","尼西亚信经 · 13 节 · 4 段（背诵版，对应 CCI 7 段）",x)
    at=CL.athanasian(C)
    x=CL.TOOL+'<div class="rc" data-recite>'
    for pn,pt,pico,gs in CL.AT_PARTS:
        x+=f'<h4 class="rpart">{ic(pico,"ic sm")}{pn} · {pt}</h4>'
        for g in gs:
            nm,lo,hi,gi=CL.AT_GROUPS[g]
            body="".join(CL.art(k,CL.lines(at[k])) for k in range(lo,hi+1))
            x+=L3(f"at-g{g}",f"第{lo}–{hi}点 · {nm}" if hi!=lo else f"第{lo}点 · {nm}",body,gi,sub=f"{hi-lo+1} 点",cls="ldc rcs")
    x+='</div>'
    x+=L3("at-txt","CCI 导言与原文整段（逐字）",block("athanasian","亚他那修信经")+hard("<b>编号差异（已核对）：</b>CCI 导言说“第二部分包括第29-43点”，但其正文编号只到第42点（第42点是“这是大公信仰……阿们”）。本站背诵版按 CCI 正文 42 点。URCNA（urcna.org/athanasian）的英文版分为 44 节；改革宗初学者网站（reformedbeginner.net）亦为 44 节——不同教会编号不同，文字内容相同，引用时请注明所用版本。"),"scroll",cls="tx")
    b += L2("cr-at","7.4","亚他那修信经 · 42 点 · 11 组（背诵版）",x)
    return L1("creeds","七","三大信经全文与背诵版","scroll","CCI《赞美手册》中文版原文逐字收录；背诵版一行一句，按条／节／主题分组。", b)

# ===== 八、比利时信条 =====
BCG=[("bc-g1","8.2","第1–7条：神与启示（本站分组）",1,7),("bc-g2","8.3","第8–11条：三位一体（本站分组）",8,11),("bc-g3","8.4","第12–15条：创造、护理、人与原罪（本站分组）",12,15),("bc-g4","8.5","第16–26条：拣选与基督的救赎（本站分组）",16,26),("bc-g5","8.6","第27–32条：教会（本站分组）",27,32),("bc-g6","8.7","第33–35条：圣礼（本站分组）",33,35),("bc-g7","8.8","第36–37条：政府与末日审判（本站分组）",36,37)]
def part_bc():
    D=J("bc")
    intro="".join(f'<p class="ex">{fn(p)}</p>' for p in D["intro"])
    b = L2("bc-intro","8.1","导言与说明（CCI 原文）", exact_note("第8–11条（三位一体）与第9条（接受三信经）是本站讲解的核心。")+intro+f'<p class="src">{src_link(D["url"],"CCI 比利时信条总页")}</p>'
        + chips([(f"bc-{a['n']}",str(a['n']),a['title']) for a in D["articles"]])
        + note("八个分节标题（神与启示、三位一体等）为本站为导航所加；CCI 页面本身只按条列出。"))
    for gid,num,gt,lo,hi in BCG:
        x=""
        for a in D["articles"][lo-1:hi]:
            x+=L3(f'bc-{a["n"]}',H.escape(a["title"]),blocks_html(a["blocks"])+f'<p class="src">{src_link(a["url"])}</p>',"scroll",cls="art tx")
        b += L2(gid,num,gt,x)
    return L1("bc","八","比利时信条全文（37条）","scroll","德布利（Guido de Brès）所著；CCI 中文版逐字收录。", b)

# ===== 九、海德堡 =====
def part_hc():
    D=J("hc")
    lds=D["lds"]
    # Q 范围
    rng={}
    for ld in lds:
        qs=[int(re.match(r"\s*(\d+)",b["x"]).group(1)) for b in ld["blocks"] if b["t"]=="h4"]
        rng[ld["n"]]=(qs[0],qs[-1])
    intro="".join(f'<p class="ex">{H.escape(p)}</p>' for p in D["intro"])
    b = L2("hc-intro","9.1","导言与结构（CCI 原文）",exact_note("共 52 个主日、129 问；使徒信经由主日7–22（问22–58）讲解。")+intro+f'<p class="src">{src_link(D["url"],"CCI 海德堡要理问答总页")}</p>'
        + chips([(f"ld{l['n']}",str(l['n']),f"主日{l['n']}：问{rng[l['n']][0]}–{rng[l['n']][1]}") for l in lds])
        + note('上方数字＝主日；悬停可见问号范围。每个主日下附 CCI“我属于”（I Belong）系列对应课程链接 ccifellowship.org/books/i-belong/N（该系列把几个主日合并的有主日26–27、28–30、36–37）。'))
    groups=[("hc-g1","9.2","第一部 论人的罪和愁苦（主日1–4）",1,4),("hc-g2","9.3","第二部 论我们的得救：中保、信心与信经（主日5–10）",5,10),
      ("hc-g3","9.4","子神和我们的得赎（主日11–19）",11,19),("hc-g4","9.5","圣灵神和我们的成圣（主日20–22）",20,22),("hc-g5","9.6","我们得称为义（主日23–24）",23,24),
      ("hc-g6","9.7","圣言与圣礼（主日25）",25,25),("hc-g7","9.8","圣洗礼（主日26–27）",26,27),("hc-g8","9.9","圣餐（主日28–31）",28,31),
      ("hc-g9","9.10","第三部 论感恩（主日32–33）",32,33),("hc-g10","9.11","十诫（主日34–44）",34,44),("hc-g11","9.12","祷告（主日45–52）",45,52)]
    def ibref(n):
        if n in (26,27): return "26-27"
        if n in (28,29,30): return "28-29-30"
        if n in (36,37): return "36-37"
        return str(n)
    for gid,num,gt,lo,hi in groups:
        x=""
        for ld in lds[lo-1:hi]:
            n=ld["n"]
            x+=L3(f'ld{n}',f"主日{n} · {HC52[n][0]}",blocks_html(ld["blocks"])+f'<p class="src">{src_link(ld["url"])} · {src_link(CCI+"/books/i-belong/"+ibref(n),"CCI《我属于》学习课程")}</p>',HC52[n][3],sub=f"问{rng[n][0]}–{rng[n][1]}",cls="art tx ld")
        b += L2(gid,num,gt,x)
    b += note("<b>分组说明：</b>“第一部/第二部/第三部”及“子神和我们的得赎”“圣灵神和我们的成圣”“我们得称为义”“圣言与圣礼”“圣洗礼”“圣餐”“十诫”“祷告”等标题均为 CCI 页面的目录名；“主日5–10”一组 CCI 未另立标题，本站按其内容（中保、信心、使徒信经、三一、创造与护理）命名。")
    return L1("hc","九","海德堡要理问答全文（129问）","scroll","乌尔西努与俄利维亚努（1563）；CCI 中文版逐字收录，含 52 主日。", b)

# ===== 十、多特 =====
def part_dort():
    D=J("dort")
    intro="".join(f'<p class="ex">{fn(p)}</p>' for p in D["intro"])
    chip=[]
    for h in D["heads"]:
        for it in h["items"]:
            lab=("驳"+h["num"] if it["title"]=="错谬反驳" else f'{h["num"]}.{it["n"]}')
            chip.append((f'dort-{h["id"]}-{it["n"]}',lab,it["title"]))
    b = L2("dt-intro","10.1","导言与结构（CCI 原文）",exact_note("多特信经分四项（第三、四项合一），共 63 个条目（含各项“错谬反驳”）。CCI 页面上未见序言或结语部分，本站不另补。")+intro+f'<p class="src">{src_link(D["url"],"CCI 多特信经总页")}</p>'+chips(chip))
    nums=["10.2","10.3","10.4","10.5"]
    for h,num in zip(D["heads"],nums):
        x=""
        for it in h["items"]:
            err = it["title"]=="错谬反驳"
            lab = "驳" if err else str(it["n"])
            x+=L3(f'dort-{h["id"]}-{it["n"]}',H.escape(it["title"]),blocks_html(it["blocks"])+f'<p class="src">{src_link(it["url"])}</p>',"alert" if err else "scroll",cls="art tx"+(" err" if err else ""))
        b += L2(f"dt-{h['id']}",num,h["title"]+f'（项{h["num"]}）',x+f'<p class="src">{src_link(h["url"],"CCI 本项总页")}</p>')
    return L1("dort","十","多特信经全文（四项教义）","scroll","1618–1619 多特大会；CCI 中文版逐字收录，含正反两面（教义与错谬反驳）。", b)
