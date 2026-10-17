# -*- coding: utf-8 -*-
"""5.13 数据对比：字数条与关键内容矩阵（均由程序对 CCI 原文统计）。"""
import json,re
from core import *
C=json.load(open("data/creeds.json",encoding="utf-8"))
TXT={k:"".join(C[k]["paras"]) for k in("apostles","nicene","athanasian")}
def n(s): return len(re.sub(r"\s|\d+\)","",s))
CN={k:n(v) for k,v in TXT.items()}
CCOL={"apostles":"#81b29a","nicene":"#e07a5f","athanasian":"#5aa9e6"}
CNAME={"apostles":"使徒信经","nicene":"尼西亚信经","athanasian":"亚他那修信经"}
def bars():
    mx=max(CN.values())
    return '<div class="lbars reveal" role="img" aria-label="三份信经按 CCI 中文原文字数的长度对比">'+"".join(
      f'<div class="lbr" style="--c:{CCOL[k]};--w:{CN[k]/mx*100:.1f}%"><span class="lbn">{CNAME[k]}</span><span class="lbt"><i></i></span><b>{CN[k]} 字</b><small>{u}</small></div>'
      for k,u in (("apostles","12 条"),("nicene","13 节"),("athanasian","42 点")))+'</div><p class="cn">字数＝CCI 中文原文去掉空白与编号后的字符数（含标点），由程序统计。</p>'
TERMS=[("创造天地／造物主","创造天地"),("道成肉身（降世为人）","降世为人|道成肉身"),("童贞女所生","童贞女|童女"),("彼拉多手下","彼拉多"),("降在阴间","降在阴间"),("第三天复活","第三天"),
 ("坐在父右边","右边"),("审判活人死人","审判活人死人"),("与父同质","同质"),("圣灵从父和子而出","从父和子而出"),("圣而公之教会","圣而公之"),("罪得赦免","罪得赦免"),("洗礼","洗礼"),
 ("身体复活","身体复活|从死里复活"),("永生","永生"),("三位一体","三位一体"),("神人二性","神性"),("永远沉沦／永火的警告","永远沉沦|永火")]
def matrix():
    rows=[[lab]+["<span class='mky'>✓</span>" if re.search(rx,TXT[k]) else "<span class='mkn'>—</span>" for k in TXT] for lab,rx in TERMS]
    return table(["关键内容（程序在 CCI 原文中搜索）","使徒信经","尼西亚信经","亚他那修信经"],rows,"cmp mx")
def l2():
    return L2("cmp-data","5.13","数据对比：长度与关键内容矩阵",
      '<p>下面两个图都不是估计，而是<b>程序直接对 CCI 中文原文统计</b>的结果（见 <code>c_data.py</code>）：左边看篇幅，下面看哪些关键内容出现在哪一份里。</p>'
      +bars()+matrix()
      +key("读法：<b>使徒信经</b>篇幅最短、没有“三位一体”“同质”这类术语，却有最完整的救恩叙事；<b>尼西亚</b>补上“同质”“受生非被造”和圣灵的神性；<b>亚他那修</b>最长，术语最密，并且是唯一带有“必永远沉沦”警告的。")
      +hard("“✓／—”只表示 CCI 中文原文是否出现相应字词。例如“道成肉身”概念在使徒信经中以“因圣灵感孕，从童贞女马利亚所生”表达，并不以这几个字出现，故矩阵中看到“—”不等于信经没有这一教义。"))
