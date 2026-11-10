/* My impact modal for the case pages. Spec: impact-modal.md. Each page gives its slides in
   <script type="application/json" id="impact-data">{"after":"#solution","slides":[["Title","Text"],...]}</script>
   and loads this file after it. Colours come from the page's own To the top buttons. */
(function(){
  var dataEl=document.getElementById('impact-data');if(!dataEl)return;
  var DATA;try{DATA=JSON.parse(dataEl.textContent)}catch(e){return}
  var SL=DATA.slides||[];if(!SL.length)return;
  var KEY='impact-closed:'+location.pathname;
  function wasClosed(){try{return localStorage.getItem(KEY)==='1'}catch(e){return false}}
  function markClosed(){try{localStorage.setItem(KEY,'1')}catch(e){}}
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var phoneQ=matchMedia('(max-width:720px)'),dockQ=matchMedia('(min-width:901px)');

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
  '.imr{position:fixed;inset:0;z-index:300;display:none}.imr.open{display:block}'+
  '.imr .imbg{position:absolute;inset:0;background:rgba(14,14,14,.42);opacity:0;transition:opacity .35s}.imr.vis .imbg{opacity:1}'+
  '.imd{position:absolute;left:50%;top:50%;background:#fff;color:#0E0E0E;border-radius:20px;box-shadow:0 30px 80px rgba(0,0,0,.22);overflow:hidden;font-family:"Inter Tight",system-ui,sans-serif;outline:none}'+
  '.imd .iml{position:absolute;inset:0;pointer-events:none}.imd .iml svg{position:absolute;display:block}.imd .iml path{fill:#0E0E0E;fill-rule:evenodd}'+
  '.imd .imt{position:absolute;transition:opacity .45s,transform .45s}.imd .imt.off{opacity:0;transform:translateY(12px)}'+
  '.imd h2.imh{font-size:40px;font-weight:400;letter-spacing:-.03em;line-height:1.05;margin:0 0 16px;max-width:16ch;text-wrap:balance;color:#0E0E0E}'+
  '.imd p.imp{font-size:17px;line-height:1.5;color:#6B6B6B;max-width:42ch;margin:0}'+
  '.imd .imx{position:absolute;width:44px;height:44px;border:0;background:none;cursor:pointer;padding:0;color:#0E0E0E;transition:opacity .4s;border-radius:50%}'+
  '.imd .imx svg{width:30px;height:30px;margin:7px;fill:none;stroke:currentColor;stroke-width:1.4}'+
  '.imd .imx:focus-visible{outline:2px solid #0E0E0E;outline-offset:2px}'+
  '.imd .imdash{position:absolute;display:flex;gap:8px;justify-content:center;transition:opacity .4s}'+
  '.imd .imdash i{width:30px;height:4px;border-radius:2px;background:#D9D9D5;transition:width .4s,background .4s}.imd .imdash i.on{width:52px;background:#0E0E0E}'+
  '.imd.wait .imx,.imd.wait .imdash{opacity:0}'+
  '.imd.ph{border-radius:0;left:0;top:0;width:100%;height:100%;transform:none}'+
  '.imd.ph h2.imh{font-size:32px;max-width:none}.imd.ph p.imp{font-size:16px}'+
  '.imd.ph .imx{width:52px;height:52px;background:#0E0E0E;color:#fff;box-shadow:0 8px 24px rgba(0,0,0,.18)}.imd.ph .imx svg{width:28px;height:28px;margin:12px;stroke-width:2}'+
  '.imd .vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}'+
  /* desktop: the OB button left of the dock */
  '.dock .imb{flex:none;width:58px;height:58px;border-radius:50%;border:0;padding:0;cursor:pointer;display:flex;align-items:center;justify-content:center;background:var(--imc);color:var(--imo);box-shadow:0 12px 32px -10px rgba(0,0,0,.45);transition:filter .2s}'+
  '.dock .imb:hover,.dock .imb:focus-visible{filter:brightness(1.06)}.dock .imb .imob{width:31px;height:20px;fill:currentColor}'+
  /* phones: one menu button in place of To the top */
  'html.has-im .mtop{display:none!important}'+
  '.imfab{display:none}'+
  '@media (max-width:900px){.imfab{position:fixed;left:50%;bottom:calc(16px + env(safe-area-inset-bottom));z-index:60;display:flex;flex-direction:column;align-items:center;gap:10px;transform:translate(-50%,calc(100% + 40px));opacity:0;pointer-events:none;transition:transform .45s cubic-bezier(.22,.61,.36,1),opacity .3s}'+
  '.imfab.show{transform:translate(-50%,0);opacity:1;pointer-events:auto}'+
  '.imfab .imm{width:52px;height:52px;border-radius:50%;border:0;padding:0;cursor:pointer;background:var(--imc);color:var(--imo);box-shadow:0 10px 28px -8px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center}'+
  '.imfab .imm svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}'+
  '.imfab .impills{display:flex;flex-direction:column;align-items:center;gap:8px}.imfab .impills[hidden]{display:none}'+
  '.imfab .impill{display:flex;align-items:center;gap:10px;height:48px;padding:0 20px 0 16px;border-radius:999px;border:0;cursor:pointer;background:var(--imc);color:var(--imo);font:600 15px/1 "Inter Tight",system-ui,sans-serif;text-decoration:none;box-shadow:0 10px 28px -8px rgba(0,0,0,.35);white-space:nowrap;animation:impop .25s both}'+
  '.imfab .impill:nth-child(2){animation-delay:.04s}'+
  '.imfab .impill svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.imfab .impill .imob{width:25px;height:16px;fill:currentColor;stroke:none}'+
  'html.menu-open .imfab{display:none}}'+
  '@keyframes impop{from{opacity:0;transform:translateY(10px) scale(.96)}}'+
  '@media (prefers-reduced-motion:reduce){.imr .imbg,.imd .imt,.imfab,.imfab .impill{transition:none;animation:none}}'+
  '@media print{.imr,.imfab,.dock .imb{display:none!important}}';
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

  /* the modal */
  var root=document.createElement('div');root.className='imr';
  root.innerHTML='<div class="imbg"></div><div class="imd" role="dialog" aria-modal="true" aria-labelledby="im-title" tabindex="-1">'+
    '<h2 class="vh" id="im-title">My impact</h2><div class="iml" aria-hidden="true"></div>'+
    '<div class="imt" aria-live="polite"><p class="vh imn"></p><h2 class="imh"></h2><p class="imp"></p></div>'+
    '<div class="imdash" aria-hidden="true"></div><button class="imx" type="button" aria-label="Close">'+X+'</button></div>';
  document.body.appendChild(root);
  var dlg=root.querySelector('.imd'),lt=root.querySelector('.iml'),tx=root.querySelector('.imt'),hh=root.querySelector('.imh'),pp=root.querySelector('.imp'),nn=root.querySelector('.imn'),dash=root.querySelector('.imdash'),xb=root.querySelector('.imx');
  var svgs=WORD.map(function(c){var s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.setAttribute('viewBox','0 0 '+G[c][0]+' 100');s.setAttribute('preserveAspectRatio','none');var p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d',G[c][1]);s.appendChild(p);lt.appendChild(s);return s});
  if(SL.length>1)SL.forEach(function(){dash.appendChild(document.createElement('i'))});

  var kb=true,L={},cur=null,run=0,slide=0,busy=false,isOpen=false,lastFocus=null;
  function layout(){
    var vw=innerWidth,vh=innerHeight,ph=phoneQ.matches;dlg.classList.toggle('ph',ph);
    if(ph){
      var bw=vw-32,bh=Math.min(190,bw*.55);
      L={W:vw,H:vh,full:{x:16,y:20,w:bw,h:Math.min(vh*.8,600)},end:{x:16,y:20,w:bw,h:bh},mid:[[0,1],[2,3],[4,5,6,7]],fin:[[0,1],[2,3,4,5,6,7]],endH:null,gx:5,gy:5};
      dlg.style.width='';dlg.style.height='';
      tx.style.left='16px';tx.style.right='16px';tx.style.top=(20+bh+26)+'px';
      xb.style.cssText='left:50%;margin-left:-26px;bottom:calc(62px + env(safe-area-inset-bottom))';
      dash.style.cssText='left:0;right:0;bottom:calc(38px + env(safe-area-inset-bottom))';
    }else{
      var W=Math.min(900,vw-64),H=Math.min(540,vh-64),pad=28,pw=Math.round(W*.367);
      L={W:W,H:H,full:{x:pad,y:pad,w:W-pad*2,h:H-pad*2},end:{x:pad,y:pad,w:pw,h:H-pad*2},mid:[[0,1],[2,3,4,5,6,7]],fin:[[0,1],[2,3],[4,5,6,7]],endH:[1,1.45,1],gx:6,gy:6};
      dlg.style.width=W+'px';dlg.style.height=H+'px';
      var tl=pad+pw+42;tx.style.left=tl+'px';tx.style.right='56px';
      var e=rows(L.fin,L.end,br(0),L.gx,L.gy,L.endH),cs=getComputedStyle(hh),fs=parseFloat(cs.fontSize),lh=parseFloat(cs.lineHeight);
      tx.style.top=(e[2].y-(lh-fs*.7)/2)+'px';
      xb.style.cssText='right:22px;top:22px';dash.style.cssText='left:'+tl+'px;bottom:40px';
    }
  }
  function centre(){if(!dlg.classList.contains('ph'))dlg.style.transform='translate(-50%,-50%)';else dlg.style.transform='none'}
  function put(R){R.forEach(function(r,i){var s=svgs[i].style;s.left=r.x+'px';s.top=r.y+'px';s.width=Math.max(r.w,0)+'px';s.height=Math.max(r.h,0)+'px'});cur=R}
  function to(R,ms,stag){var from=cur,id=run,t0=performance.now(),n=R.length,tot=ms+stag*(n-1);
    return new Promise(function(done){if(reduce||!from){put(R);return done()}
      (function f(now){if(id!==run)return done();var o=[];for(var i=0;i<n;i++){var t=Math.min(Math.max((now-t0-i*stag)/ms,0),1),e=ease(t),a=from[i],b=R[i];o.push({x:a.x+(b.x-a.x)*e,y:a.y+(b.y-a.y)*e,w:a.w+(b.w-a.w)*e,h:a.h+(b.h-a.h)*e})}put(o);if(now-t0<tot)requestAnimationFrame(f);else done()})(t0)})}
  function settle(k){return rows(L.fin,L.end,br(k),L.gx,L.gy,L.endH)}
  function show(k){slide=k;hh.textContent=SL[k][0];pp.textContent=SL[k][1];nn.textContent=SL.length>1?('Slide '+(k+1)+' of '+SL.length):'';[].forEach.call(dash.children,function(d,i){d.classList.toggle('on',i===k)})}
  function play(){run++;var id=run;dlg.classList.add('wait');tx.classList.add('off');show(0);
    if(reduce){put(settle(0));dlg.classList.remove('wait');tx.classList.remove('off');return}
    var one=[[0,1,2,3,4,5,6,7]],flat=[1,1,1,1,1,1,1,1],a=rows(one,L.full,flat,L.gx,L.gy);
    cur=null;put(a.map(function(r){return {x:r.x,y:r.y+r.h,w:r.w,h:0}}));
    to(a,520,70)
    .then(function(){return id===run&&to(rows(one,L.full,[2.6,.5,.4,.6,1.8,.5,.5,.6],L.gx,L.gy),620,0)})
    .then(function(){return id===run&&to(rows(one,L.full,[.5,.6,.5,2.2,.5,.6,2.4,.5],L.gx,L.gy),620,0)})
    .then(function(){return id===run&&to(rows(L.mid,L.full,flat,L.gx,L.gy),700,35)})
    .then(function(){return id===run&&to(settle(0),900,45)})
    .then(function(){if(id!==run)return;dlg.classList.remove('wait');tx.classList.remove('off')});
  }
  function go(d){var k=slide+d;if(busy||k<0||k>=SL.length||dlg.classList.contains('wait'))return;busy=true;tx.classList.add('off');
    setTimeout(function(){show(k);tx.classList.remove('off')},260);to(settle(k),700,30).then(function(){busy=false})}

  var others=[];
  function open(){if(isOpen)return;isOpen=true;closeMenu();lastFocus=document.activeElement;
    others=[].filter.call(document.body.children,function(el){return el!==root&&el.tagName!=='SCRIPT'&&!el.inert});others.forEach(function(el){el.inert=true});
    var sb=innerWidth-document.documentElement.clientWidth;document.documentElement.style.overflow='hidden';if(sb>0)document.documentElement.style.paddingRight=sb+'px';root.classList.add('open');layout();centre();
    dlg.getAnimations&&dlg.getAnimations().forEach(function(a){a.cancel()});
    requestAnimationFrame(function(){root.classList.add('vis')});dlg.focus({preventScroll:true});play();}
  function target(){var b=dockQ.matches?document.querySelector('.dock.show .imb'):(fab.classList.contains('show')?fab.querySelector('.imm'):null);return b}
  function close(){if(!isOpen)return;isOpen=false;run++;markClosed();
    var b=target(),done=function(){root.classList.remove('open','vis');document.documentElement.style.overflow='';document.documentElement.style.paddingRight='';others.forEach(function(el){el.inert=false});others=[];
      var f=b||(lastFocus&&document.contains(lastFocus)?lastFocus:null);if(kb&&f)f.focus({preventScroll:true});else if(document.activeElement&&document.activeElement.blur)document.activeElement.blur()};
    root.classList.remove('vis');
    if(reduce||!b||!dlg.animate){done();return}
    /* the modal folds into its button */
    var r=dlg.getBoundingClientRect(),t=b.getBoundingClientRect(),dx=t.left+t.width/2-(r.left+r.width/2),dy=t.top+t.height/2-(r.top+r.height/2),s=t.width/r.width,base=dlg.classList.contains('ph')?'':'translate(-50%,-50%) ';
    var an=dlg.animate([{transform:base+'translate(0,0) scale(1)',opacity:1,borderRadius:dlg.classList.contains('ph')?'0px':'20px'},{transform:base+'translate('+dx+'px,'+dy+'px) scale('+s+')',opacity:0,borderRadius:'999px'}],{duration:520,easing:'cubic-bezier(.6,0,.2,1)'});
    an.onfinish=function(){an.cancel();done()};
  }
  xb.addEventListener('click',function(e){kb=e.detail===0;close()});
  root.querySelector('.imbg').addEventListener('click',function(){kb=false;close()});
  root.addEventListener('keydown',function(e){
    if(e.key==='Escape'){e.preventDefault();kb=true;close();return}
    if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();go(1)}
    if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();go(-1)}
    if(e.key==='Tab'){e.preventDefault();(document.activeElement===xb?dlg:xb).focus()}
  });
  var wl=0;root.addEventListener('wheel',function(e){e.preventDefault();var n=Date.now();if(n-wl<750||Math.abs(e.deltaY)<8)return;wl=n;go(e.deltaY>0?1:-1)},{passive:false});
  var sx=0,sy=0;root.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;sy=e.touches[0].clientY},{passive:true});
  root.addEventListener('touchmove',function(e){e.preventDefault()},{passive:false});
  root.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;if(Math.abs(dx)>40&&Math.abs(dx)>Math.abs(dy))go(dx<0?1:-1);else if(Math.abs(dy)>40)go(dy<0?1:-1)});
  addEventListener('resize',function(){if(!isOpen)return;layout();centre();if(!dlg.classList.contains('wait'))put(settle(slide));else{run++;dlg.classList.remove('wait');tx.classList.remove('off');put(settle(slide))}});

  /* desktop button, left of the dock */
  var dock=document.querySelector('.dock');
  if(dock){var ib=document.createElement('button');ib.type='button';ib.className='imb';ib.setAttribute('aria-label','My impact');ib.title='My impact';ib.innerHTML=OB;dock.insertBefore(ib,dock.firstChild);ib.addEventListener('click',open)}

  /* phones: one menu button, with My impact and To the top */
  var fab=document.createElement('div');fab.className='imfab';
  fab.style.setProperty('--imc',mc[0]);fab.style.setProperty('--imo',mc[1]);
  fab.innerHTML='<div class="impills" id="im-menu" hidden><button type="button" class="impill im-open">'+OB+'My impact</button><a class="impill im-top" href="#">'+UP+'To the top</a></div><button type="button" class="imm" aria-expanded="false" aria-controls="im-menu" aria-label="Menu">'+MENU+'</button>';
  document.body.appendChild(fab);
  var mb=fab.querySelector('.imm'),pills=fab.querySelector('.impills');
  function closeMenu(){pills.hidden=true;mb.setAttribute('aria-expanded','false');mb.innerHTML=MENU;mb.setAttribute('aria-label','Menu')}
  mb.addEventListener('click',function(e){e.stopPropagation();var o=pills.hidden;if(o){pills.hidden=false;mb.setAttribute('aria-expanded','true');mb.innerHTML=X;mb.setAttribute('aria-label','Close menu')}else closeMenu()});
  fab.querySelector('.im-open').addEventListener('click',open);
  fab.querySelector('.im-top').addEventListener('click',function(e){e.preventDefault();closeMenu();scrollTo({top:0,behavior:reduce?'auto':'smooth'});var h=document.querySelector('.back');if(h&&e.detail===0)h.focus({preventScroll:true})});
  document.addEventListener('click',function(e){if(!pills.hidden&&!fab.contains(e.target))closeMenu()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!pills.hidden){closeMenu();mb.focus()}});

  /* it opens by itself once the reader has scrolled past the given block, until it has been closed once */
  var after=document.querySelector(DATA.after||'#solution');after=after&&(after.closest('.pair')||after);
  function tick(){fab.classList.toggle('show',scrollY>innerHeight*.9||(after&&after.getBoundingClientRect().bottom<innerHeight*.6));
    if(!isOpen&&!opened&&after&&!wasClosed()&&after.getBoundingClientRect().bottom<innerHeight*.5){opened=true;open()}}
  var opened=false;addEventListener('scroll',tick,{passive:true});addEventListener('resize',tick);tick();
})();
