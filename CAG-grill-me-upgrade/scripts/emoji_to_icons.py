#!/usr/bin/env python3
"""Site-wide emoji -> consistent Feather-style line-icon sweep (2026-06-03).
Replaces decorative pictograph emoji with inline SVGs that inherit the call
site's size (width/height=1em) and color (stroke=currentColor). Keeps the
canonical contact set in contact contexts and keeps text glyphs (checkmarks,
stars, X) as-is. Idempotent: re-running finds nothing to change."""
import os, re, sys

W = ('<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" '
     'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
     'stroke-linejoin="round" style="display:inline-block;vertical-align:-0.125em" '
     'aria-hidden="true">{}</svg>')

P = {
 'clipboard':'<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>',
 'file-text':'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/>',
 'file':'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>',
 'home':'<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
 'flask':'<path d="M9 3h6"/><path d="M10 3v6l-4.6 9.2A1.5 1.5 0 0 0 6.7 21h10.6a1.5 1.5 0 0 0 1.3-2.8L14 9V3"/>',
 'activity':'<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
 'dollar':'<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'users':'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'lock':'<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'ruler':'<path d="M3 17 17 3l4 4L7 21z"/><line x1="8" y1="8" x2="10" y2="10"/><line x1="11" y1="5" x2="13" y2="7"/><line x1="5" y1="11" x2="7" y2="13"/>',
 'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 'landmark':'<line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 21 8 3 8"/>',
 'bell':'<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/>',
 'dna':'<path d="M8 3c0 4.5 8 4.5 8 9s-8 4.5-8 9"/><path d="M16 3c0 4.5-8 4.5-8 9s8 4.5 8 9"/><line x1="9" y1="6.5" x2="15" y2="6.5"/><line x1="9.5" y1="12" x2="14.5" y2="12"/><line x1="9" y1="17.5" x2="15" y2="17.5"/>',
 'alert':'<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
 'cross-box':'<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/>',
 'globe':'<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 'award':'<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
 'graduation':'<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1 2.7 2 6 2s6-1 6-2v-5"/>',
 'calendar':'<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
 'scale':'<path d="M12 3v18"/><path d="M5 7h14"/><path d="M5 7 2 13a3 3 0 0 0 6 0z"/><path d="M19 7l3 6a3 3 0 0 1-6 0z"/><path d="M8 21h8"/>',
 'egg':'<path d="M12 3c-3.5 0-6 5-6 9a6 6 0 0 0 12 0c0-4-2.5-9-6-9z"/>',
 'ban':'<circle cx="12" cy="12" r="10"/><line x1="4.9" y1="4.9" x2="19.1" y2="19.1"/>',
 'flag':'<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
 'search':'<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
 'brain':'<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44A2.5 2.5 0 0 1 4 17.5 2.5 2.5 0 0 1 3.5 13 2.5 2.5 0 0 1 5 8.5 2.5 2.5 0 0 1 7 4.06 2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5"/>',
 'message':'<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8z"/>',
 'feather':'<path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/>',
 'trend-up':'<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
 'trend-down':'<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
 'bar-chart':'<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>',
 'gift':'<polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/>',
 'heart':'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
 'smile':'<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>',
 'cpu':'<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
 'book':'<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 'id-card':'<rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="8" cy="12" r="2"/><line x1="13" y1="10" x2="18" y2="10"/><line x1="13" y1="14" x2="18" y2="14"/>',
 'clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
 'tag':'<path d="M20.6 13.4 12 22l-9-9V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
 'arrow-down':'<line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/>',
 'zap':'<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
 'bulb':'<path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.1 14c.2-1 .7-1.7 1.4-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.8 1.2 1.5 1.4 2.5"/>',
 'bookmark':'<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
 'chevron':'<polyline points="9 18 15 12 9 6"/>',
 'leaf':'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.85-5.4 5.1-6"/>',
 'pill':'<path d="M10.5 20.5 3.5 13.5a4.95 4.95 0 0 1 7-7l7 7a4.95 4.95 0 0 1-7 7z"/><line x1="8.5" y1="8.5" x2="15.5" y2="15.5"/>',
 'camera':'<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
 'pointer':'<path d="M3 3l7.07 16.97 2.51-7.39 7.39-2.51z"/><path d="m13 13 6 6"/>',
 'user-x':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="17" y1="8" x2="22" y2="13"/><line x1="22" y1="8" x2="17" y2="13"/>',
 'image':'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>',
 'truck':'<rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
 'mail':'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/>',
 'plane':'<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
 'car':'<path d="M5 17H3v-5l2-5h12l2 5v5h-2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><line x1="6" y1="7" x2="18" y2="7"/>',
 'pin':'<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'sparkle':'<path d="M12 3l1.9 5.6L19.5 10l-5.6 1.9L12 17l-1.9-5.1L4.5 10l5.6-1.4z"/>',
 'phone':'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
}
def svg(n): return W.format(P[n])

# ✅ (colorful emoji, U+2705) -> green check-circle line icon. Kept green (not
# currentColor) because it is a positive "included / yes" marker. NOTE: this
# overrides DESIGN.md's canonical-set allowance of ✅ in favor of the
# user-approved full line-icon consistency sweep (2026-06-03). The text glyphs
# ✔ ✗ ★ are intentionally NOT touched (kept as list/rating markers).
CHECK = ('<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" '
         'stroke="#2D6A4F" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round" style="display:inline-block;vertical-align:-0.125em" '
         'aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
         '<polyline points="8 12.5 11 15.5 16.5 9"/></svg>')

# Decorative emoji -> icon (applied to ALL files). Excludes canonical contact set.
EMO = {
 '📋':'clipboard','📜':'file-text','📄':'file','🏠':'home','🏡':'home','🏘':'home',
 '🔬':'flask','🩺':'activity','💸':'dollar','💰':'dollar','💲':'dollar',
 '🤝':'users','🔒':'lock','📏':'ruler','🛡':'shield','🏛':'landmark','🔔':'bell',
 '🧬':'dna','⚠':'alert','🏥':'cross-box','🌍':'globe','🌐':'globe','🌎':'globe',
 '🏅':'award','🏆':'award','🎓':'graduation','📅':'calendar','⚖':'scale','🥚':'egg',
 '📵':'ban','🚫':'ban','🚩':'flag','🔍':'search','🔎':'search','🧠':'bulb',
 '🗣':'message','💬':'message','🐦':'feather','📈':'trend-up','📊':'bar-chart','📉':'trend-down',
 '✨':'sparkle','🎀':'tag','🍼':'clock','🎨':'smile','💉':'cpu','🤲':'heart',
 '📚':'book','📖':'book','🪪':'id-card','🕒':'clock','⏱':'clock','🆓':'tag',
 '⬇':'arrow-down','🚀':'zap','💡':'bulb','📌':'bookmark','🔹':'chevron',
 '🎭':'smile','🥦':'leaf','🌿':'leaf','💊':'pill','🖱':'pointer','🚨':'alert',
 '👻':'user-x','🖼':'image','🏷':'tag','🚛':'truck','🚚':'truck','📩':'mail','📧':'mail','📨':'mail',
 '📷':'camera','📸':'camera',
 # Pictograph forms of the canonical set — convert site-wide to line icons for
 # full visual consistency (user-approved full sweep, 2026-06-03).
 '📍':'pin','✈':'plane','🚗':'car','⏳':'clock','📞':'phone','✉':'mail','🕐':'clock',
}
CANON = {}        # (folded into EMO — full site-wide sweep)
CANON_FILES = set()

# set:html render-site conversions (escaped {x.icon}/{b} -> set:html)
RENDER = {
 'TrustBar.astro':[('<span class="text-2xl" aria-hidden="true">{b.icon}</span>',
                    '<span class="text-2xl" aria-hidden="true" set:html={b.icon}></span>')],
 'cag-library/SplitHero.astro':[('<div class="text-[20px]">{t.icon}</div>',
                                 '<div class="text-[20px]" set:html={t.icon}></div>')],
 'cag-library/ScamAwareness.astro':[('<div class="text-clay text-2xl">{f.icon}</div>',
                                     '<div class="text-clay text-2xl" set:html={f.icon}></div>')],
 'cag-library/MeetTheTeam.astro':[('{m.bullets.map(b => <li>{b}</li>)}',
                                   '{m.bullets.map(b => <li set:html={b}></li>)}')],
 'infographics/ComparisonInfographic.astro':[('<span style="font-size:16px;flex-shrink:0;width:20px;text-align:center;">{item.icon}</span>',
                                              '<span style="font-size:16px;flex-shrink:0;width:20px;text-align:center;" set:html={item.icon}></span>')],
 'pages/where-to-buy-african-greys-near-me/index.astro':[('<span class="text-2xl mt-0.5">{item.icon}</span>',
                                                          '<span class="text-2xl mt-0.5" set:html={item.icon}></span>')],
 'pages/african-greys-for-sale-with-health-guarantee/index.astro':[('<span class="text-2xl mt-1">{doc.icon}</span>',
                                                                    '<span class="text-2xl mt-1" set:html={doc.icon}></span>')],
 'pages/trusted-african-grey-parrot-breeders/index.astro':[('<span class="text-2xl mt-0.5">{item.icon}</span>',
                                                            '<span class="text-2xl mt-0.5" set:html={item.icon}></span>')],
}
VS = '[️︎‍]*'  # trailing variation selectors / ZWJ
FAMILY = re.compile('(?:[\U0001F466-\U0001F469]'+VS+'){2,}')  # man/woman/girl/boy cluster

def rel(p): return p.replace('src/components/','').replace('src/','')

def process(path):
    s0 = open(path, encoding='utf-8').read(); s = s0
    r = rel(path)
    for a,b in RENDER.get(r, []): s = s.replace(a,b)
    if r in [k for k in RENDER] or path.endswith(('.astro','.html')):
        pass
    # family cluster first (one users icon for the whole run)
    s = FAMILY.sub(svg('users'), s)
    s = re.sub('✅'+VS, CHECK, s)  # colorful check emoji -> green check-circle
    # decorative emoji
    for e,n in EMO.items():
        s = re.sub(re.escape(e)+VS, svg(n), s)
    # canonical set, scoped
    if r in CANON_FILES:
        for e,n in CANON.items():
            s = re.sub(re.escape(e)+VS, svg(n), s)
    if s != s0:
        open(path,'w',encoding='utf-8').write(s); return True
    return False

changed=[]
for root,_,files in os.walk('src'):
    for f in files:
        if f.endswith(('.astro','.html')):
            if process(os.path.join(root,f)): changed.append(os.path.join(root,f))
print(f"Changed {len(changed)} files:")
for c in sorted(changed): print("  ",rel(c))
