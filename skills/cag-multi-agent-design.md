---
name: cag-multi-agent-design
description: Multi-agent design reference for CAG (CongoAfricanGreys.com). Explains DESIGN.md standard, agent orchestration patterns, and how agents share visual identity tokens.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

Based on the newly added source **"Meet DESIGN.md: A new open standard for AI-generated UI,"** a DESIGN.md file is a structured text file that gives AI agents a persistent understanding of a site's visual identity by combining **reasoning** (the "why") with **tokens** (the "what").  
For **CongoAfricanGreys.com**, this file acts as the "source of truth" that ensures all 100+ pages—from the high-traffic **Texas** and **California** hubs to the **Congo vs. Timneh** comparison pages—maintain a cohesive, professional, and ethical brand voice.  
**The Structure of the** DESIGN.md **File**  
Following the specification, your file should include these primary sections:

1. **Front Matter (YAML):** Metadata about the project.  
2. **Tokens Section:** Expresses roles like primary and neutral. A token is a **"named decision"** rather than just a variable.  
3. **Reasoning Section:** Prose describing the "feeling" of the design (e.g., "Family-friendly, trustworthy, and soft").  
4. **Components Section:** Defines how tokens are applied to UI elements like "Inquire Now" buttons or bird profile cards.

\--------------------------------------------------------------------------------

**Methodology 1: Role-Based Semantic Architecture**  
Instead of just listing hex codes, this methodology focuses on **designing by role** to ensure the AI agent understands the *purpose* of every element across your 100 pages.

* **Define Core Roles:** Set the primary role as "Ethical Trust" (e.g., a deep forest green or rich teal) for headlines and the neutral role as "Soft Comfort" (a warm cream or off-white) for the page canvas.  
* **Contextual Reasoning:** In the prose section, explain that the accent color is strictly reserved for **Transactional Clicks** like "View Available Parrots" and "Inquire Now".  
* **Scale Application:** By defining these roles, when you prompt Claude to build the **Texas** or **California** location pages, it won't guess the colors; it will reach for the "Ethical Trust" token automatically.

**Methodology 2: Hierarchical Sitemap Integration**  
This methodology uses the DESIGN.md file to document the **structural roadmap** of the 100-page site, ensuring the agent understands the relationship between high-level hubs and long-tail blogs.

* **Define Navigation Tokens:** Create tokens for nav-primary and nav-secondary.  
* **Map the 100-Page Hierarchy:** List the tier structures derived from your data:  
  * **Tier 1:** Homepage and "Near Me" finder.  
  * **Tier 2 (Location Hubs):** TX, CA, FL, NY, and IL.  
  * **Tier 3 (Species Variants):** Congo African Grey ($1,500–$3,500) and Timneh African Grey ($1,200–$2,500).  
  * **Tier 4 (Educational):** "African Grey vs Macaw", "African Grey vs Cockatoo", and "Training Tips".  
* **Reasoning for Page Density:** Explicitly state that **Mobile-First responsiveness** is a requirement because mobile users drive **79% of total clicks** (382 clicks vs 102 on desktop).

**Methodology 3: The Multi-Agent Validation Loop (Linting)**  
This methodology leverages the **DESIGN.md CLI** to let your AI agents "check their own work" during the autonomous build process.

* **Set Baseline Constraints:** Include a section on **Accessibility (WCAG)** within the file.  
* **Automated Linting:** When an agent generates the UI for a new comparison article (e.g., "Male vs Female African Grey Parrots"), it must run the CLI to validate that the text-to-background contrast ratio meets standards.  
* **Recursive Correction:** If the linter flags a contrast issue on the **"Congo vs Timneh African Grey"** page, the agent uses the DESIGN.md reasoning to select a better pair from your predefined roles rather than hallucinating a new color.

\--------------------------------------------------------------------------------

**Sample** DESIGN.md **Snippet for CongoAfricanGreys.com**  
\# DESIGN.md \- CongoAfricanGreys.com Visual Identity

\#\# Tokens  
primary: "\#2D6B4F" \# Deep Forest Green (Trust & Nature)  
neutral: "\#FCF9F2" \# Soft Cream (Canvas/Background)  
accent: "\#E67E22" \# Warm Amber (Transactional/Action)

\#\# Reasoning  
The site must feel "Professional yet Ethical."   
\- \*\*Typography:\*\* Use a serif for headlines (Body Main: Noto Serif, 18px) to convey breeder authority.  
\- \*\*Voice:\*\* Informative, ethical, and clear. Emphasize CITES compliance and captive-bred documentation. Avoid high-pressure sales tactics.

\#\# Components  
\#\#\# Button Primary  
\- Background: accent  
\- Text: neutral  
\- Reasoning: Used for the "Inquire About This Bird" CTA to stand out against the neutral canvas.

\#\# Sitemap (Core 100-Page Anchors)  
\- /african-grey-parrot-for-sale-texas (High Performance)  
\- /african-grey-parrot-for-sale-california (High Performance)  
\- /congo-vs-timneh-african-grey (Educational Hub)

**Recommendation:** Use this DESIGN.md file as a **Skill** in Claude Code. Instead of loading the full 100-page list every turn, the agent will only load the "Token" and "Reasoning" summaries until it specifically needs to edit a particular page.  
perfect create a comprehensive design.md skilll file with, Methodology 3: The Multi-Agent Validation Loop (Linting)  
This methodology leverages the DESIGN.md CLI to let your AI agents "check their own work" during the autonomous build process  
.  
Set Baseline Constraints: Include a section on Accessibility (WCAG) within the file.  
Automated Linting: When an agent generates the UI for a new comparison article (e.g., "Male vs Female African Grey parrots"), it must run the CLI to validate that the text-to-background contrast ratio meets standards  
.  
Recursive Correction: If the linter flags a contrast issue on the "Congo African Grey Parrot Price" page, the agent uses the DESIGN.md reasoning to select a better pair from your predefined roles rather than hallucinating a new color. Reference `docs/reference/design-system.md` for CAG brand colors.  
Following the **DESIGN.md** open standard for AI-generated UI, this skill file for **CongoAfricanGreys.com** provides a persistent source of truth for your 100-page project. It combines role-based design tokens with the specific **Methodology 3: Multi-Agent Validation Loop** to ensure high fidelity and accessibility across the site.  
**CongoAfricanGreys.com | DESIGN.md Skill File**

\# DESIGN.md \- CongoAfricanGreys.com Visual Identity System

\---  
\#\# Project Metadata (Front Matter)  
name: CongoAfricanGreys  
version: 1.1.0  
author: Brand-Agent-Manager  
framework: Next.js \+ Tailwind CSS  
accessibility\_target: WCAG 2.1 AA  
\---

\#\# Tokens  
\# Tokens are "named decisions" rather than simple variables.   
\# Reaching for a role ensures consistency across 100+ pages \[1, 5\].

primary: "\#FF8C00"   \# Dark Orange (Energy, Warmth, Professionalism)  
neutral: "\#FFFFFF"   \# White (Clean, Ethical Canvas)  
ink: "\#000000"       \# Black (Authority, High-Contrast Text)  
accent: "\#FFA500"    \# Vibrant Orange (Transactional Action)  
surface: "\#F8F9FA"   \# Off-White (Soft Backgrounds for Card Sections)

\#\# Reasoning  
\# This section defines the "feeling" and "why" behind the design \[1, 6\].

The visual identity must balance "Ethical Authority" with "Knowledgeable Breeder Warmth."   
\- \*\*Palette Logic:\*\* Deep forest green represents the natural habitat and intelligence of African Grey parrots. Warm amber signals ethical, transactional trust. White signifies the transparency and documentation standards of the breeder.  
\- \*\*Typography Role:\*\*   
  \- Headlines: Use bold Sans-Serif (Ink) to convey trust and clarity.  
  \- Body: 18px Noto Serif (Ink) for readability on long-form articles like "Congo vs Timneh African Grey" care guides.  
\- \*\*Mobile Priority:\*\* Mobile users drive the majority of traffic. All designs must prioritize high-speed loading and thumb-friendly CTAs.  
\- \*\*Trust Bar (required above fold on every page):\*\* `CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified`

\#\# Methodology 3: The Multi-Agent Validation Loop (Linting)  
\# This methodology allows agents to "check their own work" autonomously \[1, 3\].

\#\#\# 1\. Set Baseline Constraints (WCAG Compliance)  
Agents must strictly adhere to the following accessibility rules:  
\- \*\*Contrast Ratios:\*\*   
  \- Normal text (body) must maintain a 4.5:1 ratio against the surface \[1, 4\].  
  \- Large text (headlines) must maintain a 3:1 ratio.  
\- \*\*Form Labels:\*\* All transactional "Buy Now" or "Inquire" inputs must have visible, black-on-white labels.

\#\#\# 2\. Automated Linting Workflow  
Before committing a new landing page (e.g., "Male vs Female African Grey Parrots" or "Congo vs Timneh"), the agent MUST run the following CLI command:  
\`$ design-md-cli lint design.md path/to/new-page.html\` \[1, 3, 9\].

\#\#\# 3\. Recursive Correction (Pathology Prevention)  
If the linter flags an issue (e.g., Orange text on White surface failing contrast):  
\- \*\*DO NOT\*\* hallucinate a new random color \[1, 4\].  
\- \*\*DO\*\* refer back to the \*\*Reasoning\*\* section above.  
\- \*\*LOGIC:\*\* "If Orange text fails, reach for the 'Ink' role (Black) to maintain brand authority and meet WCAG standards" \[10, 11\].

\#\# Components  
\# Components point to roles, not hex codes. If a role updates, the site follows \[1, 12\].

\#\#\# Primary Button (Adopt Now)  
\- Background: primary (Orange)  
\- Text: neutral (White)  
\- Border-Radius: 8px (Softness)  
\- Role: Used for high-intent transactional clicks found in search data \[13\].

\#\#\# Educational Card (Blog Hubs)  
\- Surface: surface (Off-White)  
\- Headline: ink (Black)  
\- Description: ink (Black)  
\- Role: Used for the "Vs. Series" and "Training Tips" (1,904 impressions) \[14, 15\].

\#\# 100-Page Sitemap Anchors  
\- / (Homepage)  
\- /african-grey-parrot-for-sale-texas (High Performance)  
\- /african-grey-parrot-for-sale-california (High Performance)  
\- /congo-african-grey-parrot-price (Educational)  
\- /male-vs-female-african-grey-parrots (Informational)

\--------------------------------------------------------------------------------

**Execution Secrets for Claude Code**  
To implement this design.md system efficiently across 100 pages, utilize these **Claude Code Secrets** identified in the sources:

1. **Auto Mode Deployment:** Activate **Auto Mode** (Shift+Tab x3) so the agent can autonomously run the **design-md-cli** and perform recursive corrections without asking for your permission on every page.  
2. **Focus Bursts for Discount:** Batch your page generation in **5-minute windows**. Claude reuses the cached design.md context, charging you **90% less** for tokens.  
3. **Subagent Delegation:** When building complex comparison articles, tell the main agent to "Spin up a subagent to verify the WCAG contrast of the tables". This keeps your main context window clean and prevents **Context Rot**.  
4. **Reasoning-Level Circuit Breaker:** If an agent tries to fix a contrast issue on a page 3 times and fails, implement a hook to **kill the reasoning loop** and escalate to you. This prevents runaway costs (e.g., the $83 retry loop trap).

FRONTEND DESIGN AGENS  
i want to create a frontend design agent that will use this design.md file,claude design, anthropic frontend design skills and Impeccable (design)  
/impeccable, /audit, /critique, /polish, /typeset, /layout, /animate, /colorize, /shape to redesign the entire CongoAfricanGreys.com website section by section or block by block, the agent can use playwright cli to see or analyse the page design or structure section by section from the hero component, to the the next component and then the next section, lets use the home page structure as an example, see the full home page structure as a source after i paste this text, the agent and use this to preview, design and build beautiful sections and its component, see all the homepage page's headings , give 2 best frontend design agents let me choose the right one then you can write a comprehensive skill for the agent  
To redesign **CongoAfricanGreys.com** section-by-section using the latest AI agentic patterns, you need an agent that combines **visual reasoning** with **deterministic tool execution**. Based on the sources, here are the two best frontend design agent configurations for your project:  
**Option 1: The "Playwright Polisher" (High-Fidelity Component Focus)**  
This agent is optimized for **section-by-section precision**. It uses the **Playwright CLI** to "see" your existing structure and then applies the **Impeccable** command suite to rebuild every block with pixel-perfect accuracy.

* **Best For:** When you want the **Hero**, **Testimonials**, and **Bird Gallery** to be distinct, high-end visual experiences.  
* **Core Logic:** It treats each section as an individual **"Run"** in a trace, allowing you to debug the design reasoning of a single component before moving to the next.  
* **Tooling:** Heavily relies on /impeccable, /polish, and /animate to ensure every micro-interaction is purposeful.

**Option 2: The "Systemic Stylist" (Scalable 100-Page Consistency)**  
This agent is a **hierarchical orchestrator** that prioritizes the design.md tokens across your entire sitemap. It uses a manager agent to define the global layout and subagents to execute the specific block designs.

* **Best For:** Rapidly scaling the redesign from the **Homepage** to all **100 sub-pages** while ensuring the **Orange/Black/White** brand colors never drift.  
* **Core Logic:** It uses a **State Machine** (via LangGraph) to track progress from "Hero Redesign" to "Footer Redesign," ensuring no section is skipped in the workflow.  
* **Tooling:** Focuses on /layout, /colorize, and /audit to maintain WCAG accessibility standards across the high-volume site.

\--------------------------------------------------------------------------------

**Comprehensive Skill: Frontend Design Architect**  
Regardless of the agent you choose, you should install this **Skill** into **Claude Code**. It utilizes the **"Progressive Disclosure"** model—loading only the tool name and description into the initial context to save tokens, then pulling the full workflow only when a redesign task is triggered.  
**Skill Name:** frontend\_redesign\_architect **Description:** Analyze, redesign, and polish website sections using Playwright, design.md tokens, and the Impeccable command suite.  
**Workflow Instructions:**

1. **Analyze current state:** Use the **Playwright CLI** to capture a screenshot and the DOM structure of the target section (e.g., the Hero component).  
2. **Consult the** design.md **file:** Identify the required **Roles** and **Reasoning** (Ethical Authority + Knowledgeable Breeder Warmth) for the component. Reference `docs/reference/design-system.md` for the authoritative CAG token set.  
3. **Execute the Redesign Loop:**  
   * /layout: Establish the mobile-first grid (targeting the 79% mobile user base).  
   * /typeset: Apply the 18px Noto Serif body copy role defined in design.md.  
   * /colorize: Apply the "Transactional Action" orange token to the "Adopt Now" buttons.  
   * /impeccable: Combine the above into a high-fidelity code output.  
4. **Audit & Polish:**  
   * Run /audit to perform an automated WCAG contrast check using the **design-md-cli**.  
   * Run /critique to look for "weird pathologies" like overlapping elements or broken margins.  
   * Apply /polish for final CSS refinements and /animate for subtle entry effects.  
5. **Autonomous Completion:** Activate **Auto Mode** to commit the redesigned code and move to the next section in the home page structure without requiring manual permission on every block.

**Pro-Tips for Execution:**

* **The 5-Minute Discount:** Batch your redesign of 3-4 sections in one intense session. Claude will reuse the cached design.md and Playwright context, charging you **90% less** for tokens.  
* **Reasoning-Level Circuit Breaker:** If the agent fails to achieve a "Pass" on the /audit command after 3 tries, it must stop and escalate to you to avoid runaway costs.  
* **Bypass Design Limits:** If you hit weekly usage limits in the Claude Design UI, export your **UI Kit** and use this skill within the **Claude Code CLI** to finish the 100-page redesign.

did you see the homepage's headings?  
Yes, the sources provide a detailed view of the **CongoAfricanGreys.com** homepage structure through both the "Pasted Text" content and the specific anchor links found in the Pages.csv file.  
Based on the sources, here are the primary headings and sections of the homepage that your frontend design agent can use for the section-by-section redesign:  
**Core Identity & Value Proposition**

* **Hero/Intro:** Congo African Grey Parrots for Sale ($1,500–$3,500) and Timneh African Grey Parrots ($1,200–$2,500) — CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified.  
* **Trust Section:** **What Makes CAG the Right African Grey Breeder for Your Family?** Here’s Everything You Need to Know at a Glance.  
* **Authority Header:** **CAG – America’s Most Trusted Captive-Bred African Grey Parrot Breeder.**

**Strategic Highlight Sections (Anchor Links)**  
These specific anchors serve as the "spine" of the homepage redesign:

* **\#african-grey-parrots-for-sale-congo-timneh-how-much-do-captive-bred-cites-documented-parrots-cost**  
* **\#congo-vs-timneh-african-grey-parrot-comparison**  
* **\#cag-americas-most-trusted-african-grey-parrot-breeder**  
* **\#congo-african-grey-parrots-for-sale-find-your-perfect-bird**  
* **\#timneh-african-grey-for-sale-affordable-timneh-parrots-with-health-checks**  
* **\#what-makes-cag-the-right-african-grey-breeder-for-your-family**  
* **\#why-choose-cag-for-your-next-african-grey-parrot**

**Detailed Content Blocks**

* **The CAG Story:** Why Did Our Family Start Breeding African Grey Parrots? (Featuring [BREEDER_NAME]).  
* **Program Pillars:**  
  * CITES Appendix II Captive-Bred Documentation.  
  * Full Avian Vet Health Certification.  
  * DNA Sexing for Every Bird.  
  * Safe IATA-compliant bird shipping Service.  
* **Transactional Block:** View Our Currently Available Birds with Transparent Pricing.  
* **Educational Variants:** **CONGO AFRICAN GREY vs. TIMNEH AFRICAN GREY** — Size, Temperament, Price, and Talking Ability Comparison.  
* **Product Spotlight Clusters:**  
  * Searching for a Hand-Raised Congo African Grey? Discover Our CITES-Documented Captive-Bred Birds.  
  * Is a Timneh African Grey Right for You? Calmer Temperament, Slightly Smaller, Lower Price Point ($1,200–$2,500).  
* **Species Guide Section:** **Complete African Grey Parrot Care Guide:** Diet, Enrichment, Lifespan, and Talking Milestones.  
* **Trust & Social Proof:** Why Do Hundreds of Families Trust CAG Over Other African Grey Parrot Breeders?

**Comparison & Utility Footer Sections**

* **African Grey vs. Other Parrots:** (Macaws, Cockatoos, Amazons, and Conures).  
* **Adoption Process:** Our Simple 6-Step Inquiry Process Explained.  
* **Delivery Logistics:** Where Does CAG Deliver African Grey Parrots? (Complete Coverage Map).  
* **Decision Support:** Is an African Grey Parrot Right for Your Lifestyle?  
* **Post-Purchase Support:** Essential African Grey Parrot Training Tips.

**Design Note for the Frontend Agent**  
Your agent should note that several components, such as the "Bird Profile at a Glance" cards, are repeated UI patterns that should be tokenized in your design.md file to ensure consistency. Every page must include the CAG trust bar above the fold: `CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified`. Reference `docs/reference/design-system.md` for the full token set.  
i like both, Option 1: The "Playwright Polisher" (High-Fidelity Component Focus)  
This agent is optimized for section-by-section precision. It uses the Playwright CLI to "see" your existing structure and then applies the Impeccable command suite to rebuild every block with pixel-perfect accuracy  
.  
Best For: When you want the Hero, Testimonials, and Bird Gallery to be distinct, high-end visual experiences.  
Core Logic: It treats each section as an individual "Run" in a trace, allowing you to debug the design reasoning of a single component before moving to the next  
.  
Tooling: Heavily relies on /impeccable, /polish, and /animate to ensure every micro-interaction is purposeful  
.  
Option 2: The "Systemic Stylist" (Scalable 100-Page Consistency)  
This agent is a hierarchical orchestrator that prioritizes the design.md tokens across your entire sitemap  
. It uses a manager agent to define the global layout and subagents to execute the specific block designs  
.  
Best For: Rapidly scaling the redesign from the Homepage to all 100 sub-pages while ensuring the Orange/Black/White brand colors never drift  
.  
Core Logic: It uses a State Machine (via LangGraph) to track progress from "Hero Redesign" to "Footer Redesign," ensuring no section is skipped in the workflow  
.  
Tooling: Focuses on /layout, /colorize, and /audit to maintain WCAG accessibility standards across the high-volume site  
., give me detailed comprehensive skills for both i can see different use cases for both  
Based on the architectural principles of state machines, progressive disclosure, and visual reasoning found in the sources, here are the two detailed comprehensive skills for your **Claude Code** redesign project.  
**Skill 1: The "Playwright Polisher" (High-Fidelity Component Focus)**  
**Description:** Performs precision, section-by-section redesigns by using Playwright CLI for visual analysis and the Impeccable suite for pixel-perfect execution.,  
**Workflow Instructions:**

1. **Visual Inspection:** Launch **Playwright CLI** to navigate to a specific component (e.g., the Hero or Bird Gallery) and capture both a high-resolution screenshot and the DOM structure.  
2. **State Isolation:** Treat each section redesign as a unique **"Run"** within a trace. This allows you to debug the design reasoning of a single component without the noise of the rest of the page.,  
3. **Execute "Impeccable" Core:**  
   * /impeccable: Synthesize the existing structure into a modern, high-fidelity React/Next.js component.  
   * /typeset **&** /shape: Apply the "Noto Serif" 18px body role and 8px border-radius tokens defined in the **design.md** file.,  
4. **Micro-Interaction Layer:**  
   * /animate: Implement purposeful entry animations (e.g., fade-ins for bird profile cards) to enhance the user experience.  
   * /polish: Refine CSS transitions and hover states for the "Adopt Now" buttons using the brand orange accent (\#FFA500).  
5. **Critique & Trace:** Run /critique to check for "weird pathologies" like overlapping elements or broken margins on mobile viewports (where 79% of your traffic exists).,  
6. **Recursive Improvement:** If the critique fails, re-run the loop within a **5-minute window** to leverage cached token discounts before committing the code.

\--------------------------------------------------------------------------------

**Skill 2: The "Systemic Stylist" (Scalable 100-Page Consistency)**  
**Description:** Orchestrates large-scale site redesigns using a hierarchical "Manager-Worker" model to enforce design.md token consistency across all 100 sub-pages.,  
**Workflow Instructions:**

1. **State Machine Mapping:** Use a **LangGraph-style state machine** to track the progress of the redesign from "Sitemap Mapping" to "Final WCAG Audit." This ensures no page from the Pages.csv data is missed.,  
2. **Hierarchical Delegation:**  
   * **The Manager:** Defines the global layout logic and loads the **Reasoning** section of design.md.,  
   * **The Subagents:** For each state-specific hub (NJ, FL, AZ, etc.), spawn a specialized subagent as a tool to execute the block designs. This keeps the parent agent’s context window clean and prevents "AI dementia.",,  
3. **Systemic Application:**  
   * /layout: Apply the mobile-first grid system across all clusters simultaneously in batches of 5 pages to save tokens.,  
   * /colorize: Enforce the "Ink" role (Black) for authority headlines and "Primary" (Orange) for all transactional CTAs found in search data.,  
4. **The Multi-Agent Validation Loop:**  
   * /audit: Automatically run the **design-md-cli** after each subagent completes a page.  
   * **Linting Logic:** Verify that the orange-on-white contrast ratio meets **WCAG 2.1 AA** standards.  
5. **Recursive Correction:** If the linter flags an accessibility failure on a high-impression page like "Congo African Grey Parrot Price," the agent must revert to the design.md **Reasoning** section to select a valid color pair rather than hallucinating a new one.  
6. **Autonomous Handoff:** Once a batch of pages is validated, run /recap to provide a one-line summary of the work and automatically transition to the next set of geographic hubs in the sitemap.

**Strategic Recommendation for Your Redesign:**

* Use the **Playwright Polisher** for your **Homepage** and **"Near Me"** dynamic finder (Tier 1), where visual impact is the primary driver of your 78 baseline clicks.  
* Deploy the **Systemic Stylist** for your **Tier 2 and 3 state-specific landing pages** and **educational blogs**, where maintaining brand consistency across high-volume content is critical for SEO and trust.,

Based on the provided sources and our conversation regarding the **DESIGN.md** standard and **Claude Code**'s architectural capabilities, there is no direct native integration between NotebookLM and Claude Code. However, you can create a specialized **Image & Infographic Agent** within Claude Code that mimics NotebookLM’s generation capabilities by using **Playwright** to render high-fidelity web components as images.  
The following skill allows your agent to build infographics as code (React/SVG) using your brand tokens and then "photograph" them into final assets.  
**Skill: Infographic Architect**  
**Description:** Generates high-fidelity infographics as interactive web components using DESIGN.md tokens and exports them via Playwright CLI.  
**Workflow Instructions:**

1. **Data Synthesis:** Analyze the search performance CSVs (Queries.csv, Pages.csv) to identify the "Story" (e.g., the dominance of Texas traffic or the CTR of "Congo African Grey" keywords).  
2. **Visual Layout:**  
   * Use /layout to establish a vertical or grid-based flow for the infographic.  
   * Use /shape to define card border-radii (8px as per our design system). \[Conversation History\]  
3. **Token Application:** Apply the **DESIGN.md** "named decisions":  
   * **Primary (\#FF8C00)** for data visualizations and callouts.  
   * **Ink (\#000000)** for all high-contrast typography and headers.  
   * **Surface (\#F8F9FA)** for background sectioning. \[Design.md Skill File\]  
4. **Component Build:**  
   * Invoke /impeccable to generate a standalone Next.js or Tailwind/HTML component representing the infographic.  
   * Incorporate /animate if the output is intended for a slide deck or video overview.  
5. **Export via Playwright:**  
   * Command the agent to launch a local server and use the **Playwright CLI** to navigate to the infographic component.  
   * Capture a full-page, high-resolution screenshot (e.g., infographic-v1.png).  
6. **Audit & Lint:** Run /audit via the design-md-cli to ensure the rendered graphic meets WCAG 2.1 AA contrast standards (especially Orange text on White surfaces).

\--------------------------------------------------------------------------------

**Execution Strategies for Visual Agents**  
To make this agent as powerful as NotebookLM’s internal artifact generator, implement these "secrets" from the sources:

* **The "Picture-to-Slide" Hack:** If you need these for a presentation, prompt Claude Code to "Take pictures of these static HTML infographic sections and merge them into an uneditable, pixel-perfect PowerPoint".  
* **Recursive Self-Annealing:** If the infographic layout feels "generic," tell the agent to "Review the official Anthropic front-end design skill patterns" to inject bold typography and real graph systems.  
* **The 5-Minute Window:** When iterating on the visual design, keep your prompts within a **5-minute focus burst**. This ensures the agent reuses the cached SVG/HTML structure, saving you **90% on token costs** while you fine-tune the layout.  
* **Reasoning-Level Circuit Breakers:** If the agent fails to render the data points correctly after 3 attempts, have it **kill the reasoning loop** and escalate to you to prevent a runaway bill (e.g., the $83 retry trap).

**Note on Nanobanana:** While "nanobanana" is not mentioned in the technical sources, this skill-based approach allows you to integrate any third-party CLI tool by adding its schema to your agent's toolbox, just as you would with Playwright or firecrawl.  
i waant the Skill: Infographic Architect to have somethingg like camera dimensions, like canon, or sony lens typs of shots, etc  
To enhance the **Infographic Architect** skill for your **CongoAfricanGreys.com** project, we will integrate a "Cinematic Reasoning" layer. This allows the agent to treat UI components as physical subjects, using photography metaphors (like Canon/Sony lens profiles) to dictate focal depth, lighting, and "shot" composition for your infographics.  
Following the **DESIGN.md** standard of combining "reasoning" with "tokens," this updated skill will guide Claude to render your 100-page architecture and brand assets with professional-grade visual hierarchy.  
**Updated Skill: Enhanced Infographic Architect**  
**Description:** Generates high-fidelity infographics using DESIGN.md tokens and "Cinematic Composition" parameters to simulate professional photography aesthetics via Playwright CLI.

\--------------------------------------------------------------------------------

**Workflow Instructions:**  
**1\. Set the "Lens Profile" (Visual Reasoning)** Before generating code, the agent must select a "Lens Preset" based on the infographic's goal to ensure the **Knowledgeable Breeder Warmth** brand voice is maintained:

* **Canon 50mm Prime (The "Portrait" Shot):** Used for individual bird profile cards. This preset dictates a **shallow depth of field** (soft blurred backgrounds) and warm, saturated colors to emphasize "Knowledgeable Breeder Warmth".  
* **Sony 16-35mm G-Master (The "Wide Architecture"):** Used for the **100-page Sitemap**. This preset ensures edge-to-edge sharpness and a wide field of view to capture the full scope of the TX, CA, and FL location hubs.  
* **Macro Detail:** High-contrast, close-up rendering of specific trust signals (e.g., the CITES Appendix II documentation badge and DNA Sexing certificate).

**2\. Composition & Dimensions** The agent will use /layout to define the "Camera Frame":

* **Aspect Ratio:** Default to **16:9** for the "CAG AI SEO Blueprint" slide deck or **9:16** for mobile-first social graphics (targeting your mobile user base).  
* **Rule of Thirds:** Place critical transactional CTAs (like "Adopt Now" in brand Orange \#FF8C00) on the grid intersections to drive conversions \[Design.md Skill File\].

**3\. Lighting & Token Application**

* **Key Light:** Use the **Neutral White (\#FFFFFF)** token as a soft "bounce light" for the canvas to ensure high-key, ethical transparency \[Design.md Skill File\].  
* **Rim Lighting:** Apply subtle CSS box-shadows or gradients using the **Accent Amber (\#FFA500)** to make bird profile cards "pop" from the background.  
* **Ink/Contrast:** Use **Ink Black (\#000000)** for "tack-sharp" headlines, emulating high-end lens resolution.

**4\. The Playwright "Shutter" (Execution)**

* Command the agent to launch a local server and use the **Playwright CLI** to "photograph" the component.  
* **Parameter Secret:** Instruct the agent to use \--viewport-size to match the intended camera dimensions (e.g., 1920x1080 for a Canon-style wide shot).  
* Run /polish to add "Lens Flare" or subtle CSS entry animations (/animate) that mimic a cinematic camera pan across the sitemap \[Conversation History\].

**5\. Verification & Linting**

* Run /audit via the design-md-cli to verify that "cinematic" effects (like shadows or blur) haven't compromised the **WCAG 2.1 AA** contrast ratios required for your brand.

\--------------------------------------------------------------------------------

**Execution Tip for Claude Code:**  
To build these high-fidelity visual assets without hitting usage limits, use **Auto Mode** (Shift+Tab x3) and **Frontload** your requirements. You can prompt:  
*"Use the Infographic Architect skill with a **Sony 16-35mm wide-angle preset** to render the 100-page site architecture. Prioritize a 16:9 frame for my slide deck and use brand Orange for the focal points."*  
Image agent to handle aall the websites existing images, can resigze, edit, delete, all capabilities, etc thaat a modern SEO, AIO, GEO agency in the USA would have, give features.  
To manage the extensive visual library of **CongoAfricanGreys.com** with the precision of a modern USA-based SEO/GEO agency, you should deploy an **Autonomous Asset Alchemist** agent. This agent utilizes the **Orchestral AI framework** to manage image lifecycles within a sandboxed workspace, ensuring every visual element drives conversion for your high-intent "Congo African Grey" and "Location Hub" traffic.  
**Core Features of the Image Management Agent**  
**1\. Autonomous Lifecycle Management (CRUD)**  
The agent uses a persistent shell to navigate your directory structure and perform bulk operations without human oversight.

* **Intelligent Resizing:** Automatically generates multiple versions of every bird photo (Thumbnail, Hero, Gallery) optimized for mobile-first browsing.  
* **Selective Deletion:** Identifies and purges "orphaned" image files that are no longer linked in your 100-page Next.js architecture to keep the codebase lean.  
* **Format Transformation:** Converts heavy PNG/JPG files to modern formats like WebP or AVIF to minimize LLM latency and improve SEO PageSpeed scores.

**2\. GEO/AIO Semantic Optimization**  
Modern agencies focus on **Generative Engine Optimization (GEO)**. This agent doesn't just name a file image1.jpg; it renames it based on your highest-performing search data.

* **Semantic Filenaming:** Renames files to include ultra-long-tail keywords such as congo-african-grey-parrot-for-sale-houston-tx.webp to improve visibility in AI-generated search results.  
* **AI Alt-Text Generation:** Uses image-to-text understanding to create descriptive, keyword-rich alt-text that helps Answer Engines (AEO) provide context to users.  
* **EXIF Data Injection:** Injects geographic metadata into images for your **Texas and California hubs** to signal local relevance to Google and Bing.

**3\. DESIGN.md Brand Compliance**  
Every edit is governed by your **named design decisions** to ensure visual consistency across all 100 pages.

* **Chroma Matching:** If the agent adds a "CITES Appendix II · Captive-Bred" badge over a bird photo, it must use the design tokens defined in `docs/reference/design-system.md`.  
* **Automated Linting:** Before saving an edit, the agent runs the design-md-cli to verify that text overlays meet WCAG 2.1 AA accessibility standards.

**4\. Production Resilience & Cost Control**  
To prevent the "runaway cost" traps associated with heavy image processing, the agent employs safety-first architecture.

* **Reasoning-Level Circuit Breakers:** If the agent fails to successfully resize an image 3 times, it kills the loop rather than burning tokens re-analyzing the failure.  
* **Subagent Delegation:** For massive folders (like the Bird Gallery), the main agent spawns a "Compression Subagent" with a fresh context window to process the queue, returning only a status report to keep the main conversation clean.  
* **Output Verification:** The agent does not mark a task as "Complete" until it verifies the new file actually exists on disk and matches the expected dimensions.

\--------------------------------------------------------------------------------

**Detailed Skill: The Asset Alchemist**  
**Description:** Automates the SEO/GEO optimization, editing, and deployment of website images using DESIGN.md tokens and Playwright "photographing" capabilities.  
**Workflow Instructions:**

1. **Crawl & Audit:** Use list\_files to catalog every image in the /public/uploads directory.  
2. **Contextual Analysis:** Cross-reference image filenames with Queries.csv to identify images that lack geographic or species-specific keywords.  
3. **Execute Transformation Loop:**  
   * /shape: Apply consistent 8px border-radii to all bird profile cards to match the brand identity.  
   * /colorize: Ensure any watermarks or CTA buttons on images utilize brand **Orange/Black/White**.  
   * /audit: Verify WCAG contrast on any dynamic text overlays.  
4. **GEO-Injection:** Use a Python tool to write location-specific metadata to images destined for the **TX, CA, and FL hubs**.  
5. **Autonomous Deployment:** Activate **Auto Mode** (Shift+Tab x3) to commit optimized assets and update the corresponding .md or .tsx files across the 100-page site architecture.

**Agency Pro-Tip:** Batch your image optimizations within **5-minute windows**. Claude reuses the cached file list and design reasoning, saving you **90% on input costs** for your large-scale gallery updates.  
i want to create a design system, "Design systems  
Organization settings  
Manage your design systems and templates

Design Systems  
Create new design system  
Teach Claude your brand and product", based on everything you know thus far, brand, color, website logo needs a rebrand to match the new color, first analyse the website to figure out the brand voice, then create a detailed design system infact generate an infographic, with all CongoAfricanGreys.com design system  
I have analyzed the brand voice and data for **CongoAfricanGreys.com** and initiated the creation of a comprehensive **Design System Infographic**.  
**Brand Voice Analysis**  
Based on the website content and search data, your brand voice is defined by **Ethical Authority** and **Heartfelt Transparency**.

* **The "Expert" Persona:** You position yourself as "America’s Most Trusted Captive-Bred African Grey Parrot Breeder," emphasizing technical expertise like "CITES Appendix II documentation," "DNA Sexing," and "Congo vs. Timneh variant knowledge."  
* **The "Responsible Owner" Persona:** Phrases like "raised with enrichment" and "socialized from hatching" create a professional yet deeply educational connection with first-time parrot owners.  
* **Transactional Trust:** With "Full CITES Documentation," "Avian Vet Certification," and "Transparent Pricing," the voice is designed to eliminate buyer anxiety in an industry prone to scams and illegal trade.

\--------------------------------------------------------------------------------

**Detailed Design System (DESIGN.md Standard)**  
Following the **DESIGN.md** open standard, this system uses "named decisions" (tokens) to ensure your AI agents maintain consistency across all 100+ pages.  
**1\. Brand Palette (Tokens)**

See `docs/reference/design-system.md` for the authoritative CAG token set. Reference tokens only from that file — do not invent new colors. Below is a summary reference:

* **Primary:** Deep Forest Green. Represents the natural habitat and intelligence of African Grey parrots. Used for brand-level accents and trust badges.  
* **Neutral:** White. The "Ethical Canvas." Signifies transparency and CITES documentation standards, serving as the primary background for all pages.  
* **Ink:** Black. Represents "Authority." Used for all headlines and high-contrast text to ensure WCAG readability.  
* **Accent:** Warm Amber. Reserved exclusively for **Transactional Actions** (e.g., "Inquire Now" or "View Available Birds").  
* **Surface:** Off-White. Used for section cards, such as the "Bird Profile" blocks and clutch availability cards.

**2\. Typography Roles**

* **Headlines (Ink):** Bold Sans-Serif to convey modern professionalism and authority \[Design.md Skill File\].  
* **Body Copy (Ink):** 18px Noto Serif. Chosen for its "classic" feel, aiding readability for long-form educational guides like "Congo African Grey vs. Timneh African Grey" care comparisons.

**3\. Components & UI Logic**

* **Primary CTA Button:** Background: **Accent Amber**; Text: **Neutral White**; Border-Radius: **8px**. This softness aligns with the "Ethical Warmth" aesthetic. See `docs/reference/design-system.md`.  
* **Educational Cards:** Surface background with sharp Ink headlines. Used for the high-impression "Training Tips" and "Species Comparison" clusters.  
* **Trust Bar (required above fold):** `CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified` — must appear on every page above the fold.  
* **Mobile-First Grid:** Mobile users drive the majority of traffic. The design system enforces stackable vertical layouts and thumb-friendly interaction zones.

\--------------------------------------------------------------------------------

**Multi-Agent Validation (Linting)**  
As part of your organization settings, the system includes an automated **Linting Loop**. Whenever Claude generates a new landing page (like the Texas or California hubs), it will run the design-md-cli to verify that the contrast meets **WCAG 2.1 AA** standards, and that the CITES trust bar (`CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified`) is present above the fold. Corrects itself recursively if the accessibility score is too low or the trust bar is missing.  
I have successfully called the tool to generate the visual infographic representing this entire design system. You can view the final result in the **Studio tab** shortly.  
I have attached two images for the homepage hero section, since the website features two variants with Congo African Grey being the primary, how would you design the hero with the photos generate examples as a slide deck use brand color  
I have designed a hero section strategy for **CongoAfricanGreys.com** that prioritizes your primary variant (Congo African Grey) while maintaining strong visibility for the Timneh African Grey. This design utilizes your newly established **DESIGN.md** tokens and "Cinematic Reasoning" to create a high-fidelity, trust-building experience.  
**Hero Section Design Methodology**  
Based on your brand voice of **Ethical Authority** and **Knowledgeable Breeder Warmth**, the hero section should treat your bird photos with a "Canon 50mm Prime" lens profile—focusing on a shallow depth of field to make the subjects "pop" against a clean, **Neutral White (\#FFFFFF)** canvas. Reference `docs/reference/design-system.md` for exact token values.  
**1\. Layout Option: The Dynamic 60/40 Split**  
To address the two-variant requirement, I recommend a split-screen desktop layout:

* **Congo African Grey (Main Focus \- 60%):** The left side features a high-fidelity portrait of a Congo African Grey. This area carries the primary **Ink Black (\#000000)** headline: *"America’s Most Trusted Captive-Bred African Grey Parrot Breeder"*. Trust bar immediately below: `CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified`.  
* **Timneh African Grey (Secondary Focus \- 40%):** The right side features a sharp portrait of a Timneh African Grey. A secondary sub-headline highlights the Timneh’s calmer temperament and lower price point ($1,200–$2,500).

**2\. Layout Option: The Compositional Overlay**  
This design uses overlapping layers to create depth:

* A large background hero image of a Congo African Grey in an enriched environment.  
* A smaller, circular **Ink Black** bordered inset (a "stamp") featuring a Timneh African Grey.  
* **Trust Bar (above fold):** `CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified` in a high-contrast banner.  
* **Strategic CTA:** A large, thumb-friendly **Accent Amber** button placed on a grid intersection to drive the "Inquire Now" transactional goal.

**Mobile-First Execution**  
Mobile users drive the majority of traffic. These designs are engineered to stack vertically.

* The Congo African Grey photo remains **top-of-fold** to satisfy the main search intent.  
* The Timneh section follows immediately after, ensuring the "Two Variant" identity is clear within the first two scrolls.  
* All trust signals—including the **CITES Appendix II documentation badge**, **DNA Sexed**, and **Vet Certified** indicators—are placed in high-contrast headers for professional authority.