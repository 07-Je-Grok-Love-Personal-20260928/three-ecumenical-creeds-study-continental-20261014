(function(){var d=document,b=d.body,rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(!rm&&'IntersectionObserver'in window){d.documentElement.classList.add('js');var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px'});d.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});setTimeout(function(){d.querySelectorAll('.reveal').forEach(function(el){if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')})},50)}
var wide=function(){return innerWidth>=1100};
function tog(){if(wide())b.classList.toggle('tochide');else b.classList.toggle('tocopen')}
d.getElementById('tocbtn').onclick=tog;d.getElementById('tocx').onclick=tog;
d.querySelectorAll('#toc a').forEach(function(a){a.addEventListener('click',function(){if(!wide())b.classList.remove('tocopen')})});
d.querySelectorAll('.tg').forEach(function(t){t.onclick=function(){var li=t.closest('.t1');li.classList.toggle('closed');t.setAttribute('aria-expanded',!li.classList.contains('closed'))}});
var links={};d.querySelectorAll('#toc a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a});
var secs=[].slice.call(d.querySelectorAll('section[id]'));var cur=null;
var pend=[].slice.call(d.querySelectorAll('.reveal'));function sweep(){if(!pend.length)return;pend=pend.filter(function(el){if(el.classList.contains('in'))return false;if(el.getBoundingClientRect().top<innerHeight){el.classList.add('in');return false}return true})}
function spy(){sweep();var y=innerHeight*0.25,act=null;for(var i=0;i<secs.length;i++){if(secs[i].getBoundingClientRect().top<y)act=secs[i];}
var id=act&&act.id;if(act&&act.classList.contains('l1')){var f=act.querySelector('.l2');if(f&&f.getBoundingClientRect().top<y)id=f.id}
if(id!==cur){d.querySelectorAll('#toc a.on').forEach(function(a){a.classList.remove('on')});var a=links[id];if(a){a.classList.add('on');var l1=a.closest('.t1');if(l1){l1.classList.remove('closed');}if(wide()&&!b.classList.contains('tochide')){var t=d.getElementById('toc'),r=a.getBoundingClientRect();if(r.top<60||r.bottom>innerHeight-40)t.scrollTop+=r.top-innerHeight/2}}cur=id}
var h=d.documentElement;d.getElementById('prog').style.width=(h.scrollTop/(h.scrollHeight-innerHeight)*100)+'%'}
var cs=d.querySelectorAll('[data-count]');if(!rm&&cs.length){cs.forEach(function(c){var n=+c.dataset.count,t0=null;c.textContent='0';function st(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1400);c.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(st);else c.textContent=n}requestAnimationFrame(st);setTimeout(function(){c.textContent=n},2500)})}
var tk=0;addEventListener('scroll',function(){if(!tk){tk=1;requestAnimationFrame(function(){spy();tk=0})}},{passive:true});spy();
d.querySelectorAll('[data-open]').forEach(function(x){x.onclick=function(){x.parentNode.previousElementSibling.querySelectorAll('details').forEach(function(e){e.open=true})}});
d.querySelectorAll('[data-close]').forEach(function(x){x.onclick=function(){x.parentNode.previousElementSibling.querySelectorAll('details').forEach(function(e){e.open=false})}});
d.querySelectorAll('[data-reader]').forEach(function(r){var zs=r.querySelectorAll('.zh');
r.querySelectorAll('[data-mode]').forEach(function(btn){btn.onclick=function(){var m=btn.dataset.mode;if(m==='en'){r.classList.toggle('noen');return}
r.querySelectorAll('[data-mode]').forEach(function(o){if(o.dataset.mode!=='en')o.classList.toggle('ghost',o!==btn)});
zs.forEach(function(z){z.classList.remove('masked','cue');if(m==='hide')z.classList.add('masked');if(m==='cue')z.classList.add('cue')})}});
r.querySelectorAll('.verses li').forEach(function(li){li.onclick=function(){var z=li.querySelector('.zh');if(z.classList.contains('masked')||z.classList.contains('cue'))z.classList.remove('masked','cue');else z.classList.add('masked')}})});
var fc=d.getElementById('fc'),seen=new Set();d.querySelectorAll('.flip').forEach(function(f,i){f.onclick=function(){f.classList.toggle('on');f.setAttribute('aria-pressed',f.classList.contains('on'));seen.add(i);fc.textContent=seen.size}});
var qs=d.getElementById('qs');function score(){qs.textContent=d.querySelectorAll('.opt.ok.picked').length}
d.querySelectorAll('.qq').forEach(function(q){var a=+q.dataset.ans;q.querySelectorAll('.opt').forEach(function(o){o.onclick=function(){if(q.dataset.done)return;q.dataset.done=1;var i=+o.dataset.i;o.classList.add('picked',i===a?'ok':'no');q.querySelectorAll('.opt')[a].classList.add('ok');score()}})});
d.getElementById('qreset').onclick=function(){d.querySelectorAll('.qq').forEach(function(q){delete q.dataset.done;q.querySelectorAll('.opt').forEach(function(o){o.classList.remove('ok','no','picked')})});score()};
})();
