import { chromium } from '/Users/apple/Downloads/CAG/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const SRC = process.argv[4] || '/Users/apple/Downloads/CAG/docs/design/homepage-variations';
const SCRATCH = process.argv[2];
const OUT = process.argv[3];
fs.rmSync(SCRATCH,{recursive:true,force:true}); fs.mkdirSync(SCRATCH,{recursive:true});
for (const f of fs.readdirSync(SRC)) {
  if (f.endsWith('.dc.html')) {
    let t = fs.readFileSync(path.join(SRC,f),'utf8');
    t = t.replace(/<script src="\.\/support\.js"><\/script>/g,'');
    fs.writeFileSync(path.join(SCRATCH,f), t);
  } else if (/\.(webp|png|jpg|jpeg|svg)$/i.test(f)) {
    fs.copyFileSync(path.join(SRC,f), path.join(SCRATCH,f));
  }
}
const width = f => f.includes('-Mobile') ? 390 : f.includes('-Tablet') ? 768 : 1440;
const browser = await chromium.launch();
const results = [];
const files = fs.readdirSync(SCRATCH).filter(f=>f.endsWith('.dc.html')).sort();
for (const f of files) {
  const w = width(f);
  const isMobile = f.includes('-Mobile');
  const page = await browser.newPage({ viewport:{width:w, height:900}, deviceScaleFactor:1 });
  await page.goto('file://'+path.join(SCRATCH,f));
  await page.evaluate(()=>document.fonts.ready);
  await page.waitForTimeout(250);
  const r = await page.evaluate(({isMobile}) => {
    const root = document.querySelector('x-dc > div') || document.body.firstElementChild;
    const parse = c => { const m=c.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p=m[1].split(',').map(s=>parseFloat(s)); return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}; };
    const lum = c => { const f=v=>{v/=255; return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4);}; return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b); };
    const ratio = (a,b) => { const L1=lum(a),L2=lum(b); return (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05); };
    const blend=(fg,bg)=>({r:fg.r*fg.a+bg.r*(1-fg.a),g:fg.g*fg.a+bg.g*(1-fg.a),b:fg.b*fg.a+bg.b*(1-fg.a),a:1});
    const visible = el => { const s=getComputedStyle(el); if(s.display==='none'||s.visibility==='hidden'||parseFloat(s.opacity)===0) return false; const rr=el.getBoundingClientRect(); return rr.width>0&&rr.height>0; };
    const out = { scrollWidth: document.documentElement.scrollWidth, rootWidth: root?root.getBoundingClientRect().width:0, rootHeight: root?Math.ceil(root.getBoundingClientRect().height):0, minFont:null, minFontSel:null, smallTargets:[], contrast:[], overImage:[], examined:0, overPhoto:[] };
    const sel = el => { let s=el.tagName.toLowerCase(); if(el.className && typeof el.className==='string' && el.className.trim()) s+='.'+el.className.trim().split(/\s+/)[0]; const txt=(el.textContent||'').trim().slice(0,42); return s+' "'+txt+'"'; };
    const all = [...document.querySelectorAll('x-dc *')];
    for (const el of all) {
      if (!visible(el)) continue;
      const hasOwnText = [...el.childNodes].some(n=>n.nodeType===3 && n.textContent.trim().length>0);
      const s = getComputedStyle(el);
      const fs_ = parseFloat(s.fontSize);
      if (hasOwnText) {
        out.examined++;
        const er = el.getBoundingClientRect();
        for (const im of document.querySelectorAll('x-dc img')) {
          if (!visible(im)) continue;
          const ir = im.getBoundingClientRect();
          if (er.left < ir.right && er.right > ir.left && er.top < ir.bottom && er.bottom > ir.top) {
            // is there an opaque bg between el and the img's stacking context?
            let n=el, opaque=false;
            while (n && n!==document.documentElement) { const c=parse(getComputedStyle(n).backgroundColor); if(c&&c.a>=0.999){opaque=true;break;} if(n.contains(im)) break; n=n.parentElement; }
            if (!opaque) out.overPhoto.push({ sel: sel(el), fs: parseFloat(getComputedStyle(el).fontSize), color: getComputedStyle(el).color });
            break;
          }
        }
        if (isMobile && (out.minFont===null || fs_ < out.minFont)) { out.minFont=fs_; out.minFontSel=sel(el); }
        // background
        let bgEl=el, bg=null, imgAncestor=false;
        while (bgEl && bgEl!==document.documentElement) {
          const bs=getComputedStyle(bgEl);
          if (bs.backgroundImage && bs.backgroundImage!=='none') imgAncestor=true;
          const c=parse(bs.backgroundColor);
          if (c && c.a>=0.999) { bg=c; break; }
          bgEl=bgEl.parentElement;
        }
        if (!bg) bg={r:255,g:255,b:255,a:1};
        let fg=parse(s.color); if(!fg) continue;
        if (fg.a<1) fg=blend(fg,bg);
        const cr = ratio(fg,bg);
        const bold = parseInt(s.fontWeight)>=700;
        const large = fs_>=24 || (bold && fs_>=18.66);
        const need = large?3:4.5;
        if (cr < need) {
          const rec = { sel: sel(el), fs: fs_, bold, ratio: Math.round(cr*100)/100, need, fg:s.color, bg:`rgb(${Math.round(bg.r)},${Math.round(bg.g)},${Math.round(bg.b)})`, overImage: imgAncestor };
          (imgAncestor ? out.overImage : out.contrast).push(rec);
        }
      }
      if (isMobile && el.matches('a,button,[role=button],summary')) {
        const rr=el.getBoundingClientRect();
        if (rr.height < 44) out.smallTargets.push({ sel: sel(el), h: Math.round(rr.height*10)/10 });
      }
    }
    return out;
  }, {isMobile});
  r.file=f; r.frameWidth=w; results.push(r);
  await page.close();
}
await browser.close();
fs.writeFileSync(OUT, JSON.stringify(results,null,1));
// summary
let ov=0,cf=0,st=0,sf=0,oi=0,op=0;
for (const r of results) {
  if (r.scrollWidth > r.frameWidth+1) { ov++; console.log('OVERFLOW',r.file, r.scrollWidth,'>',r.frameWidth); }
  if (Math.abs(r.rootWidth-r.frameWidth)>1) console.log('ROOTWIDTH',r.file,r.rootWidth,'!=',r.frameWidth);
  if (r.minFont!==null && r.minFont<14) { sf++; console.log('SMALLFONT',r.file,r.minFont,r.minFontSel); }
  if (r.smallTargets.length) { st+=r.smallTargets.length; console.log('HIT<44',r.file, r.smallTargets.map(t=>t.h+' '+t.sel).join(' | ')); }
  if (r.contrast.length) { cf+=r.contrast.length; console.log('CONTRAST',r.file, r.contrast.map(c=>c.ratio+':1 '+c.fs+'px '+c.fg+' on '+c.bg+' '+c.sel).join(' || ')); }
  if (r.overImage.length) oi+=r.overImage.length;
  if (r.examined < 5) console.log('!! LOW EXAMINED', r.file, r.examined);
  if (r.overPhoto && r.overPhoto.length) { op+=r.overPhoto.length; console.log('OVER-PHOTO', r.file, r.overPhoto.map(o=>o.fs+'px '+o.color+' '+o.sel).join(' | ')); }
}
console.log('\nTOTALS files='+results.length,'overflow='+ov,'smallFont='+sf,'hitTargets='+st,'contrastFails='+cf,'overImageIndeterminate='+oi,'overPhotoText='+op,'examinedTotal='+results.reduce((a,r)=>a+r.examined,0));
