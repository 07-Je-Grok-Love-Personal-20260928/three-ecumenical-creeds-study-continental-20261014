# 三大公教会信经 · 欧陆改革宗深读（v20261014-4）

使徒信经、尼西亚信经、亚他那修信经，以及三项联合信条（比利时信条、海德堡要理问答、多特信经）的中文综合学习网站（欧陆改革宗视角）。

## 在线访问（3 个部署）
- GitHub Pages：https://07-je-grok-love-personal-20260928.github.io/three-ecumenical-creeds-study-continental-20261014/
- Netlify：https://three-ecumenical-creeds-study-continental-20261014.netlify.app/
- Surge：https://three-ecumenical-creeds-study-continental-20261014.surge.sh/
- 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-20261014

## 页面（13 页，共用可隐藏目录与统一编号）
| 页面 | 内容 |
|---|---|
| `index.html` | 首页：十二站学习路径、进度环（localStorage）、视觉工具总览 |
| `bible.html` 一 | 全本圣经视角：四幕救恩史、三约、三一、基督论 |
| `apostles.html` 二 | 使徒信经深读（时间线、地图、逐句、CCI《我属于》主日7–22对照等） |
| `nicene.html` 三 | 尼西亚信经深读（含与改革宗初学者译本对照） |
| `athanasian.html` 四 | 亚他那修信经深读（42点；编号与译本对照；URCNA 脚注） |
| `compare.html` 五 | 比较：异同表、三圈重叠图、分层揭示、信条交叉引用图、各教会陈述 |
| `westminster.html` 六 | 与威斯敏斯特标准的次要对照（WCF 1.10、2、8、31；WLC 9–11…；WSC 6、21…） |
| `creeds.html` 七 | 三信经全文（CCI 逐字）与诵读工具 |
| `bc.html` 八 | 比利时信条全文（37条，CCI 逐字） |
| `hc.html` 九 | 海德堡要理问答全文（129问，52主日，CCI 逐字） |
| `dort.html` 十 | 多特信经全文（63项，CCI 逐字） |
| `memory.html` 十一 | 口诀、思维导图、翻卡、自测 |
| `sources.html` 十二 | 来源与说明：逐字收录 / 转述 / CCI 上没有找到的内容 |

## 文本来源与原则
- 三信经与三项联合信条的中文正文**逐字取自**华人改革宗《赞美手册》（基督教华人网络团契，CCI，https://ccifellowship.org/books/book-of-praise），每条均附原页链接；数据在 `data/*.json`，由 `tools/gen_data.py` 从抓取页面生成，`tools/verify_exact.py` 核对页面与数据一致。
- CCI 的《我属于》、仪文、签署书、《烛台宣言》、《真理的火焰》等其他内容只做转述与短引，并注明出处。
- 其他改革宗网站（ccreformed.org、reformedbeginner.net、canrc.org、urcna.org、heritagereformed.com、prca.org、opc.org、canadianreformedseminary.ca、wts.edu、crts.edu）只转述实际读到的页面内容；PRCA 因站点验证页仅取搜索摘录。
- 不确定处标“约”。以圣经为最高权威。

## 开发
```
python3 build.py            # 生成全部 *.html（需要 Python 3）
python3 tools/check_links.py   # 站内链接/锚点/目录检查
python3 tools/verify_exact.py  # 原文一致性检查
python3 tools/audit_all.py more.py   # 引文核对（需本地爬取缓存）
```
静态站，无需构建；无 JavaScript 时内容全部可见；遵守 `prefers-reduced-motion`。
