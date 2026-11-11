/* My impact section for the case pages. Spec: impact-modal.md. Each page gives its contributions in
   <script type="application/json" id="impact-data">{"after":"#solution","slides":[["Title","Text"],...]}</script>
   and loads this file after it. The section goes right after the story block that holds "after".
   Colours of the buttons come from the page's own To the top buttons. */
(function(){
  var dataEl=document.getElementById('impact-data');if(!dataEl)return;
  var DATA;try{DATA=JSON.parse(dataEl.textContent)}catch(e){return}
  var SL=DATA.slides||[];if(!SL.length)return;
  var anchor=document.querySelector(DATA.after||'#solution');if(!anchor)return;
  var host=anchor.closest('.wrap')||anchor.closest('.pair')||anchor;
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var phoneQ=matchMedia('(max-width:720px)');

  /* colours: desktop from the dock's To the top, phones from the floating one */
  function colours(sel,fb){var el=document.querySelector(sel);if(!el)return fb;var c=getComputedStyle(el);return [c.backgroundColor,c.color]}
  var dk=colours('.dock a.totop',['#0E0E0E','#FFFFFF']);
  var mt=document.querySelector('.mtop'),mc=['#0E0E0E','#FFFFFF'];
  if(mt){var d0=mt.style.display;mt.style.display='flex';mc=colours('.mtop',mc);mt.style.display=d0}

  var OB='<svg class="imob" viewBox="3.6 19.6 93.8 60.8" aria-hidden="true"><path fill-rule="evenodd" d="M4,50A30,30 0 0 1 64,50V80H34A30,30 0 0 1 4,50ZM44,50A10,10 0 1 0 24,50A10,10 0 1 0 44,50Z"/><path d="M72,20H82A15,15 0 0 1 82,50A15,15 0 0 1 82,80H72Z"/></svg>';
  var X='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  var MENU='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  var UP='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>';

  var css=''+
  '.imsec{padding-top:clamp(24px,4vw,56px);padding-bottom:clamp(72px,10vw,140px)}'+
  '.imsec .vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}'+
  '.imsec h2.imw{margin:0 0 clamp(40px,5vw,72px);outline:none;scroll-margin-top:80px}'+
  '.imsec .iml{display:block;position:relative;width:100%}.imsec .iml svg{position:absolute;display:block}.imsec .iml path{fill:#0E0E0E;fill-rule:evenodd}'+
  '.impart{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:var(--cg,24px);row-gap:clamp(32px,4vw,56px)}'+
  '.impart li{display:flex;flex-direction:column;gap:10px;min-width:0}'+
  '.impart .n{font-size:15px;color:var(--muted,#6B6B6B);font-variant-numeric:tabular-nums}'+
  '.impart h3{margin:0;font-size:clamp(22px,2.2vw,28px);font-weight:500;letter-spacing:-.02em;line-height:1.15;text-wrap:balance}'+
  '.impart p{margin:0;color:var(--muted,#6B6B6B);font-size:16px;line-height:1.5;max-width:36ch}'+
  '@media (min-width:901px){.impart{column-gap:48px}}'+
  '@media (max-width:900px){.impart{grid-template-columns:repeat(2,minmax(0,1fr))}}'+
  /* phones: the contributions one under another (her call 2026-11-11: no slider) */
  '@media (max-width:720px){.impart{grid-template-columns:1fr}.impart .hb{display:none}}'+
  /* wider screens: every title on two lines, so the texts below start level (her call 2026-11-11) */
  '@media (min-width:721px){.impart h3{min-height:2.3em}}'+
  /* desktop: the OB button left of the dock */
  '.dock .imb{flex:none;height:58px;border-radius:999px;border:0;padding:0 14px;cursor:pointer;display:flex;align-items:center;background:var(--imc);color:var(--imo);font-family:inherit;font-size:14px;font-weight:600;line-height:1;white-space:nowrap;box-shadow:0 12px 32px -10px rgba(0,0,0,.45);transition:padding .3s cubic-bezier(.22,.61,.36,1),filter .2s}'+
  '.dock .imb span{max-width:0;opacity:0;margin-left:0;overflow:hidden;transition:max-width .3s cubic-bezier(.22,.61,.36,1),opacity .2s,margin .3s cubic-bezier(.22,.61,.36,1)}'+
  '.dock .imb:hover,.dock .imb:focus-visible{padding:0 20px 0 16px}.dock .imb:hover span,.dock .imb:focus-visible span{max-width:140px;opacity:1;margin-left:10px}'+
  '.dock .imb:hover,.dock .imb:focus-visible{filter:brightness(1.06)}.dock .imb .imob{flex:none;width:30px;height:20px;fill:currentColor}'+
  /* phones: one menu button in place of To the top */
  'html.has-im .mtop{display:none!important}'+
  '.imfab{display:none}'+
  '@media (max-width:900px){.imfab{position:fixed;left:50%;bottom:calc(16px + env(safe-area-inset-bottom));z-index:60;display:flex;flex-direction:column;align-items:center;gap:10px;transform:translate(-50%,calc(100% + 40px));opacity:0;pointer-events:none;transition:transform .45s cubic-bezier(.22,.61,.36,1),opacity .3s}'+
  '.imfab.show{transform:translate(-50%,0);opacity:1;pointer-events:auto}'+
  '.imfab .imm{width:52px;height:52px;border-radius:50%;border:0;padding:0;cursor:pointer;background:var(--imc);color:var(--imo);box-shadow:0 10px 28px -8px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center}'+
  '.imfab .imm svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}'+
  '.imfab .impills{display:flex;flex-direction:column;align-items:center;gap:8px}.imfab .impills[hidden]{display:none}'+
  '.imfab .impill{display:flex;align-items:center;gap:10px;height:48px;padding:0 20px 0 16px;border-radius:999px;border:0;cursor:pointer;background:var(--imc);color:var(--imo);font-family:"Inter Tight",system-ui,sans-serif;font-size:15px;font-weight:600;line-height:1;text-decoration:none;box-shadow:0 10px 28px -8px rgba(0,0,0,.35);white-space:nowrap;animation:impop .25s both}'+
  '.imfab .impill:nth-child(2){animation-delay:.04s}'+
  '.imfab .impill svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.imfab .impill .imob{width:25px;height:16px;fill:currentColor;stroke:none}'+
  'html.menu-open .imfab{display:none}}'+
  '@keyframes impop{from{opacity:0;transform:translateY(10px) scale(.96)}}'+
  '@media (prefers-reduced-motion:reduce){.imfab,.imfab .impill{transition:none;animation:none}}'+
  '@media print{.imfab,.dock .imb{display:none!important}}';
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  document.documentElement.classList.add('has-im');
  document.documentElement.style.setProperty('--imc',dk[0]);document.documentElement.style.setProperty('--imo',dk[1]);

  /* glyphs: 100 units tall, in the manner of the OB logo */
  var G={
   M:[100,'M0,100V0H34L50,38L66,0H100V100H70V52L50,86L30,52V100Z'],
   Y:[92,'M0,0H33L46,36L59,0H92L63,58V100H29V58Z'],
   I:[34,'M0,0H34V100H0Z'],
   P:[82,'M0,0H66A16,16 0 0 1 82,16V50A16,16 0 0 1 66,66H34V100H0Z M50,18A8,8 0 0 1 58,26V40A8,8 0 0 1 50,48A8,8 0 0 1 42,40V26A8,8 0 0 1 50,18Z'],
   A:[84,'M0,100V16A16,16 0 0 1 16,0H68A16,16 0 0 1 84,16V100H52V74H32V100Z M42,22A8,8 0 0 1 50,30V46A8,8 0 0 1 42,54A8,8 0 0 1 34,46V30A8,8 0 0 1 42,22Z'],
   C:[84,'M16,0H68A16,16 0 0 1 84,16V40H52V30A8,8 0 0 0 36,30V70A8,8 0 0 0 52,70V60H84V84A16,16 0 0 1 68,100H16A16,16 0 0 1 0,84V16A16,16 0 0 1 16,0Z'],
   T:[86,'M0,0H86V34H60V100H26V34H0Z']
  };
  var WORD='MYIMPACT'.split('');
  var BREATH=[[1,1,1,1,1,1,1,1],[1.5,.7,.6,1.4,1.3,.8,.8,1.2],[.7,1.5,1.4,.6,.8,1.3,1.2,.8],[1.2,.9,1,1,.7,1,1.5,.9],[.9,1.2,1.3,.8,1.1,.8,1,1.3]];
  function br(k){return BREATH[k%BREATH.length]}
  function ease(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
  function rows(R,box,wt,gx,gy,hw){
    var out=[],hs=hw||R.map(function(){return 1}),ht=hs.reduce(function(a,b){return a+b},0),free=box.h-gy*(R.length-1),y=box.y;
    R.forEach(function(r,ri){var rh=free*hs[ri]/ht,sum=0;r.forEach(function(i){sum+=G[WORD[i]][0]*wt[i]});
      var k=(box.w-gx*(r.length-1))/sum,x=box.x;r.forEach(function(i){var w=G[WORD[i]][0]*wt[i]*k;out[i]={x:x,y:y,w:w,h:rh};x+=w+gx});y+=rh+gy});
    return out;
  }

  /* the section: the word MY IMPACT across the full width, the contributions below */
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  /* a title breaks into two lines of about the same length */
  function two(t){var w=String(t).split(' '),b=1,d=1e9;if(w.length<2)return esc(t);for(var i=1;i<w.length;i++){var x=Math.abs(w.slice(0,i).join(' ').length-w.slice(i).join(' ').length);if(x<d){d=x;b=i}}return esc(w.slice(0,b).join(' '))+'<br class="hb"> '+esc(w.slice(b).join(' '))}
  var sec=document.createElement('section');sec.className='imsec wrap';sec.id='my-impact';sec.setAttribute('aria-labelledby','im-h');
  sec.innerHTML='<h2 class="imw" id="im-h" tabindex="-1"><span class="vh">My impact</span><span class="iml" aria-hidden="true"></span></h2>'+
    '<ol class="impart" aria-label="My impact">'+SL.map(function(s,i){return '<li><span class="n">'+(i<9?'0':'')+(i+1)+'</span><h3>'+two(s[0])+'</h3><p>'+esc(s[1])+'</p></li>'}).join('')+'</ol>';
  host.parentNode.insertBefore(sec,host.nextSibling);
  var hd=sec.querySelector('.imw'),lt=sec.querySelector('.iml');
  var svgs=WORD.map(function(c){var s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.setAttribute('viewBox','0 0 '+G[c][0]+' 100');s.setAttribute('preserveAspectRatio','none');var p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d',G[c][1]);s.appendChild(p);lt.appendChild(s);return s});

  var L={},cur=null,run=0,played=false;
  function layout(){
    var ph=phoneQ.matches,W=lt.clientWidth,H=Math.round(W*(ph?.52:.4)),g=ph?5:Math.max(6,Math.round(W*.006));
    lt.style.height=H+'px';
    L={full:{x:0,y:0,w:W,h:H},mid:[[0,1],[2,3],[4,5,6,7]],fin:[[0,1],[2,3,4,5,6,7]],finH:[1,1.3],gx:g,gy:g};
  }
  function put(R){R.forEach(function(r,i){var s=svgs[i].style;s.left=r.x+'px';s.top=r.y+'px';s.width=Math.max(r.w,0)+'px';s.height=Math.max(r.h,0)+'px'});cur=R}
  function to(R,ms,stag){var from=cur,id=run,t0=performance.now(),n=R.length,tot=ms+stag*(n-1);
    return new Promise(function(done){if(reduce||!from){put(R);return done()}
      (function f(now){if(id!==run)return done();var o=[];for(var i=0;i<n;i++){var t=Math.min(Math.max((now-t0-i*stag)/ms,0),1),e=ease(t),a=from[i],b=R[i];o.push({x:a.x+(b.x-a.x)*e,y:a.y+(b.y-a.y)*e,w:a.w+(b.w-a.w)*e,h:a.h+(b.h-a.h)*e})}put(o);if(now-t0<tot)requestAnimationFrame(f);else done()})(t0)})}
  function settle(){return rows(L.fin,L.full,br(0),L.gx,L.gy,L.finH)}
  function hidden(){var a=rows([[0,1,2,3,4,5,6,7]],L.full,[1,1,1,1,1,1,1,1],L.gx,L.gy);return a.map(function(r){return {x:r.x,y:r.y+r.h,w:r.w,h:0}})}

  /* the opening, once, the first time the word scrolls into view (after Resn's "Sculpting Harmony") */
  function play(){if(played)return;played=true;run++;var id=run;
    if(reduce){put(settle());return}
    var one=[[0,1,2,3,4,5,6,7]],flat=[1,1,1,1,1,1,1,1],a=rows(one,L.full,flat,L.gx,L.gy);
    put(hidden());
    to(a,520,70)
    .then(function(){return id===run&&to(rows(one,L.full,[2.6,.5,.4,.6,1.8,.5,.5,.6],L.gx,L.gy),620,0)})
    .then(function(){return id===run&&to(rows(one,L.full,[.5,.6,.5,2.2,.5,.6,2.4,.5],L.gx,L.gy),620,0)})
    .then(function(){return id===run&&to(rows(L.mid,L.full,flat,L.gx,L.gy),700,35)})
    .then(function(){return id===run&&to(settle(),900,45)});
  }
  layout();
  if(reduce||!('IntersectionObserver' in window)){played=true;put(settle())}
  else{put(hidden());var io=new IntersectionObserver(function(es){if(es.some(function(e){return e.isIntersecting})){io.disconnect();play()}},{threshold:.35});io.observe(lt)}

  var rw=innerWidth;addEventListener('resize',function(){if(innerWidth===rw)return;rw=innerWidth;layout();if(played){run++;put(settle())}else put(hidden())});

  /* the buttons take the reader to the section */
  function goTo(e){closeMenu();hd.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});if(e&&e.detail===0)hd.focus({preventScroll:true})}

  /* desktop button, left of the dock */
  var dock=document.querySelector('.dock');
  if(dock){var ib=document.createElement('button');ib.type='button';ib.className='imb';ib.innerHTML=OB+'<span>My impact</span>';dock.insertBefore(ib,dock.firstChild);ib.addEventListener('click',goTo)}

  /* phones: one menu button, with My impact and To the top */
  var fab=document.createElement('div');fab.className='imfab';
  fab.style.setProperty('--imc',mc[0]);fab.style.setProperty('--imo',mc[1]);
  fab.innerHTML='<div class="impills" id="im-menu" hidden><button type="button" class="impill im-open">'+OB+'My impact</button><a class="impill im-top" href="#">'+UP+'To the top</a></div><button type="button" class="imm" aria-expanded="false" aria-controls="im-menu" aria-label="Menu">'+MENU+'</button>';
  document.body.appendChild(fab);
  var mb=fab.querySelector('.imm'),pills=fab.querySelector('.impills');
  function closeMenu(){pills.hidden=true;mb.setAttribute('aria-expanded','false');mb.innerHTML=MENU;mb.setAttribute('aria-label','Menu')}
  mb.addEventListener('click',function(e){e.stopPropagation();if(pills.hidden){pills.hidden=false;mb.setAttribute('aria-expanded','true');mb.innerHTML=X;mb.setAttribute('aria-label','Close menu')}else closeMenu()});
  fab.querySelector('.im-open').addEventListener('click',goTo);
  fab.querySelector('.im-top').addEventListener('click',function(e){e.preventDefault();closeMenu();scrollTo({top:0,behavior:reduce?'auto':'smooth'});var h=document.querySelector('.back');if(h&&e.detail===0)h.focus({preventScroll:true})});
  document.addEventListener('click',function(e){if(!pills.hidden&&!fab.contains(e.target))closeMenu()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!pills.hidden){closeMenu();mb.focus()}});
  function tick(){fab.classList.toggle('show',scrollY>innerHeight*.9)}
  addEventListener('scroll',tick,{passive:true});addEventListener('resize',tick);tick();
})();
