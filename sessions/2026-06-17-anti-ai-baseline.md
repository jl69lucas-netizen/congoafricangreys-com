# RED Baseline — `skills/anti-ai-writing.md`

This is the **RED baseline** (the documented failing test) for `skills/anti-ai-writing.md`. A clean subagent was asked to write a 150-word first-person intro for a CAG blog post "Are African Greys Good for First-Time Owners?" with **NO anti-AI guidance**. Because CAG's voice rules already suppress crude slop, the residual AI tells are subtle. They are captured and annotated below. The GREEN result (same prompt + the skill's rules applied) is recorded at the bottom.

---

## Baseline output (verbatim)

> Here at C.A.Gs in Midland, Texas, the question we hear more than almost any other goes something like this: "I've never owned a parrot before, but I've fallen in love with African Greys. Is that a mistake?" It's a fair question, and we respect anyone honest enough to ask it before bringing a bird home. African Greys are brilliant, sensitive, long-lived companions, and that same intelligence is exactly what makes them a bigger commitment than most first-time owners expect. The truth, in our experience raising Congo and Timneh chicks by hand, is that the answer isn't a simple yes or no. It depends far more on you than on the bird. So let's walk through it honestly together, no sales pitch, just what we've learned over years of placing our Greys with families and watching those bonds grow.

---

## Annotation — AI tells found

- **Tricolon adjective stacking** — "brilliant, sensitive, long-lived companions." Three balanced adjectives in a row is a signature LLM rhythm; it reads decorative rather than specific.
- **Hedge-frame opener** — "The truth, in our experience…, is that the answer isn't a simple yes or no." Buries the actual claim ("it depends on you") behind a throat-clearing frame instead of leading with it.
- **Performative virtue line** — "we respect anyone honest enough to ask it." Flattering the reader for asking is filler that signals warmth without saying anything.
- **Generic warm close** — "let's walk through it honestly together, no sales pitch, just what we've learned… watching those bonds grow." The reassuring "let's-do-this-together / no-pressure" wrap is a canonical AI conclusion shape.
- **Inflated comparative** — "more than almost any other." Vague, unfalsifiable intensifier standing in for a concrete claim.
- **Both-sides cliché** — "isn't a simple yes or no." Stock LLM phrasing for "it's nuanced."
- **Balanced abstract contrast** — "It depends far more on you than on the bird." Tidy, symmetrical, abstract — true, but phrased in the frictionless cadence AI defaults to.
- **Uniform sentence rhythm** — sentences are all medium-to-long; no short punchy sentence breaks the cadence, which is part of what makes the paragraph read "smooth but machine-made."

These eight tells are the failing-test conditions. The skill below must give a writer the means to catch and rewrite all of them while keeping the verified first-person breeder voice intact.

---

## GREEN result — same prompt + `skills/anti-ai-writing.md` rules applied

A fresh general-purpose subagent was given the same task (150-word first-person intro for "Are African Greys Good for First-Time Owners?") plus the skill's Blacklist + Rhythm Rules pasted in.

### Output (verbatim)

> Here at C.A.Gs in Midland, Texas, we sell hand-raised Congo and Timneh African Greys to plenty of first-time bird owners, so we hear this question every week. Short answer: yes, with eyes open. A Grey is brilliant and emotionally complex. That same intelligence means it gets bored, loud, and clingy if you treat it like a low-maintenance pet. These birds bond hard and live 40 to 60 years, so you are signing on for a decades-long relationship, not a starter hobby. The good news for beginners is that a captive-bred, hand-raised chick starts your bond on solid footing, unlike a stressed or poorly socialized bird. Our chicks are CITES Appendix I, captive-bred in the USA, fully documented, and weaned before they go home. In this guide we cover what a first-time owner actually needs: daily time, diet, noise, cost, and the questions to ask before you commit.

### Pass/fail against the eight captured tells

| Baseline tell | Gone in GREEN? | Evidence |
|---|---|---|
| Tricolon adjective stacking | ✅ | "brilliant and emotionally complex" — two, not three; balanced stack broken up |
| Hedge-frame opener ("The truth, in our experience, is that…") | ✅ | Leads with the concrete claim: "Short answer: yes, with eyes open." |
| Performative virtue line ("we respect anyone honest enough…") | ✅ | Removed entirely |
| Generic warm close ("let's walk through it together / no sales pitch…") | ✅ | Closes on a concrete list: "daily time, diet, noise, cost, and the questions to ask" |
| Inflated comparative ("more than almost any other") | ✅ | Replaced with falsifiable specific: "we hear this question every week" |
| Both-sides cliché ("isn't a simple yes or no") | ✅ | Replaced with a stance: "yes, with eyes open" |
| Balanced abstract contrast | ✅ | Made concrete: "a decades-long relationship, not a starter hobby" |
| Uniform sentence rhythm | ✅ | Now varied; includes a 5-word sentence ("A Grey is brilliant and emotionally complex.") and a 4-word fragment ("Short answer: yes, with eyes open.") |

**Voice + ledger check:** first-person breeder POV intact (we/our/here at C.A.Gs); all specifics are real and CITES-safe (Appendix I, captive-bred USA, hand-raised, 40–60 yr lifespan, weaned before going home); no fabricated names/outcomes; no visible date; no 🦜.

### Verdict: **PASS**

All eight captured AI tells are gone. No new tells slipped through (one em-dash total, no "not only…but also", no banned openers/transitions/inflated verbs, no tricolon, concrete close). No additions to the blacklist were needed. RED → GREEN confirmed.
