

STRATEGY AGENT, Read and verified everything. Confirmation first, then the plan for how we do it.

* YOU MUST USE ALL THE SPECIFIED COMPONENTS FOR THE PAGE BELOW. DO NOT INHERIT ANY CROSSOVER FROM THE CvC, CvM, or MvF pages. I have provided all component links to check and see the components for yourself so you know what I am saying.   
* HERO C — Photo \+ Decision Bar: two "Choose a Congo/Timneh if…" cards inside the hero. Fastest to the decision; pushes the H1 lower and duplicates section 4's Quick Answer.  
*   
* 🎨 Hero lab is live in your preview panel (`hero-lab.html`) — three heroes, each rendered at desktop 1200px and in a true 375px phone frame, all following your spec (Congo LEFT / Timneh RIGHT,

\- (recorded in `DECISIONS.md`) and Screen 2 is now in your preview panel (`core-components-lab.html`) — pushed to main.

\-in `DECISIONS.md`, with a note that your 8B gradient-fade seam is a deliberate Set-B divergence from the sitewide hairline seam) and Screen 3 is now in your preview panel (`cards-lab.html`) — all images verified live, pushed to main.

## ✅ The 22 rules (0–21) — YOU MUST FOLLOW THESE RULES. 

Rule 0 — Component set for THIS page (locked, no visual companion):

HERO C (photo \+ decision-bar, two choose-if cards) · new counter-snippet style (not the homepage/CvT set) · TOC 1C bordered grid · mobile jump 2B underline tabs · Key Takeaways 3C columns · Quick Answer 4B band recolored clay/orange (not forest — you flagged it competes with hero) · Compare E desktop \+ mobile tab-pill but a new flow distinct from CvT/homepage · Scorecard 6B dots or AI infographic (open — see Q) · FAQ 7C hybrid top-3 open · Seam 8A hairline+logo · Buttons 9B all-pill · Newsletter 10A+B+C all three, positioned exactly like MvF (top/mid/bottom, short copy) · Breeder card 11C byline chip (enhanced) · Compare-birds stat cards 12B/12C green-header (modernized) · Available cards 13B horizontal-mini \+ 5 badges (CITES · PCR DNA-Sexed · Vet Certified · PBFD & APV Screened · Fully Weaned) · Breeding-pair+eggs 14B duo-image split (pair $3,000, eggs link-out no invented price, stacks on mobile) · Shipping 15B journey timeline \+ $200 deposit step, provided shipping images · Health 16B per-risk minis · 17B feature pull-quote · Blog 18B horizontal · same contact form.

Rules 1–21 — structure, content & QA gates to avoid unnecessary duplicates; do not carry from CvC, CvT \+ MvF (Use the research data, headers, etc below):

* Structure: every H2/H3 carries an image; full H1→H6 outline approved *before code*, no skips, ≥5 H5 and ≥5 H6; 21–24 H2 sections, 5,000–6,000 words; conversational hybrid question+entity headers, unique per page; 4–8 .cag-seam dividers; no visible dates.  
* Hero/visual fixes: full-bleed homepage-height hero, copy left / two portraits center-right \+ vs roundel, mobile stacks images first, sentence-case clay eyebrow; push birds back from the VS circle (portrait \= clip-mask \+ zoom/translate; landscape \= object-position) — the MvF Kent/Evie fix; .portrait modifier for square OGs; taller 4:3 image window on mobile; responsive \-760.webp siblings \+ srcset on every infographic.  
* Content moat: page-specific counter snippet (never the homepage four); real reviews only; bird cards 5 badges; 6–8+ diverse external authority domains mid-sentence; first-person voice; anti-AI grep clean; Style-2 humor ≤1/section, never on health/legal; non-commodity breeder markers.  
* Schema/tech: FAQPage \+ Article, no page-level BreadcrumbList (component emits it); 4-part title ending C.A.Gs – \<LSI\>; sticky 96px offsets; contrast floors (\#b04228 fills white 5.7:1, verdict cells \#2D6A4F); links start/mid-sentence never at end.  
* Anti-duplication (binding gate): dup\_content\_audit.py ≥12-word cross-page check \= hard FAIL; this page claims its own 7-location pill set \+ unique variant anchors (CvT owns TX/FL/NY/LA/Chicago/GA/NC; MvF owns AZ/PA/OH/Miami/Dallas/WA/NJ — cockatoo gets a fresh set).  
* Final gate: astro build → verify in dist/ → final\_page\_audit.py \--comparison PASS/PASS-WITH-WARNINGS → keyword-verifier \+ anti-AI \+ non-commodity \+ Lighthouse warm-median-of-3.

## 📋 The build sequence (exact same steps as CvC, CvT & MvF)

1. Sprint 0 — deep research (this session): 30-competitor registry sweep \+ fresh top-7 Google/Bing/Reddit/YouTube/Facebook/Pinterest/forum/Instagram → SERP snapshot, competitor reverse-engineering, content gap.  
2. Fan-out → keyword universe \+ entity map \+ NLP/LSI library.  
3. Sprint 0.5 Upgraded Grill Me Skill Invoke for questions about the page/build, etc.  
4. Deliverables for your confirmation: angles \+ framework-per-section \+ keyword variations \+ entity map \+ full H1→H6 outline \+ A/B/C section distribution matrix \+ Gemini prompt pack with SEO filenames (saved to sessions/comparison-research/african-grey-vs-cockatoo/).  
5. You: confirm angles/framework/keywords/entities \+ generate & drop the AI infographics.  
6. Then (next session): build to disk → gates → deploy.

No code gets written until step 4 is signed off.

THE PAGE MUST MEET/PASS ALL THESE CHECKS, and you must show proof that it was done.

All 11 tasks done, verified in-browser (desktop \+ mobile), gate-passed, deployed, verified live, and saved for reuse.

## What shipped — /african-grey-vs-cockatoo/ finishing pass

| \# | Task | Result |
| :---- | :---- | :---- |
| 1 | Move top newsletter | Now sits in the S8→S9 gap (breaks the two long image-less sections: health-risks ↔ contrafreeloading) |
| 2 | Move bottom newsletter | Now between CITES and Shipping (removed from below the form — killed the form dup); copy re-matched to CITES/shipping context |
| 3 | Slim middle newsletter | New opt-in compact prop on NewsletterV2 — shorter image, tighter padding, headline down from 36px→24px, trimmed copy (homepage untouched) |
| 3b | Swap grey close-up → Moluccan+Citron cockatoo | New .portrait-tall (3:4, medium), both crested heads visible |
| 4 | Swap CITES photo → Mark-with-grey-and-Amazon | New .photo43 (4:3, medium, \+srcset); alt written to what's actually visible |
| 5 | TOC \+ jump rail polish | Flex rows, tabular clay numerals 01–24, hairlines, hover indent — clean on all devices |
| 6 | Card heights \+ Match cards | Species/bird/pair crops taller with head-biased object-position; Match cards get clay ticks \+ hover, 5th card spans full width |
| 7 | Typography parity | h1 28px / h2 20px on mobile, newsletter 20px — no oversized headers; no horizontal overflow |
| 8 | Quick Answer wrong component | Rebuilt to the matrix-assigned 4B (clay snippet \+ green/clay Choose-if cards) — it had silently inherited the flagship's plain green box |
| 9 | Compact | Seams 40→28px, body padding trimmed, two seams removed |
| 10 | Pair/eggs images | 210→250px; pair heads up, candled eggs down — both read clearly |
| 11 | Live pass (last session's open item) | In-browser preview done (desktop+mobile screenshots) and deployed-URL verified live: Choose-if cards, both photo swaps, relocated newsletter all confirmed, old image gone |

Gate: final\_page\_audit.py \--comparison → PASS-WITH-WARNINGS (H1:1 H2:26 H3:41 H4:15 H5:8 H6:7, Organization \+ FAQPage) — same three soft WARNs the flagship carries, no regression.  
Deployed: commits 8f12ec0 (page) \+ 87c0124 (log), both live on main → Cloudflare.  
Saved for reuse: `sessions/2026-07-09-grey-vs-cockatoo-finishing-pass.md` (full patterns) \+ memory pointer, so the remaining spokes (macaw, amazon, breeders, hub) can reuse the compact prop, the two image-fit classes, the QA-4B check, and the head-crop rule.

SEE ALL RESEARCH DATA BELOW. Read all, and then confirm you understand and can verify from 1-6, etc.  
1\.

To optimize your page **"African Grey vs. Macaw"** for SEO, AIO (AI Optimization), AEO, and GEO, you must leverage the specialized biomechanical, behavioral, and scientific data provided in the sources that your competitors often overlook.

### **1\. Competitive Landscape Analysis (Top 7 Competitors)**

| Competitor | Strategy & Angle | Why They Rank |
| ----- | ----- | ----- |
| **PetHelpful** | **Experiential Narrative:** Uses a direct comparison of "Gracie" (Macaw) vs. "Bubba" (Grey). | High engagement through relatable stories and clear, point-by-point winning categories. |
| **Clawmate** | **Programmatic Data:** Uses 5-point scales for size, trainability, and shedding. | Structural relevance and predictable URL paths that search crawlers easily index. |
| **Squawk Shop** | **Biomechanical Safety:** Focuses on bite force (PSI) and safety protocols. | High E-E-A-T for "risk-mitigation" search intent; they provide the "Newton" measurements LLMs love. |
| **Hepper** | **Programmatic Broadness:** Uses "At a Glance" parameter cards for rapid indexing. | High topical authority in general avian education and formal taxonomical classification. |
| **ZuPreem** | **Gamified Authority:** Uses "Tournament Brackets" to decide the "Best Pet Bird". | Social validation via owner polls and strong veterinary backing (Dr. Laurie Hess). |
| **BirdTricks** | **Behavioral Modification:** Focuses on "lifestyle fit" and early-stage owner education. | Strong author credentials (Patty Jourgensen) and deep internal linking to training products. |
| **Seven Bird** | **E-commerce Comparison:** Provides a detailed physical and nutritional breakdown for buyers. | Comprehensive care requirements (space, diet, cost) linked directly to purchase funnels. |

---

### **2\. The Strategy: SEO, AEO, and GEO**

To outrank these competitors and get cited by AI (ChatGPT, Perplexity, Gemini), implement the following:

* **GEO Strategy (Fact-Density):** LLMs prioritize "fact-dense" structured data. Place a **Markdown comparison table** at the top of the page comparing **Measured Bite Force (Newtons)**, **Estimated PSI**, and **Ecological Niche**.  
* **AEO Strategy (Conversational Headers):** Use headers that mirror voice search queries. Below each header, provide a **40-60 word concise answer** to capture "People Also Ask" (PAA) snippets.  
* **AIO Strategy (Token-Efficient Semantic Clusters):** Group content by "Clusters" (Health, Behavior, Safety) using LSI terms like **"Psittacine dander"** and **"Contrafreeloading"**.

---

### **3\. Entity and Keyword Blueprint**

#### **Primary Entities to Include:**

* **Species:** *Psittacus erithacus* (Congo Grey), *Ara ararauna* (Blue and Gold), *Ara macao* (Scarlet), *Ara chloropterus* (Green Wing), *Anodorhynchus hyacinthinus* (Hyacinth Macaw).  
* **Experts:** Dr. Irene Pepperberg (Intelligence), Patty Jourgensen (Behavior), Dr. Laurie Hess (Nutrition).

#### **LSI & NLP Keywords (The Competitor Gap):**

* **Technical/Biomechanical:** "Zygodactyl feet," "upper bill force," "measured Newtons vs estimated PSI," "beak contact patch".  
* **Behavioral Pathology:** "Contrafreeloading," "feather destruction," "hormonal aggression," "screaming tantrums," "separation anxiety".  
* **Health:** "Hypocalcemia," "Atherosclerosis," "UV-B sunlight requirements," "Vitamin D synthesis".

---

### **4\. Recommended Page Sections & Subsections**

#### **H1: African Grey vs. Macaw: The Ultimate Companion Comparison**

* **The "At a Glance" Table:** Include weight, lifespan (40-80 years), and noise levels (Macaws are significantly louder).

#### **H2: Biomechanical Risk: The "Walnut vs. Popsicle Stick" Comparison**

* Provide the unique "Home Safety Test" comparison: A **Macaw’s bite** is like cracking a walnut with metal pliers (\~539 N), whereas a **Grey’s bite** is like snapping a wooden popsicle stick (\~61-96 N).

#### **H2: Macaw Species Subsections: Which "Ara" Fits You?**

* **African Grey vs. Blue and Gold Macaw:** Compare the "Energizer Bunny" energy of the B\&G to the "laid-back, chatty" nature of the Grey.  
* **African Grey vs. Scarlet Macaw:** Focus on the "vibrancy vs. intellect" angle; Scarlets are gifts of nature in appearance but Greys lead in contextual language.  
* **African Grey vs. Green Wing Macaw:** Address the size disparity; Green Wings are among the largest, while Greys are "the perfect medium size".

#### **H2: The "Lifecycle Mismatch" & Succession Planning**

* **Unique Content:** Address the fact that these birds often outlive their owners. Include a "Legacy Planning" guide for parrots that may see up to 20 homes in a lifetime.

#### **H2: Nutritional Nuances: Calcium and Fat Requirements**

* Explain that **Macaws need higher fat** (nuts like Brazil nuts and macadamias), while **Greys need higher calcium** and direct UV-B light to prevent seizures.

---

### **5\. Essential Visuals to Create**

1. **Bite Force Matrix:** A visual graph showing Macaw vs. Grey vs. Human (150-200 PSI) to emphasize safety.  
2. **"Which Bird?" Flowchart:** A decision tree based on **Apartment Living** (Grey is better) vs. **Chaotic Homes** (Macaws handle chaos better).  
3. **The Enrichment Circle:** A diagram showing how **Contrafreeloading** (giving the beak a job) prevents **Feather Plucking**.  
4. **Species Comparison Infographic:** Photos of the Grey subspecies (Congo vs. Timneh) vs. the primary Macaw species (Scarlet, B\&G, Green Wing).

2\.  
MOST IMPORTANT PART/RULE OF THE BUILD, YOU MUST CONFIRM YOU UNDERSTAND HOW TO IMPLEMENT THIS EXACT STRATEGY.

To optimize your page for SEO, AEO, and GEO, you must leverage the highly specific scientific data and behavioral insights found in the sources that general pet sites often miss. This strategy focuses on established entities and "gap" keywords to ensure your content is indexed as the definitive authority.

### **1\. Keyword Targeting Strategy by Intent**

#### **Informational Intent (Early Research)**

* **Primary Keywords:** "African Grey vs Macaw," "Macaw vs African Grey," "best large parrot for pets".  
* **Concurrent Keywords:** "Talking ability," "parrot intelligence," "lifespan," "noise level," "bird temperament".  
* **Low-Competition/Gap Keywords (Target These):** "Old World vs New World parrot social dynamics," "independent bonding vs velcro birds," "parrots for quiet households," "which parrot outlives owners".

#### **Analytical Intent (Comparison & Data)**

* **Primary Keywords:** "Macaw bite force PSI," "African Grey vs Macaw size comparison," "Scarlet Macaw vs Congo African Grey".  
* **Concurrent Keywords:** "Measured Newtons vs PSI," "beak contact patch," "gram weight comparison," "Appendix I CITES species".  
* **Gap Keywords:** "Bite force of Ara ararauna," "hypocalcemia in African Greys vs Macaws," "psittacine dander levels," "UV-B requirements for calcium absorption".

#### **Transactional & Risk-Mitigation Intent (Near Purchase)**

* **Primary Keywords:** "African Grey for sale," "Macaw price," "how to stop parrot plucking".  
* **Concurrent Keywords:** "USDA AWA licensed breeder," "CITES documentation," "fully weaned baby parrots," "hand-raised birds".  
* **Gap Keywords:** "Generational succession planning for parrots," "parrot legacy planning," "contrafreeloading enrichment toys," "Teflon toxicity safety guide".

---

### **2\. Primary Entities and Semantic SEO Terms**

AI engines like Perplexity and ChatGPT prioritize content that maps relationships between recognized entities.

* **Taxonomical Entities:** *Psittacus erithacus* (Grey), *Ara ararauna* (Blue & Gold), *Ara macao* (Scarlet), *Ara chloropterus* (Green-winged), *Anodorhynchus hyacinthinus* (Hyacinth).  
* **Expert Entities:** **Dr. Irene Pepperberg** (intelligence), **Patty Jourgensen** (behavior), **Dr. Laurie Hess** (nutrition), **Pamela Clark** (avian consultant).  
* **LSI (Latent Semantic Indexing) Terms:** "Velcro birds," "powder down," "psittacine dander," "zygodactyl feet," "upper bill force," "contextual language use," "separation anxiety".  
* **Behavioral Pathology Terms:** "Contrafreeloading," "feather destruction," "self-mutilation," "hormonal aggression," "eye pinning," "screaming tantrums".

---

### **3\. Conversational Header Strategy (AEO & GEO)**

You requested all headers (H1-H6) to be in conversational FAQ format. Here are two options:

#### **Option 1: Direct Problem-Solving FAQ (Recommended)**

* **H1:** Should I get an African Grey or a Macaw as my lifetime companion?  
* **H2:** Which parrot is better for apartment living, a Grey or a Macaw?  
* **H3:** Do African Greys or Macaws talk more clearly?  
* **H4:** How strong is a Macaw's bite force compared to an African Grey?  
* **H5:** Can people with allergies safely own a Macaw?  
* **H6:** Who will take care of my parrot after I die?

**Reason why this is RECOMMENDED:** This format mirrors exact user voice search patterns and "People Also Ask" (PAA) boxes. It provides "fact-dense" triggers for AI models to extract direct answers.

---

### **4\. Hybrid Headers: Keyword \+ Entity/Terms**

This is what I would actually implement.

To satisfy both SEO (keywords) and E-E-A-T (authority via entities), use "Two-Part" or "Hybrid" headers.

#### **Option B: Question \+ Behavioral Term (The "Outcome" Angle) \- RECOMMENDED**

* Examples  
* **H2:** Which is the ultimate "Velcro Bird"? (Comparing the affection styles of Macaws and Greys).  
* **H2:** Why is my bird plucking feathers? (How **contrafreeloading** prevents behavioral pathology).

## **Hybrid Entity \+ Question Headers**

Pattern

**Keyword \+ Entity \+ Question \+ Intent**

### **Why this is the strongest approach**

This format combines four powerful SEO signals in a single heading:

1. **Primary keyword** ("African Grey vs Macaw")  
2. **Secondary entity** ("Talking Ability", "Personality", "Cost", "Noise Levels")  
3. **Natural language question** ("Which Bird Is...", "Can...", "How...")  
4. **User intent qualifier** ("for Beginners", "for Families", "Over a Lifetime", "in Apartments")

It aligns with how people search, how Google organizes comparison topics, and how AI systems retrieve and quote authoritative answers. It also creates clear semantic relationships that can improve both traditional rankings and citations in AI-generated responses.

**Reason why Option B is RECOMMENDED:** It combines a high-volume search question with a "hook" term (e.g., velcro bird, contrafreeloading) that adds immediate depth and curiosity. This strategy signals to search engines that the page is not just a summary but a specialized resource.

---

### **5\. Strategy to Outrank Competitors**

1. **Lead with Structured Data:** Place a **Markdown comparison table** immediately after the H1 comparing **Measured Bite Force (N)**, **PSI**, and **Noise Decibels (dB)**. Competitors like Hepper use general cards; you will win by being biomechanically specific.  
2. **Address the "Lifecycle Mismatch":** Create a dedicated section on **generational succession planning**. Most competitors ignore the 40–80 year lifespan reality; addressing this builds massive trust and targets high-anxiety long-tail queries.  
3. **Include the "Home Safety Test":** Use the "Pliers vs Walnut" and "Popsicle Stick Snap" analogies to make technical bite-force data relatable.  
4. **Species-Specific Subsections:** For your "African Grey vs Scarlet Macaw" and "African Grey vs Green Wing" sections, use a "Causal Link" approach: explain how the bird's size (Green Wing) dictates specific financial costs for toy destruction ($200-$300/month).  
5. **AEO Summary Blocks:** Below each H2, include a **40-60 word concise summary** that answers the question directly. This is the optimal length for Google and AI chatbots to cite you as a source.

3\.

For your **African Grey vs. Macaw** page, a **Blended Framework** is the most effective way to satisfy both human readers (who want emotional and lifestyle matching) and AI engines (which prioritize structured data and entity relationships).

This strategy transitions through different frameworks as the user moves down the page, moving from broad attention to technical data, and finally to high-trust action.

### **1\. The Hero Section: AIDA (Attention) Framework**

* **Header Type:** Conversational H1 ("Should I get an African Grey or a Macaw as my lifetime companion?").  
* **Goal:** Capture the "Attention" phase of AIDA with a vibrant visual of both species and a "hook" regarding the 40–80 year commitment.  
* **AEO Component:** A 40–60 word summary block answering the H1 immediately below it.

### **2\. The "At a Glance" Section: Entity-Based GEO Framework**

* **Framework Focus:** Generative Engine Optimization (GEO). AI models like Perplexity and ChatGPT prioritize fact-dense, structured data.  
* **Content:** A high-density **Markdown Comparison Table** including scientific names (*Psittacus erithacus* vs. *Ara ararauna*), weight (grams), noise levels (dB), and CITES status.  
* **Why it works:** It establishes "structural relevance" and makes your data the easiest for AI to parse and cite as a primary source.

### **3\. The Behavioral Deep Dive: Causal Link Framework**

* **Framework Focus:** Explaining the *why* behind the *what*.  
* **Content:**  
  * **Intelligence:** Link **Dr. Irene Pepperberg's** research on Greys to the owner's need for advanced puzzle toys.  
  * **Contrafreeloading:** Explain how the innate drive to work for food prevents **feather plucking**.  
  * **Bonding Style:** Compare the "Independent Observer" (Grey) vs. the "High-Energy/Velcro" nature of the Macaw.

### **4\. Biomechanical Risk: Risk-Mitigation Framework**

* **Framework Focus:** Addressing safety concerns for prospective owners.  
* **Content:** A "Bite Force Matrix" comparing **Measured Newtons vs. Estimated PSI**.  
* **Visual Hook:** Use the **"Home Safety Tests"** (Popsicle Stick Snap vs. Walnut Crack with Pliers) to make technical data relatable.

### **5\. Lifestyle Matching: Benefit/Outcome-Led Framework**

* **Framework Focus:** Transitioning from "Interest" to "Desire" by showing the user their future life.  
* **Content:** "Choose a Macaw if you want a vibrant 'Energizer Bunny'..." vs. "Choose a Grey if you prefer a 'laid-back, chatty' companion...".  
* **AEO Snippet:** A dedicated subsection on "Which is better for apartment living?" (spoiler: the Grey).

### **6\. Macaw Species Subsections: Taxonomy Framework**

* **Framework Focus:** Entity depth for long-tail SEO.  
* **Content:** Bulleted breakdowns for **Scarlet**, **Blue & Gold**, and **Green Wing Macaws**.  
* **Key Differentiator:** Include the "Beak Contact Patch" size for each to show how it affects toy destruction costs ($200-$300/month).

### **7\. The Lifecycle Mismatch: Purpose/Legacy Framework**

* **Framework Focus:** Building massive E-E-A-T (Trustworthiness) by addressing the rehoming crisis.  
* **Content:** A "Generational Succession Plan" guide. Discuss the reality that these birds often outlive their owners and may see 20+ homes in a lifetime.  
* **Why it outranks competitors:** Most sites avoid the "negative" reality of ownership; addressing it positions you as a high-authority consultant, not just a seller.

### **8\. Nutritional Nuances: Technical/Expert-Led Framework**

* **Framework Focus:** Professional advice to prevent health crises.  
* **Content:**  
  * **African Greys:** Focus on UV-B light requirements for **Vitamin D synthesis** and preventing **Hypocalcemia**.  
  * **Macaws:** Focus on the requirement for higher fat content (Brazil nuts and Macadamias).

### **9\. Closing & Contact: AIDA (Action) \+ Trust Framework**

* **Framework Focus:** Final conversion.  
* **Content:** High-visibility trust signals: **USDA AWA Licensed**, **CITES Appendix I Compliant**, and **Hand-Raised/Fully Weaned** status.  
* **The Action:** A clear "Inquire About a Bird" or "Book a Behavioral Consultation" button.

4\.

Yes. This is actually where **modern SEO (2026)** has shifted dramatically.

For **Google \+ AI Overviews \+ ChatGPT \+ Gemini \+ Claude \+ Perplexity**, you're no longer writing just for keyword matching. You're writing to satisfy **entity retrieval**, **question answering**, **semantic completeness**, and **knowledge graph relationships**.

For **African Grey vs Macaw**, I'd design the page as an **Entity-First Conversational Knowledge Document**, not a traditional blog post.

---

# **1\. Primary Search Intent**

## **Core Intent**

Commercial Investigation

"I want to know which parrot is right for me."

---

## **Supporting Intent**

* Learn differences  
* Compare intelligence  
* Compare personalities  
* Compare costs  
* Compare talking ability  
* Compare lifespan  
* Compare ownership  
* Compare suitability

---

# **2\. Keyword Universe**

Instead of targeting one keyword...

Target an entire keyword ecosystem.

---

## **PRIMARY KEYWORDS**

African Grey vs Macaw

Macaw vs African Grey

African Grey or Macaw

Macaw or African Grey

African Grey Parrot vs Macaw

Macaw comparison

African Grey comparison

---

## **SECONDARY KEYWORDS**

best pet parrot

best companion parrot

best talking parrot

most intelligent parrot

African Grey talking

Macaw talking

Macaw intelligence

African Grey intelligence

Macaw personality

African Grey personality

---

## **SPECIES COMPARISON KEYWORDS**

African Grey vs Scarlet Macaw

African Grey vs Blue and Gold Macaw

African Grey vs Green Wing Macaw

African Grey vs Hyacinth Macaw

African Grey vs Military Macaw

African Grey vs Severe Macaw

African Grey vs Hahn's Macaw

African Grey vs Red-fronted Macaw

African Grey vs Yellow-collared Macaw

African Grey vs Mini Macaw

---

## **BUYER INTENT**

Which parrot should I buy?

Should I buy an African Grey?

Should I get a Macaw?

Best bird for beginners

Best bird for families

Best bird for apartments

Best bird for talking

Best bird for cuddling

Best bird for bonding

---

## **LONG TAIL**

Is an African Grey smarter than a Macaw?

Can a Macaw talk like an African Grey?

Which bird screams more?

Which bird costs more?

Which bird lives longer?

Which bird bites harder?

Which bird needs more attention?

Which bird is easier to train?

Can a Macaw learn words?

Which bird is friendlier?

---

## **VERY LONG TAIL**

Should I buy an African Grey or a Blue and Gold Macaw?

African Grey vs Scarlet Macaw personality

African Grey vs Green Wing Macaw for beginners

Is a Hyacinth Macaw smarter than an African Grey?

Which parrot talks better, an African Grey or a Macaw?

Can an African Grey and a Macaw live together?

Is a Macaw too loud for an apartment?

---

# **3\. Competitor Gap Keywords**

Almost no competitors fully cover these.

These are opportunities.

air purifier

bird-safe home

daily enrichment

mental stimulation

positive reinforcement

flight training

clicker training

free flight

noise level meter

bite force

ownership cost

annual cost

50-year commitment

vacation care

boarding

insurance

avian emergency

travel cage

pet sitter

destructive chewing

foraging toys

cognitive enrichment

species suitability

working professionals

retirees

children

allergies

powder down

feather dust

---

# **4\. Concurrent Keywords**

Google loves these appearing naturally.

African Grey

↓

talking bird

↓

intelligent parrot

↓

companion parrot

↓

problem solver

↓

mimicry

↓

speech

↓

vocabulary

↓

contextual learning

↓

bonding

↓

lifelong pet

---

Macaw

↓

large parrot

↓

colourful parrot

↓

powerful beak

↓

social bird

↓

playful bird

↓

active bird

↓

chewing

↓

loud vocalisation

↓

flight

↓

climbing

---

# **5\. Entity Map**

## **Core Entities**

African Grey

Congo African Grey

Timneh African Grey

Macaw

Scarlet Macaw

Blue-and-Gold Macaw

Green-wing Macaw

Hyacinth Macaw

Military Macaw

Hahn's Macaw

Severe Macaw

Mini Macaw

Psittaciformes

Psittacidae

---

## **Anatomy**

Beak

Hooked beak

Tongue

Tail

Feathers

Powder down

Plumage

Wing span

Feet

Zygodactyl feet

Nostrils

Iris

---

## **Behaviour**

Flocking

Socialization

Enrichment

Foraging

Chewing

Mimicry

Problem solving

Bonding

Separation anxiety

Territorial behaviour

Hormonal behaviour

Independence

Play

Curiosity

---

## **Veterinary**

Avian veterinarian

Psittacosis

PBFD

Polyomavirus

Hypocalcaemia

Vitamin A deficiency

Beak trimming

Nail trimming

DNA sexing

Microchip

Health certificate

Quarantine

---

## **Nutrition**

Pellets

Fresh vegetables

Leafy greens

Fruit

Seeds

Calcium

Protein

Omega fatty acids

Fresh water

---

## **Ownership**

Travel cage

Play stand

UV lighting

Perches

Foraging toys

Carrier

Insurance

Air purifier

Emergency fund

Lifetime commitment

---

# **6\. Semantic SEO Vocabulary**

companion bird

hookbill

exotic pet

avian behaviour

avian cognition

bird enrichment

intelligent companion

talking ability

speech clarity

mental stimulation

behavioural enrichment

social interaction

daily exercise

out-of-cage time

responsible ownership

ethical breeder

lifelong care

positive reinforcement

bird-safe household

---

# **7\. LSI Vocabulary**

These aren't true "LSI" in the old technical sense, but they are valuable semantically related phrases.

talking ability

speech mimicry

vocal learning

problem solving

noise level

daily routine

owner experience

family suitability

temperament

diet

lifespan

veterinary care

playfulness

flight exercise

activity level

destructive chewing

mental health

stress reduction

social needs

housing requirements

---

# **8\. NLP Co-occurrence Phrases**

Google expects these combinations.

African Grey

* 

talking

* 

intelligence

* 

problem solving

* 

speech

* 

vocabulary

* 

memory

* 

Alex

* 

cognition

---

Macaw

* 

beak strength

* 

colourful feathers

* 

flight

* 

large cage

* 

climbing

* 

playful

* 

loud

* 

social

---

5\.

Excellent—this is the level of analysis I recommend using as the foundation for the page. Below is **Phase 1 – Complete SERP Analysis** for **"African Grey vs Macaw"**, based on the available live search results combined with search intent analysis.

---

# **PHASE 1 — COMPLETE SERP ANALYSIS**

## **Primary Target Keyword**

**African Grey vs Macaw**

---

# **Search Intent Classification**

## **Primary Intent (★★★★★)**

**Commercial Investigation**

The user is evaluating two expensive, long-lived companion parrots before making a purchase or adoption decision.

Typical thoughts:

* Which bird should I buy?  
* Which bird is better?  
* Which fits my lifestyle?

---

## **Secondary Intent (★★★★★)**

Comparison

Users want direct comparisons for:

* Intelligence  
* Talking ability  
* Personality  
* Noise  
* Size  
* Lifespan  
* Training  
* Cost  
* Maintenance

These comparison topics appear consistently across the ranking pages. ([PetHelpful](https://pethelpful.com/all-pets/should-i-buy-a-macaw-or-an-african-grey?utm_source=chatgpt.com))

---

## **Hidden Intent (Most Competitors Miss)**

Google increasingly rewards content that addresses deeper ownership concerns, including:

* Apartment suitability  
* Family compatibility  
* Time commitment  
* Long-term ownership costs  
* Feather dust and allergies  
* Veterinary expenses  
* Travel and boarding  
* Emotional bonding  
* Rescue vs breeder decisions

These topics are generally underrepresented in the current ranking pages. ([PetHelpful](https://pethelpful.com/all-pets/should-i-buy-a-macaw-or-an-african-grey?utm_source=chatgpt.com))

---

# **Current SERP Landscape**

The available results show a mixture of:

| Website Type | Purpose |
| ----- | ----- |
| Niche bird blogs | Experience-based comparisons |
| Pet publisher sites | General buying advice |
| Breed comparison databases | Structured comparison tables |
| Brand/editorial sites | Pet ownership guidance |
| Reddit | Real owner experiences |
| YouTube | Behaviour demonstrations |

Google is rewarding **comparison-focused** content rather than encyclopedic species profiles.

---

# **Top Competitors Currently Appearing**

| Competitor | Why They Rank |
| ----- | ----- |
| CongoAfricanGreys.com | Niche topical authority and focused comparison hub. ([Congo African Greys](https://congoafricangreys.com/african-grey-comparison/?utm_source=chatgpt.com)) |
| PetHelpful | Experience-driven comparison with clear buying guidance. ([PetHelpful](https://pethelpful.com/all-pets/should-i-buy-a-macaw-or-an-african-grey?utm_source=chatgpt.com)) |
| AnimalCompare | Fast-scanning tables and structured comparisons. ([AnimalCompare.com](https://animalcompare.com/compare/african-grey-parrot-vs-macaw/?utm_source=chatgpt.com)) |
| PangoVet | Rich visuals, buying-focused layout, overview sections. ([The Vet Desk](https://articles.pangovet.com/pet-lifestyle/birds/macaw-vs-african-grey/?utm_source=chatgpt.com)) |
| The Vet Desk | Detailed care and personality content. ([The Vet Desk](https://thevetdesk.com/pet-lifestyle/birds/macaw-vs-african-grey/?utm_source=chatgpt.com)) |
| Parrot Website | Strong topical authority around parrots and cognitive comparisons. ([Parrot Website](https://www.parrotwebsite.com/are-african-greys-smarter-than-macaws/?utm_source=chatgpt.com)) |

---

# **Why These Pages Rank**

Common characteristics include:

## **1\. Simple comparison format**

Nearly every page answers:

* Which is better?  
* Which is smarter?  
* Which talks more?  
* Which is louder?

---

## **2\. Easy scanning**

Most use:

* tables  
* bullet lists  
* side-by-side comparisons  
* "At a glance" sections

---

## **3\. Buyer-focused writing**

The content is less about biology and more about helping someone choose a pet.

---

## **4\. Readability**

Most articles are written for a broad audience and avoid technical jargon.

---

## **5\. Matching user questions**

Topics consistently include:

* Intelligence  
* Talking  
* Noise  
* Personality  
* Lifespan  
* Care  
* Space requirements  
* Suitability

---

# **SERP Weaknesses**

The top-ranking pages rarely include:

* Original research  
* Veterinary citations  
* Interactive decision frameworks  
* Ownership timelines  
* Cost projections  
* Scientific studies  
* Advanced enrichment guidance  
* AI-friendly question formatting  
* Visual knowledge assets

This creates a significant opportunity for differentiation.

---

# **Featured Snippet Opportunities**

Google is likely to favor concise answers to questions such as:

* Which bird is smarter?  
* Which bird talks better?  
* Which bird is louder?  
* Which bird is easier to own?  
* Which bird lives longer?  
* Which bird is better for beginners?

Each section on your page should begin with a direct answer before expanding.

---

# **People Also Ask (Intent Clusters)**

## **Intelligence**

* Which bird is smarter?  
* Is an African Grey smarter than a Macaw?  
* Which bird learns faster?  
* Which bird solves puzzles better?

---

## **Talking**

* Which bird talks more?  
* Can Macaws talk?  
* Which bird has a larger vocabulary?  
* Which bird copies speech more accurately?

---

## **Personality**

* Which bird is friendlier?  
* Which bird bonds more closely?  
* Which bird is better with families?  
* Which bird is more affectionate?

---

## **Noise**

* Which bird is louder?  
* Can a Macaw live in an apartment?  
* Does an African Grey scream?

---

## **Care**

* Which bird needs a bigger cage?  
* Which bird is easier to train?  
* Which bird requires more attention?

---

## **Ownership**

* Which bird costs more?  
* Which bird is easier for beginners?  
* Which bird lives longer?  
* Which bird is the better lifelong companion?

---

# **Fan-Out Query Tree**

African Grey vs Macaw  
│  
├── Intelligence  
│   ├── Which bird is smarter?  
│   ├── Problem solving  
│   ├── Memory  
│   ├── Vocabulary  
│   └── Cognitive ability  
│  
├── Talking  
│   ├── Speech clarity  
│   ├── Vocabulary  
│   ├── Mimicry  
│   ├── Context understanding  
│   └── Best talking parrot  
│  
├── Personality  
│   ├── Bonding  
│   ├── Family suitability  
│   ├── One-person bird  
│   ├── Affection  
│   └── Independence  
│  
├── Behaviour  
│   ├── Biting  
│   ├── Screaming  
│   ├── Destructive chewing  
│   ├── Playfulness  
│   └── Hormonal behaviour  
│  
├── Care  
│   ├── Diet  
│   ├── Cage size  
│   ├── Toys  
│   ├── Enrichment  
│   └── Exercise  
│  
├── Health  
│   ├── Feather plucking  
│   ├── Powder down  
│   ├── Avian veterinarian  
│   ├── Common diseases  
│   └── Lifespan  
│  
├── Cost  
│   ├── Purchase price  
│   ├── Annual care  
│   ├── Veterinary expenses  
│   ├── Insurance  
│   └── Lifetime ownership cost  
│  
└── Lifestyle  
    ├── Apartments  
    ├── Families  
    ├── Seniors  
    ├── Working professionals  
    └── Multi-bird households

---

# **Related Search Clusters**

Natural adjacent topics include:

* African Grey vs Cockatoo  
* African Grey vs Amazon Parrot  
* African Grey vs Eclectus  
* Macaw vs Cockatoo  
* Best talking parrot  
* Best pet parrot  
* Smartest parrot  
* Quietest parrot  
* Best parrot for beginners  
* Macaw personality  
* African Grey personality

These are excellent opportunities for internal linking and topical clustering.

---

# **Reddit Insights**

Recent owner discussions highlight practical differences:

* Macaws are often described as more energetic, mischievous, and physically demanding.  
* African Greys are frequently characterized as deeply intelligent, selective in bonding, and more sensitive to environmental changes.  
* Experienced owners stress that both species require substantial enrichment and are unsuitable for casual pet ownership. ([Reddit](https://www.reddit.com/r/Macaws/comments/1rw9lrg/why_are_macaws_such_little_shits/?utm_source=chatgpt.com))

---

# **YouTube Intent**

Video content around this comparison typically focuses on:

* Daily life with each species  
* Talking demonstrations  
* Noise comparisons  
* Owner experiences  
* "Which bird should you choose?"

Embedding or creating complementary video content around these themes can reinforce topical authority.

---

# **Image SERP Strategy**

The dominant visual intent is comparison. To outperform existing pages, create original assets such as:

1. Hero comparison banner  
2. Size comparison silhouette  
3. Intelligence scorecard  
4. Talking ability infographic  
5. Noise level meter  
6. Lifespan timeline  
7. Personality radar chart  
8. Daily care schedule  
9. Diet comparison  
10. Family suitability scorecard  
11. Apartment suitability guide  
12. Cost breakdown  
13. Pros and cons cards  
14. Decision tree ("Which bird is right for you?")  
15. Quick-reference comparison table

---

# **Shopping Intent**

Although informational, the query frequently leads users toward:

* Purchasing a bird  
* Finding a reputable breeder  
* Choosing cages and play stands  
* Selecting pellet diets and enrichment toys  
* Learning about veterinary care and long-term ownership

This supports integrating contextual calls to action and educational buying guidance rather than overt sales messaging.

---

# **Biggest Opportunity**

The current SERP largely compares **African Grey vs "Macaw" as a single group**. Very few pages meaningfully distinguish between individual macaw species.

This creates a major content advantage for **CongoAfricanGreys.com** by adding dedicated comparison sections such as:

* African Grey vs Scarlet Macaw  
* African Grey vs Blue-and-Gold Macaw  
* African Grey vs Green-winged Macaw  
* African Grey vs Hyacinth Macaw  
* African Grey vs Military Macaw  
* African Grey vs Hahn's Macaw  
* African Grey vs Severe Macaw

Those sections introduce unique entities, satisfy more specific search intents, and significantly expand topical authority while capturing long-tail queries that competitors largely ignore.

