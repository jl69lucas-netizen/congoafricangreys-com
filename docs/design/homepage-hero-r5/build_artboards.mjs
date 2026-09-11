// Generates the 9 hero artboards (A/B/C × Mobile/Tablet/Desktop) for round 5.
// Copy is the live HeroV3 copy, verbatim (src/components/cag-library/HeroV3.astro).
// Run: node docs/design/homepage-hero-r5/build_artboards.mjs
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const DIR = path.dirname(fileURLToPath(import.meta.url));

// ── Tokens (CONTRACT §3, never invented) ─────────────────────────────
const BED = '#0f3d2c';   // forest dark scrim — clay H1 span reads 3.45:1 here (large text)
const AVI = '#234f3b';
const FOREST = '#2D6A4F';
const CLAY = '#e8604c';
const CLAY_INK = '#c8472f';
const CLAY_SM = '#b04228';
const CREAM = '#faf7f4';
const INK = '#1f2a24';
const EYEBROW_DK = '#9fb1ab';
const LEAD_DK = '#cfd8d5';
const CRED_DK = '#dbe2df';
const SHADOW = '0 6px 28px rgba(60,30,10,.12)';
const RULE = `1px solid ${FOREST}`; // hero/counter seam: tone shift + 1px rule

// ── Live copy (verbatim) ─────────────────────────────────────────────
const EYEBROW = 'C.A.Gs &middot; Family Aviary Since 2014';
const H1_A = 'Congo and Timneh African Grey Breeder in';
const H1_B = 'Midland, Texas';
const LEAD = 'Mark &amp; Teri Benjamin have hand-raised captive-bred Congo and Timneh African Greys in our family home since 2014. Every Grey is lab-sexed, avian-vet certified and <a href="#proof" style="color:inherit; text-decoration:underline; text-decoration-color:rgba(232,96,76,.55); text-underline-offset:3px;">documented</a> before it leaves us &mdash; never wild-caught, always with lifetime breeder support.';
const CTA1 = 'View Available Greys &rarr;';
const CTA2 = 'Reserve Yours Now &rarr;';
const CREDS = ['USDA AWA Licensed', 'CITES Appendix I Documented', 'PCR DNA-Sexed', 'Avian-Vet Certified'];
const AVAIL = '6 Birds Available Now';
const ALT = 'Hand-raised Congo African Grey parrot with silver-scalloped grey plumage and a red tail in the Benjamin family aviary';

// ── Pieces ───────────────────────────────────────────────────────────
const span = (clayColor = CLAY) =>
  `<span style="color:${clayColor}; font-style:italic;">${H1_B}</span>`;

const eyebrow = (color = EYEBROW_DK, align = 'left') =>
  `<span style="display:block; font-size:13px; font-weight:500; letter-spacing:.1em; line-height:18px; color:${color}; text-align:${align};">${EYEBROW}</span>`;

const h1 = (size, { align = 'left', lh = 1.1, color = '#faf7f4', maxw = 'none' } = {}) =>
  `<h1 style="font-size:${size}px; line-height:${lh}; letter-spacing:-.012em; color:${color}; text-align:${align}; max-width:${maxw}; text-wrap:balance;">${H1_A} ${span()}</h1>`;

const lead = (size, { align = 'left', maxw = '62ch', color = LEAD_DK } = {}) =>
  `<p style="font-size:${size}px; line-height:1.6; color:${color}; text-align:${align}; max-width:${maxw}; text-wrap:pretty;">${LEAD}</p>`;

const btn = (primary, { full = false, fs = 14 } = {}) => {
  const base = `display:inline-flex; align-items:center; justify-content:center; box-sizing:border-box; min-height:46px; border-radius:50px; font-size:${fs}px; font-weight:600; line-height:22px; white-space:nowrap;${full ? ' width:100%;' : ''}`;
  return primary
    ? `<a href="#available-birds" style="${base} background:${CLAY_INK}; color:#ffffff; padding:12px 24px;">${CTA1}</a>`
    : `<a href="#contact" style="${base} border:2px solid rgba(250,247,244,.6); color:#faf7f4; background:transparent; padding:10px 22px;">${CTA2}</a>`;
};

const ctas = ({ justify = 'flex-start', stack = false, fs = 14 } = {}) =>
  stack
    ? `<div style="display:flex; flex-direction:column; gap:10px; width:100%;">${btn(true, { full: true, fs })}${btn(false, { full: true, fs })}</div>`
    : `<div style="display:flex; flex-wrap:wrap; gap:12px; justify-content:${justify};">${btn(true, { fs })}${btn(false, { fs })}</div>`;

const check = (stroke) =>
  `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="${stroke}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none;"><path d="M3 8.4l3.3 3.3L13 5"></path></svg>`;

// layout: 'grid2' | 'row' | 'col'
const creds = ({ layout = 'grid2', color = CRED_DK, stroke = CLAY, fs = 13, justify = 'flex-start', gap = '10px 22px' } = {}) => {
  const li = (t) => `<li style="display:flex; align-items:flex-start; gap:8px; font-size:${fs}px; font-weight:500; line-height:20px; color:${color};">${check(stroke)}<span>${t}</span></li>`;
  const wrap =
    layout === 'grid2' ? `display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:${gap};`
    : layout === 'col' ? `display:flex; flex-direction:column; gap:8px;`
    : `display:flex; flex-wrap:wrap; gap:${gap}; justify-content:${justify};`;
  return `<ul aria-label="Breeder credentials" style="${wrap}">${CREDS.map(li).join('')}</ul>`;
};

const availPill = (extra = '') =>
  `<span style="display:inline-flex; align-items:center; gap:8px; background:#ffffff; color:${FOREST}; border-radius:50px; padding:7px 15px; font-size:13px; font-weight:600; line-height:18px; white-space:nowrap; box-shadow:0 10px 30px rgba(60,30,10,.22);${extra}"><svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><circle cx="5" cy="5" r="4" fill="${CLAY_INK}"></circle></svg><span>${AVAIL}</span></span>`;

const img = (style) =>
  `<img src="hero-midland.webp" alt="${ALT}" width="800" height="600" style="display:block; object-fit:cover; ${style}">`;

const HELMET = `<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,600;1,6..72,600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
  <style>
    body { margin:0; background:${CREAM}; font-family:"IBM Plex Sans", system-ui, sans-serif; color:${INK}; }
    h1,h2,h3 { font-family: Newsreader, Georgia, serif; font-weight:600; letter-spacing:-.003em; margin:0; }
    p { margin:0; } ul { margin:0; padding:0; list-style:none; }
    a { color:${CLAY_SM}; text-decoration:none; } a:hover { color:${CLAY_INK}; }
  </style>
</helmet>`;

const doc = (width, inner) => `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
${HELMET}
<div id="root" style="width:${width}px; background:${CREAM}; display:flex; flex-direction:column;">${inner}</div>
</x-dc>
</body>
</html>
`;

const section = (style, inner) =>
  `<section aria-label="C.A.Gs African Grey breeder introduction" style="position:relative; overflow:hidden; background:${BED}; border-bottom:${RULE}; ${style}">${inner}</section>`;

// ════════════════════════════════════════════════════════════════════
// A · PAPERWORK CARD — copy on the open scrim; the photo is a cream
// document card that carries the credentials + availability.
// ════════════════════════════════════════════════════════════════════
// Breeder 2026-09-11: availability pill "almost transparent" so both Greys' faces show.
// Bottom-right sits on the empty floor fabric in every crop; a light scrim tint + text-shadow
// keeps the white text legible without hiding the photo.
const glassPill = `<span style="position:absolute; left:10px; bottom:10px; display:inline-flex; align-items:center; gap:7px; background:rgba(15,61,44,.28); color:#ffffff; border:1px solid rgba(250,247,244,.55); border-radius:50px; padding:5px 12px; font-size:12.5px; font-weight:600; line-height:18px; white-space:nowrap; text-shadow:0 1px 2px rgba(0,0,0,.55);"><svg width="8" height="8" viewBox="0 0 10 10" aria-hidden="true"><circle cx="5" cy="5" r="4" fill="${CLAY}"></circle></svg><span>${AVAIL}</span></span>`;

const paperCard = ({ photoH, credLayout, credFs = 13, pad = 14, objPos = '50% 24%' }) =>
  `<div style="display:flex; flex-direction:column; gap:14px; background:${CREAM}; border-radius:18px; padding:${pad}px; box-shadow:0 24px 60px rgba(0,0,0,.28);">
    <div style="position:relative; border-radius:12px; overflow:hidden; background:${AVI};">${img(`width:100%; height:${photoH}px; object-position:${objPos};`)}${glassPill}</div>
    <div style="display:flex; flex-direction:column; gap:10px; padding:0 4px 4px;">
      <span style="font-size:12.5px; font-weight:600; letter-spacing:.1em; text-transform:uppercase; line-height:16px; color:${CLAY_SM};">Breeder credentials</span>
      ${creds({ layout: credLayout, color: INK, stroke: CLAY_SM, fs: credFs, gap: '8px 16px' })}
    </div>
  </div>`;

const A = {
  Desktop: doc(1440, section('padding:28px 120px;',
    `<div style="display:grid; grid-template-columns:minmax(0, 1fr) 492px; gap:64px; align-items:center;">
      <div style="display:flex; flex-direction:column; gap:14px;">
        ${eyebrow()}
        ${h1(44)}
        ${lead(16, { maxw: '58ch' })}
        <div style="display:flex; padding-top:8px;">${ctas()}</div>
      </div>
      ${paperCard({ photoH: 232, credLayout: 'grid2', objPos: '50% 40%' })}
    </div>`)),
  Tablet: doc(768, section('padding:32px;',
    `<div style="display:grid; grid-template-columns:292px minmax(0, 1fr); gap:32px; align-items:center;">
      ${paperCard({ photoH: 150, credLayout: 'col', credFs: 13, pad: 12 })}
      <div style="display:flex; flex-direction:column; gap:12px;">
        ${eyebrow()}
        ${h1(30, { lh: 1.12 })}
        ${lead(14.5)}
        <div style="display:flex; padding-top:4px;">${ctas({ fs: 13.5 })}</div>
      </div>
    </div>`)),
  Mobile: doc(390, section('padding:20px 16px 28px;',
    `<div style="display:flex; flex-direction:column; gap:22px;">
      ${paperCard({ photoH: 168, credLayout: 'grid2', credFs: 12.5, pad: 12 })}
      <div style="display:flex; flex-direction:column; gap:12px;">
        ${eyebrow()}
        ${h1(27, { lh: 1.14 })}
        ${lead(14.5)}
        <div style="display:flex; padding-top:6px;">${ctas({ stack: true })}</div>
      </div>
    </div>`)),
};

// ════════════════════════════════════════════════════════════════════
// B · ARCH WINDOW — triptych: headline right-aligned into a grounded
// aviary arch; actions and credentials on the far side.
// ════════════════════════════════════════════════════════════════════
const arch = ({ w, h, grounded = true, pill = true }) => {
  const r = Math.round(w / 2) + 10;
  return `<div style="position:relative; box-sizing:border-box; width:${w + 20}px; padding:10px 10px ${grounded ? 0 : 10}px; border:1px solid rgba(250,247,244,.24); ${grounded ? 'border-bottom:none;' : ''} border-radius:${r}px ${r}px ${grounded ? '0 0' : '22px 22px'};">
      <div style="position:relative; overflow:hidden; background:${AVI}; border-radius:${r - 10}px ${r - 10}px ${grounded ? '0 0' : '14px 14px'};">${img(`width:${w}px; height:${h}px; object-position:40% 40%;`)}</div>
      ${pill ? `<div style="position:absolute; left:0; right:0; bottom:${grounded ? 16 : 22}px; display:flex; justify-content:center;">${availPill()}</div>` : ''}
    </div>`;
};

const B = {
  Desktop: doc(1440, section('padding:28px 100px 0;',
    `<div style="display:grid; grid-template-columns:minmax(0, 1fr) 380px minmax(0, 1.12fr); gap:48px; align-items:end;">
      <div style="display:flex; flex-direction:column; gap:14px; align-items:flex-end; padding-bottom:40px; align-self:center;">
        ${eyebrow(EYEBROW_DK, 'right')}
        ${h1(44, { align: 'right', maxw: '12ch' })}
      </div>
      ${arch({ w: 360, h: 380 })}
      <div style="display:flex; flex-direction:column; gap:18px; padding-bottom:36px; align-self:center;">
        ${lead(15.5, { maxw: '52ch' })}
        ${ctas()}
        <div style="border-top:1px solid rgba(250,247,244,.16); padding-top:14px;">${creds()}</div>
      </div>
    </div>`)),
  Tablet: doc(768, section('padding:28px 32px 0;',
    `<div style="display:grid; grid-template-columns:270px minmax(0, 1fr); gap:28px; align-items:end;">
      ${arch({ w: 250, h: 300 })}
      <div style="display:flex; flex-direction:column; gap:12px; padding-bottom:28px;">
        ${eyebrow()}
        ${h1(30, { lh: 1.12 })}
        ${lead(14.5)}
        <div style="display:flex; padding-top:4px;">${ctas({ fs: 13.5 })}</div>
        <div style="border-top:1px solid rgba(250,247,244,.16); padding-top:12px;">${creds({ fs: 12.5, gap: '8px 16px' })}</div>
      </div>
    </div>`)),
  Mobile: doc(390, section('padding:24px 16px 28px;',
    `<div style="display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; justify-content:center; width:100%; border-bottom:1px solid rgba(250,247,244,.24);">${arch({ w: 264, h: 224 })}</div>
      <div style="display:flex; flex-direction:column; gap:12px; align-items:center; padding-top:20px;">
        ${eyebrow(EYEBROW_DK, 'center')}
        ${h1(27, { align: 'center', lh: 1.14 })}
        ${lead(14.5, { align: 'center' })}
        <div style="display:flex; width:100%; padding-top:6px;">${ctas({ stack: true })}</div>
        <div style="width:100%; padding-top:6px;">${creds({ fs: 12.5, gap: '8px 12px' })}</div>
      </div>
    </div>`)),
};

// ════════════════════════════════════════════════════════════════════
// C · INLINE-PHOTO HEADLINE — centred, type-led; the Midland photo is a
// pill set inside the headline just before "Midland, Texas".
// ════════════════════════════════════════════════════════════════════
const glow = `<div aria-hidden="true" style="position:absolute; inset:0; background:radial-gradient(760px 300px at 50% 0%, rgba(232,96,76,.14), transparent 70%); pointer-events:none;"></div>`;

const inlinePill = (w, h) =>
  `<span style="display:inline-block; vertical-align:middle; position:relative; top:-.08em; width:${w}px; height:${h}px; margin:0 .18em; border-radius:50px; overflow:hidden; background:${AVI}; box-shadow:0 0 0 2px rgba(250,247,244,.22), 0 12px 32px rgba(0,0,0,.3);">${img(`width:100%; height:100%; object-position:50% 30%;`)}</span>`;

const h1Inline = (size, pw, ph) =>
  `<h1 style="font-size:${size}px; line-height:1.14; letter-spacing:-.012em; color:#faf7f4; text-align:center;">${H1_A.replace(' Breeder in', '')}<br>Breeder in${inlinePill(pw, ph)}${span()}</h1>`;

const ruleEyebrow = `<div style="display:flex; align-items:center; justify-content:center; gap:14px;"><span aria-hidden="true" style="width:32px; height:1px; background:rgba(159,177,171,.5);"></span>${eyebrow(EYEBROW_DK, 'center')}<span aria-hidden="true" style="width:32px; height:1px; background:rgba(159,177,171,.5);"></span></div>`;

const C = {
  Desktop: doc(1440, section('padding:24px 120px 26px;',
    `${glow}<div style="position:relative; display:flex; flex-direction:column; align-items:center; gap:14px;">
      ${ruleEyebrow}
      ${h1Inline(50, 292, 96)}
      ${lead(15.5, { align: 'center', maxw: '112ch' })}
      <div style="display:flex; padding-top:6px;">${ctas({ justify: 'center' })}</div>
      <div style="display:flex; align-items:center; gap:22px; padding-top:4px;">${creds({ layout: 'row', gap: '8px 22px' })}<span aria-hidden="true" style="width:1px; height:22px; background:rgba(250,247,244,.2);"></span>${availPill(' box-shadow:none;')}</div>
    </div>`)),
  Tablet: doc(768, section('padding:28px 32px;',
    `${glow}<div style="position:relative; display:flex; flex-direction:column; align-items:center; gap:12px;">
      ${ruleEyebrow}
      ${h1Inline(34, 176, 60)}
      ${lead(14.5, { align: 'center', maxw: '76ch' })}
      <div style="display:flex; padding-top:4px;">${ctas({ justify: 'center', fs: 13.5 })}</div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:12px; padding-top:4px;">${creds({ layout: 'row', fs: 12.5, gap: '8px 18px', justify: 'center' })}${availPill(' box-shadow:none;')}</div>
    </div>`)),
  Mobile: doc(390, section('padding:20px 16px 28px;',
    `${glow}<div style="position:relative; display:flex; flex-direction:column; align-items:center; gap:12px;">
      <div style="position:relative; width:100%; padding-bottom:16px;">
        <div style="border-radius:80px; overflow:hidden; background:${AVI}; box-shadow:0 0 0 2px rgba(250,247,244,.22);">${img('width:100%; height:136px; object-position:50% 26%;')}</div>
        <div style="position:absolute; left:0; right:0; bottom:0; display:flex; justify-content:center;">${availPill()}</div>
      </div>
      <div style="padding-top:6px;">${eyebrow(EYEBROW_DK, 'center')}</div>
      ${h1(27, { align: 'center', lh: 1.14 })}
      ${lead(14.5, { align: 'center' })}
      <div style="display:flex; width:100%; padding-top:6px;">${ctas({ stack: true })}</div>
      <div style="width:100%; padding-top:6px;">${creds({ fs: 12.5, gap: '8px 12px' })}</div>
    </div>`)),
};

let n = 0;
for (const [name, set] of Object.entries({ A, B, C })) {
  for (const [vp, html] of Object.entries(set)) {
    fs.writeFileSync(path.join(DIR, `Hero-${name}-${vp}.dc.html`), html);
    n++;
  }
}
// Main.dc.html = the leading candidate (the canvas requires one). It sits in A-Desktop's slot.
fs.writeFileSync(path.join(DIR, 'Main.dc.html'), A.Desktop);
console.log(`wrote ${n} artboards + Main.dc.html (= Hero-A-Desktop) to ${DIR}`);
