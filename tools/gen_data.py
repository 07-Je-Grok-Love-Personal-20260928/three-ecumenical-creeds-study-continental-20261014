# -*- coding: utf-8 -*-
"""从本地 CCI 抓取缓存（cci.json）生成 data/*.json。正文逐字保留，不改写。
用法：python3 tools/gen_data.py /workspace/cci_crawl/cci.json"""
import json,re,sys
src=sys.argv[1] if len(sys.argv)>1 else "/workspace/cci_crawl/cci.json"
D=json.load(open(src))
BASE="https://ccifellowship.org"
def blk(bl): return [{"t":t,"x":x} for t,x in bl]
# 三信经
cr={}
for k,key in [("creed_apostles","apostles"),("creed_nicene","nicene"),("creed_athanasian","athanasian")]:
    d=D[k]; bl=d["blocks"]
    cr[key]={"title":d["title"],"url":BASE+d["url"],"intro":bl[0][1],"paras":[x for t,x in bl[1:]]}
cr["index_intro"]=D["creeds_index"]["blocks"][0][1]; cr["index_url"]=BASE+"/books/book-of-praise/creeds"
json.dump(cr,open("data/creeds.json","w"),ensure_ascii=False,indent=1)
# 比利时信条
bc={"url":BASE+"/books/book-of-praise/confessions/the-belgic-confession","intro":[x for t,x in D["bc_index"]["blocks"] if t=="p"],"articles":[]}
for n in range(1,38):
    d=D[f"bc_{n}"]; bc["articles"].append({"n":n,"title":d["title"],"url":BASE+d["url"],"blocks":blk(d["blocks"])})
json.dump(bc,open("data/bc.json","w"),ensure_ascii=False,indent=1)
# 海德堡
GROUPS={1:"第一部 论人的罪和愁苦",5:"第二部 论我们的得救",11:"子神和我们的得赎",20:"圣灵神和我们的成圣",23:"我们得称为义",25:"圣言与圣礼",26:"圣洗礼",28:"圣餐",32:"第三部 论感恩",34:"十诫",45:"祷告"}
hc={"url":BASE+"/books/book-of-praise/confessions/heidelberg-catechism","intro":[x for t,x in D["hc_idx"]["blocks"] if t=="p"],"lds":[]}
nq=0
for n in range(1,53):
    d=D[f"hc_{n}"]; bl=blk(d["blocks"]); nq+=sum(1 for b in bl if b["t"]=="h4")
    hc["lds"].append({"n":n,"title":d["title"],"url":BASE+d["url"],"group":GROUPS.get(n),"blocks":bl})
assert nq==129,nq
json.dump(hc,open("data/hc.json","w"),ensure_ascii=False,indent=1)
# 多特
heads=[("section1","1","第一项教义 论神的拣选与弃绝",19),("section2","2","第二项教义 论基督的死和人藉此而得的救赎",10),("section3-4","3-4","第三、四项教义 论人的败坏、向神归正及其方法",18),("section5","5","第五项教义 真信徒能持守信仰",16)]
dt={"url":BASE+"/books/book-of-praise/confessions/canons-of-dort","intro":[x for t,x in D["dort_idx"]["blocks"] if t=="p"],"heads":[]}
for sec,num,name,cnt in heads:
    items=[]
    for i in range(1,cnt+1):
        d=D[f"dort_{sec}_{i}"]; items.append({"n":i,"title":d["title"],"url":BASE+d["url"],"blocks":blk(d["blocks"])})
    dt["heads"].append({"id":sec,"num":num,"title":name,"url":BASE+"/books/book-of-praise/confessions/canons-of-dort/"+sec,"items":items})
json.dump(dt,open("data/dort.json","w"),ensure_ascii=False,indent=1)
print("ok", sum(len(h["items"]) for h in dt["heads"]))
