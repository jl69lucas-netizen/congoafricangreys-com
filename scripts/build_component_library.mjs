#!/usr/bin/env node
/**
 * build_component_library.mjs
 *
 * Reads docs/artifacts/component-library/manifest.json plus the webp captures beside it
 * and writes two deterministic files:
 *   docs/artifacts/cags-component-library.md    markdown source of truth
 *   docs/artifacts/cags-component-library.html  the browsable artifact page
 *
 * Re-run after scripts/component_library_capture.mjs re-captures the components.
 */
import { readFileSync, writeFileSync, statSync } from 'node:fs';
import { join, dirname, basename, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const LIB = join(ROOT, 'docs/artifacts/component-library');
const MD_OUT = join(ROOT, 'docs/artifacts/cags-component-library.md');
const HTML_OUT = join(ROOT, 'docs/artifacts/cags-component-library.html');
const ARTIFACT_URL = 'https://claude.ai/code/artifact/6be797ba-d2bf-4cb8-b8e2-601cbade03d2';
const VPS = ['375', '768', '1280'];
const ORDER = ['hero', 'counter', 'toc', 'table', 'bird-card', 'reviews', 'trust',
  'key-takeaway', 'owner', 'faq', 'shipping', 'seam', 'newsletter', 'form'];

const manifest = JSON.parse(readFileSync(join(LIB, 'manifest.json'), 'utf8'));
const rows = manifest.rows.slice();
const genDate = manifest.generated.slice(0, 10);
const commit = manifest.commit.slice(0, 7);

const cats = ORDER.filter((c) => rows.some((r) => r.category === c));
for (const r of rows) if (!ORDER.includes(r.category)) throw new Error(`unordered category: ${r.category}`);
const byCat = (c) => rows.filter((r) => r.category === c);
const captureCount = rows.reduce((n, r) => n + VPS.filter((v) => r.captures[v]).length, 0);

/* ---------- helpers ---------- */
const pascal = (s) => s.split(/[-_.]/).filter(Boolean).map((w) => w[0].toUpperCase() + w.slice(1)).join('');
const href = (r) => 'https://congoafricangreys.com/' + (r.page ? r.page + '/' : '');
const pageLabel = (r) => (r.page ? `/${r.page}/` : '/');
const isComponent = (r) => r.source.startsWith('src/components/');
const importName = (r) => pascal(basename(r.source, extname(r.source)));
const usageLine = (r) => (isComponent(r)
  ? `import ${importName(r)} from '${r.source}';`
  : `Inline in ${r.source}; search for ${r.selector}`);
const usageMd = (r) => (isComponent(r)
  ? `\`import ${importName(r)} from '${r.source}';\``
  : `Inline in \`${r.source}\`; search for \`${r.selector}\``);
const capMark = (r, v) => (r.captures[v] ? '✓' : 'hidden');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function cardMarkdown(r) {
  const lines = [
    `### ${r.name}`,
    '',
    `- Category: ${r.category}`,
    `- Page: ${pageLabel(r)} (${href(r)})`,
    `- Source: \`${r.source}\``,
    `- Selector: \`${r.selector}\``,
    `- Captures: ${VPS.map((v) => `${v} ${capMark(r, v)}`).join(' / ')}`,
    '',
  ];
  if (isComponent(r)) {
    lines.push('```astro', `import ${importName(r)} from '${r.source}';`, '```');
  } else {
    lines.push(`Inline page markup. Open \`${r.source}\` and search for \`${r.selector}\`.`);
  }
  return lines.join('\n') + '\n';
}

/* ---------- markdown ---------- */
const md = [];
md.push('# C.A.Gs Component Library', '');
md.push(`**Artifact URL:** ${ARTIFACT_URL}`, '');
md.push(`Every live C.A.Gs component captured in a real browser at 375, 768 and 1280. ${rows.length} components, ${captureCount} captures, generated ${genDate} from commit \`${commit}\`.`, '');
md.push('Rebuild: `node scripts/component_library_capture.mjs` to re-capture, then `node scripts/build_component_library.mjs` to regenerate this file and the HTML page beside it.', '');
md.push('A capture marked `hidden` means the component does not render at that width, which is the component telling you its own responsive contract.', '');
for (const c of cats) {
  const list = byCat(c);
  md.push(`## ${c} (${list.length})`, '');
  md.push('| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |');
  md.push('|---|---|---|---|:--:|:--:|:--:|---|');
  for (const r of list) {
    md.push(`| ${r.name} | [${pageLabel(r)}](${href(r)}) | \`${r.source}\` | \`${r.selector}\` | ${capMark(r, '375')} | ${capMark(r, '768')} | ${capMark(r, '1280')} | ${usageMd(r)} |`);
  }
  md.push('');
}
const mdText = md.join('\n');
writeFileSync(MD_OUT, mdText);

/* ---------- html ---------- */
const dataUri = (file) => 'data:image/webp;base64,' + readFileSync(join(LIB, file)).toString('base64');

const chips = ['all', ...cats].map((c) => {
  const n = c === 'all' ? rows.length : byCat(c).length;
  return `<button class="chip${c === 'all' ? ' on' : ''}" type="button" data-cat="${c}">${c === 'all' ? 'All' : esc(c)} <span class="n">${n}</span></button>`;
}).join('');

const vpButtons = [...VPS, 'all'].map((v) =>
  `<button class="chip vp${v === '1280' ? ' on' : ''}" type="button" data-vp="${v}">${v === 'all' ? 'All' : v}</button>`).join('');

function cardHtml(r) {
  const shots = VPS.map((v) => {
    const c = r.captures[v];
    if (!c) return `<div class="shot" data-vp="${v}" hidden><p class="none">Hidden at ${v}px. This component does not render at that width.</p></div>`;
    return `<div class="shot" data-vp="${v}"${v === '1280' ? '' : ' hidden'}><span class="vplab">${v}px</span><div class="frame"><img src="${dataUri(c.file)}" width="${c.w}" height="${c.h}" loading="lazy" decoding="async" alt="${esc(r.name)} at ${v}px"></div></div>`;
  }).join('');
  return `<article class="card" data-cat="${r.category}">
<header class="chead"><h3>${esc(r.name)}</h3><button class="copy" type="button" data-label="Copy usage">Copy usage</button></header>
<p class="meta"><a href="${href(r)}" target="_blank" rel="noopener">${esc(pageLabel(r))}</a> <span class="dot">&middot;</span> <code>${esc(r.source)}</code> <span class="dot">&middot;</span> <code>${esc(r.selector)}</code></p>
<p class="use"><code>${esc(usageLine(r))}</code></p>
<div class="shots">${shots}</div>
<script type="text/markdown" class="usage">${esc(cardMarkdown(r))}</script>
</article>`;
}

const sections = cats.map((c) => `<section class="cat" id="cat-${c}" data-cat="${c}">
<h2>${esc(c)} <span class="n">${byCat(c).length}</span></h2>
<div class="grid">${byCat(c).map(cardHtml).join('\n')}</div>
</section>`).join('\n');

const html = `<title>C.A.Gs Component Library</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --ground:#faf7f4; --paper:#ffffff; --ink:#1e2a24; --ink-2:#4b5a52; --ink-3:#7a867f;
  --line:#e2ddd4; --green:#2d6a4f; --green-soft:#eaf4ef; --clay:#e8604c; --clay-ink:#b04228;
  --clay-soft:#fbe7e2; --code-bg:#f2efe9; --shadow:0 1px 2px rgba(60,30,10,.05),0 8px 24px rgba(60,30,10,.05);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#151a17; --paper:#1d2420; --ink:#eceae3; --ink-2:#b7bdb6; --ink-3:#818b85;
    --line:#2f3934; --green:#78bd97; --green-soft:#1f2f28; --clay:#f08a78; --clay-ink:#f2a394;
    --clay-soft:#3a2622; --code-bg:#11161380; --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.25);
  }
}
:root[data-theme="dark"]{
  --ground:#151a17; --paper:#1d2420; --ink:#eceae3; --ink-2:#b7bdb6; --ink-3:#818b85;
  --line:#2f3934; --green:#78bd97; --green-soft:#1f2f28; --clay:#f08a78; --clay-ink:#f2a394;
  --clay-soft:#3a2622; --code-bg:#11161380; --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.25);
}
*{box-sizing:border-box}
[hidden]{display:none !important}
body{margin:0;background:var(--ground);color:var(--ink);font:16px/1.6 "IBM Plex Sans",system-ui,-apple-system,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
.wrap{max-width:1240px;margin:0 auto;padding:36px 20px 96px;display:grid;gap:28px}
header.masthead{display:grid;gap:8px;padding-bottom:18px;border-bottom:2px solid var(--green)}
.eyebrow{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--green);font-weight:600;margin:0}
h1{font-family:Newsreader,Georgia,serif;font-weight:600;font-size:clamp(28px,4.2vw,42px);line-height:1.08;margin:0;text-wrap:balance}
.sub{color:var(--ink-2);margin:0;font-size:14.5px;max-width:74ch}
.bar{position:sticky;top:0;z-index:20;background:var(--ground);border-bottom:1px solid var(--line);padding:12px 0;display:grid;gap:10px;margin:0}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.lab{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600;margin-right:2px}
.chip{font:inherit;font-size:13px;font-weight:500;padding:6px 12px;border-radius:50px;border:1px solid var(--line);background:var(--paper);color:var(--ink-2);cursor:pointer;transition:background .18s,color .18s,border-color .18s}
.chip .n{font-size:11px;color:var(--ink-3);font-variant-numeric:tabular-nums}
.chip:hover{border-color:var(--green);color:var(--green)}
.chip.on{background:var(--green);border-color:var(--green);color:#fff}
.chip.on .n{color:rgba(255,255,255,.75)}
.chip:focus-visible,.copy:focus-visible,a:focus-visible{outline:3px solid var(--clay);outline-offset:2px;border-radius:4px}
.btn{font:inherit;font-size:13px;font-weight:600;padding:6px 14px;border-radius:50px;border:1px solid var(--clay);background:var(--clay);color:#fff;cursor:pointer}
.btn.done{background:var(--green);border-color:var(--green)}
section.cat{display:grid;gap:14px}
section.cat h2{font-family:Newsreader,Georgia,serif;font-weight:600;font-size:22px;margin:0;line-height:1.2;display:flex;align-items:baseline;gap:8px}
section.cat h2 .n{font-family:"IBM Plex Sans",sans-serif;font-size:11.5px;font-weight:600;color:var(--green);background:var(--green-soft);padding:2px 9px;border-radius:50px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr));gap:18px}
.card{min-width:0;background:var(--paper);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);padding:16px 16px 18px;display:grid;gap:10px;align-content:start}
.chead{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.chead h3{font-family:Newsreader,Georgia,serif;font-size:17px;font-weight:600;margin:0;line-height:1.25}
.copy{flex:none;font:inherit;font-size:11.5px;font-weight:600;letter-spacing:.03em;padding:5px 11px;border-radius:50px;border:1px solid var(--line);background:transparent;color:var(--ink-2);cursor:pointer;transition:border-color .18s,color .18s,background .18s}
.copy:hover{border-color:var(--green);color:var(--green)}
.copy.done{border-color:var(--green);background:var(--green-soft);color:var(--green)}
.meta,.use{margin:0;font-size:12px;color:var(--ink-3);line-height:1.5;overflow-wrap:anywhere}
.meta a{color:var(--clay-ink);text-decoration:none;border-bottom:1px solid var(--line);font-weight:500}
.meta a:hover{border-color:var(--clay-ink)}
.dot{color:var(--line)}
code{font:11.5px/1.5 "IBM Plex Mono",ui-monospace,Menlo,monospace;background:var(--code-bg);padding:1px 5px;border-radius:4px;color:var(--ink-2)}
.use code{display:block;padding:7px 9px;color:var(--ink)}
.shots{display:grid;gap:10px;min-width:0}
.shot{min-width:0;display:grid;gap:5px}
.vplab{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.frame{overflow:auto;border:1px solid var(--line);border-radius:16px;background:var(--ground)}
.frame img{display:block;height:auto;max-width:100%}
body.actual .frame img{max-width:none}
.none{margin:0;font-size:12px;color:var(--ink-3);border:1px dashed var(--line);border-radius:16px;padding:14px;background:var(--ground)}
.empty{display:none;color:var(--ink-3);font-size:14px}
.toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);background:var(--ink);color:var(--ground);padding:9px 16px;border-radius:50px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:40}
.toast.show{opacity:1}
@media (max-width:520px){.bar{padding:10px 0}.wrap{padding:24px 14px 72px}}
</style>

<div class="wrap">
<header class="masthead">
  <p class="eyebrow">CongoAfricanGreys.com &middot; Component library</p>
  <h1>C.A.Gs Component Library</h1>
  <p class="sub">${rows.length} components, ${captureCount} captures at 375, 768 and 1280, generated ${genDate} from commit <code>${commit}</code>.</p>
</header>

<div class="bar">
  <div class="row"><span class="lab">Category</span>${chips}</div>
  <div class="row"><span class="lab">Viewport</span>${vpButtons}<span class="lab" style="margin-left:14px">Scale</span><button class="chip fit on" type="button" data-fit="fit">Fit</button><button class="chip fit" type="button" data-fit="actual">Actual</button><button class="btn" type="button" id="copy-all" data-label="Copy whole library as Markdown">Copy whole library as Markdown</button></div>
</div>

<p class="empty" id="empty">No components in that category.</p>
${sections}
</div>
<div class="toast" id="toast">Copied</div>

<script type="text/markdown" id="full-md">${esc(mdText)}</script>
<script>
(function(){
  var toast=document.getElementById('toast');
  function flash(btn){ if(btn){ var l=btn.getAttribute('data-label'); btn.classList.add('done'); btn.textContent='Copied'; setTimeout(function(){btn.classList.remove('done'); btn.textContent=l;},1400);} toast.classList.add('show'); setTimeout(function(){toast.classList.remove('show');},1200); }
  function fallback(t){ var ta=document.createElement('textarea'); ta.value=t; ta.style.position='fixed'; ta.style.opacity='0'; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(e){} document.body.removeChild(ta); }
  function copy(t,btn){ if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(t).then(function(){flash(btn);},function(){fallback(t);flash(btn);}); } else { fallback(t); flash(btn); } }
  function store(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  function load(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }

  var catChips=[].slice.call(document.querySelectorAll('.chip[data-cat]'));
  var vpChips=[].slice.call(document.querySelectorAll('.chip[data-vp]'));
  var fitChips=[].slice.call(document.querySelectorAll('.chip[data-fit]'));
  var secs=[].slice.call(document.querySelectorAll('section.cat'));
  var empty=document.getElementById('empty');

  function setCat(cat){
    catChips.forEach(function(c){ c.classList.toggle('on', c.getAttribute('data-cat')===cat); });
    var any=false;
    secs.forEach(function(s){ var show=(cat==='all'||s.getAttribute('data-cat')===cat); s.hidden=!show; if(show) any=true; });
    empty.style.display=any?'none':'block';
    store('cag-cl-cat',cat);
  }
  function setVp(vp){
    vpChips.forEach(function(c){ c.classList.toggle('on', c.getAttribute('data-vp')===vp); });
    [].slice.call(document.querySelectorAll('.shot')).forEach(function(s){
      s.hidden = !(vp==='all' || s.getAttribute('data-vp')===vp);
    });
    store('cag-cl-vp',vp);
  }
  function setFit(f){
    fitChips.forEach(function(c){ c.classList.toggle('on', c.getAttribute('data-fit')===f); });
    document.body.classList.toggle('actual', f==='actual');
    store('cag-cl-fit',f);
  }
  catChips.forEach(function(c){ c.addEventListener('click',function(){ setCat(c.getAttribute('data-cat')); }); });
  vpChips.forEach(function(c){ c.addEventListener('click',function(){ setVp(c.getAttribute('data-vp')); }); });
  fitChips.forEach(function(c){ c.addEventListener('click',function(){ setFit(c.getAttribute('data-fit')); }); });

  [].slice.call(document.querySelectorAll('.card')).forEach(function(card){
    var src=card.querySelector('script.usage');
    card.querySelector('.copy').addEventListener('click',function(){ copy(src.textContent.trim()+'\\n', this); });
  });
  var all=document.getElementById('copy-all');
  all.addEventListener('click',function(){ copy(document.getElementById('full-md').textContent, this); });

  var savedCat=load('cag-cl-cat'); var savedVp=load('cag-cl-vp'); var savedFit=load('cag-cl-fit');
  setCat(savedCat&&document.querySelector('.chip[data-cat="'+savedCat.replace(/"/g,'')+'"]')?savedCat:'all');
  setVp(savedVp&&['375','768','1280','all'].indexOf(savedVp)>-1?savedVp:'1280');
  setFit(savedFit==='actual'?'actual':'fit');
})();
</script>
`;

writeFileSync(HTML_OUT, html);

const kb = (p) => (statSync(p).size / 1024).toFixed(1);
console.log(`components ${rows.length} / captures ${captureCount} / categories ${cats.length}`);
console.log(`${MD_OUT}  ${kb(MD_OUT)} KB`);
console.log(`${HTML_OUT}  ${(statSync(HTML_OUT).size / 1048576).toFixed(2)} MB`);
console.log(`<title> byte offset: ${html.indexOf('<title>')}`);
