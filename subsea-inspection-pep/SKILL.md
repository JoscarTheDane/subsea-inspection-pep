---
name: subsea-inspection-pep
description: Write Project Execution Plans for subsea/diving structural inspection tenders — answering operational readiness questions, not filling a generic template.
version: 1.0
---

# Subsea Inspection PEP

## Trigger
User asks to write or update a Project Execution Plan (PEP) for an offshore structural inspection / diving tender. Typically for clients like CNL (Chevron), Shell, TotalEnergies, Oando — involving API RP 2SIM Level 2 / 3 surveys.

## The Fundamental Rule

**A tender PEP is not a generic template — it must answer specific operational questions that demonstrate you've understood the job.** The user will correct generic filler. The following structure and checklist is what they expect.

## Required Data Points

Every PEP for a subsea inspection tender MUST answer all of these. If the SOW doesn't contain the answer, mark it `[TBC]` and the user will supply contractor-specific info.

### 1. DEPTH & WORKSCOPE (front page)
- Water depth range (e.g. "2m to 60m")
- API RP 2SIM levels (Level 2 only, or Level 2 + Level 3)
- List of fields / facilities (e.g. "Okan, Meji, Delta, Delta South, Tapa, Parabe...")

### 2. LOCATION DETAILS
- Distance from support base / nearest commercial ports
- How is the site accessed? (vessel / heli / airplane)
- Nearest hospital and medevac route

### 3. FACILITIES / SUBJECT
- Pipeline specs (diameter, grade, wall thickness, coating — state `[TBC]` if not in SOW)
- Platform specs, GA drawings, coordinates — note these are typically in a separate data book
- What protection materials are present (concrete mattresses, rock dump, fendering)

### 4. LOCKOUT/TAGOUT (LOTO)
- Specific LOTO procedure for the project — state how the diver's worksite is isolated
- Reference client PTW system

### 5. VESSELS & EQUIPMENT
- Vessel name(s), class, capabilities (ask user for their specific vessel)
- Task of each vessel (DSV = dive platform, RIB/Zodiac = personnel/equipment transfer)
- Dedicated kVA for diving (minimum per SOW, actual from vessel specs)
- Diving deployment method (LARS from stern, ladder entry, SRP from RIB)
- Umbilical length (based on max depth) and umbilical management hazards

### 6. EMERGENCY RESPONSE
- Nearest hyperbaric chamber / recompression facility
- Nearest hospital and medevac corridor
- Emergency Response Method (heli medevac, crew boat transfer, etc.)
- Decontamination plan if leaking product is encountered

### 7. PERSONNEL
- Total team size per spread (dive team + supervision + data + HSE + deck)
- Full role breakdown (PM, Diving Superintendent, Diving Supervisor, 3.4U Coordinator, HSE, ACFM Tech, Divers, Data Controller, Deck Crew)
- Personnel transfer method (boat landing specs, FROG, helicopter deck)
- Crew change method and rotation schedule

### 8. MOBILISATION
- Where vessels are stationed during mobilisation of diving equipment
- Who is on the mobilisation team
- Routing from support base to work site (e.g. Warri → Escravos convoy)
- Method of mobilising and crew changes
- Air bank layout and cascade system configuration

### 9. COMMUNICATIONS
- Method of comms to land (VHF, SSB, satellite — voice, email, fax)
- Contact numbers for project team

### 10. HAZMAT / ENVIRONMENT
- Are we diving around product / effluent? (SIMOPS on producing facilities — YES)
- Provide MSDS for produced fluids at the facilities
- What protection materials are needed (PPE, decontamination kit, etc.)
- Removal or repositioning of pipeline protection materials where present

### 11. NDT METHODOLOGY — ACFM over MPI
Propose ACFM as primary Level 3 NDT when:
- SOW admits poor to zero visibility (sediment discharge, river plumes)
- SOW notes currents >1 knot make MPI difficult
- SOW states divers must determine "adequate visibility" for MPI

ACFM advantages to highlight:
- Zero-visibility capable (electromagnetic, not visual)
- Immune to water currents
- Quantitative crack sizing in one scan
- Works through coatings up to 5mm
- No particle application or UV lighting needed
- Keep MPI as contingency where conditions permit

## PEP Document Format
- Restricted / ECCN header (matching client document control)
- Revision History table
- Table of Contents
- Abbreviations table (matching example format)
- Section structure matching example PEPs from prior projects
- Output as .docx using python-docx with Calibri font, blue heading colours
- Blue table headers on dark background (`#003366`) with white text

## Reference Integration
When IMCA standards are referenced in the PEP:
1. Load the `imca-register-check` skill
2. Cross-reference every IMCA D-series document the user lists against the current register
3. Present a delta table showing what changed
4. Flag non-IMCA refs (DMAC, IOGP, IMO, USN, API, ISO) as "external, verify separately"
5. Add all CNL/operator-specific attachments identified in the SOW

## Interface-First Delivery Rule

**CRITICAL: Do NOT auto-generate content into the .docx.** The user is actively working on their own PEP and will paste specific sections themselves. Always:

1. Produce the requested content IN THE CHAT as paste-ready text
2. Let the user review and accept before anything goes into the document
3. Never write directly to the .docx unless explicitly asked
4. When checking references (IMCA register, etc.), give the raw table output in chat

## Section Format Preferences

Each section has a specific format the user expects based on Atlantic Marine / Shell example PEPs. **Match the example format exactly — same phrasing structures, same level of detail, same table columns.**

### Introduction (2.1 Purpose)
5-paragraph structure:
1. "[Contractor] have been contracted by [Client], to provide [services] for [project name]"
2. "This involves risk-assessed underwater inspections, surveys and NDT on critical structural components of [facilities] to ensure safe and continued operations."
3. "The scope complies fully with [standards — Lloyd's / API / IMCA / client-specific]..."
4. "All [operations] will be performed from a Client-approved [vessel/DSV] utilising [deployment method — LARS] and [equipment — SRP system], and shall be conducted in strict compliance with all applicable company policies and procedures approved by [Client]."
5. "The safe execution and efficiency of operations is of the essence to allow [facilities] to remain in [production/service] while inspections and repairs are performed."

### Document Objectives (2.2)
4-paragraph structure:
1. "[Contractor] have been contracted to carry out [scope] in accordance with [standards]"
2. "The objective of this document is to outline the comprehensive scope of work, procedures, equipment and safety protocols for [project]. This involves risk-assessed [specific activities]..."
3. "The document provides detailed information on project execution, [operations type], mobilisation planning, vessel and equipment requirements, HSE management, reporting systems and quality assurance measures necessary to ensure successful and safe completion of [project]."
4. "Overall, this document serves as a comprehensive guide for the [project name], outlining the tasks, responsibilities and procedures to ensure the safe and effective completion of [campaign]."

### Scope of Work (Section 3)
Two-table format matching the user's example exactly:
- Table 1: **General Activities** — columns: No. | 🚢 Activity | 📄 Description
  - Numbered rows: Project Management & Documentation, Pre-Mobilisation Inspection, Equipment Mobilisation, Personnel Mobilisation, Community Engagement, Facility Entry & LOTO, HIRA, PTW, Kick-off, Reporting, Demobilisation
- Table 2: **Inspection Activities** — columns: No. | 🌊 Activity | 🔧 Key Tasks
  - Numbered rows: GVI, Marine Growth Survey, Anode Survey, CP Readings, USWT, Debris Survey, Scour Survey, Pipeline & Riser Survey, Video Survey, Level 3 Survey, ACFM, Preliminary Reports, Final Reports
- Confirm SOW-specific wording in descriptions (e.g. "Video shall not include cleaning activity, only inspection work"; "PDF preliminary reports within 24 hours of completion of offshore inspections per facility")
- Ask user to confirm any ambiguous SOW wording before writing

### Asset History (Section 4)
Narrative format with two subsections:
- **4.1 Asset Information** — list of fields/facilities, water depth range, access methods, nearest ports — sourced from SOW
- **4.2 Asset History** — per-field narrative: discovery year, first production year, platform vintage, water depth. Notable integrity context (aging infrastructure, environmental conditions). Reference SOW marine conditions (visibility, currents, seabed type). Use Perplexity (`sonar-pro` model, API key from memory) for public-domain field data (discovery years, platform ages) but NEVER override SOW data.

### Organisational Chart
Mermaid flowchart with `:::classname` tags on EVERY node:
- Color classes must be defined and applied. The user will correct if classes are missing.
- Standard classes from Atlantic Marine examples: `onshore` (dark navy), `Sky` (deep blue), `Ash` (dark grey), `main` (steel blue), `combination` (purple), `Aqua` (teal), `sub` (dark slate)
- All nodes need font-size 26-28px, white text on dark backgrounds
- Client team (CNL) gets `Sky` class, separate subgraph
- Onshore → Offshore arrow, plus Client ↔ OffshoreMgr dotted line
- Typical roles: Managing Director, Executive Directors, HSE Manager, HR, DPA, Project Coordinator, Equipment Manager, Project Manager, Logistics Coordinator, AutoCAD Designer (onshore). Dive Supervisors, Superintendent/OCM (management). Dive Technician, Diver/DMT, Inspection Diver, Construction Diver, Standby Diver, 3.4U Coordinator, Data Recorder, ACFM Technician (diving). Offshore HSE Officer, DSV Master & Deck Crew (safety/logistics). CNL Project Engineer, Site Rep, HSE Rep (client).

### Roles & Responsibilities
Authority/Responsibilities block format matching Atlantic Marine examples:
```
### 5.X [Role Name]

**Authority:**
Reports to [superior].
[Specific authority statements — e.g., "Holds a Letter of Appointment (LOA)", "Sole authority to commence diving operations", "Authorised to prohibit the start or order cessation"]

**Responsibilities:**
[Bulleted or paragraph list of specific duties]
```

### HSE: Key Safety Practices
Bulleted list format. Remove irrelevant items from the example (e.g. ROV-specific if this is diver-only). Add project-specific items:
- Lock Out Tag Out (LOTO)
- Permit to Work (PTW) compliance
- Diver deployment and recovery via LARS
- Mooring operations — [specific anchor type]
- Differential pressure hazards
- Pinch points
- Adherence to approved procedures
- HP water jetting safety
- Diver communications and umbilical management
- HP air and gas system safety
- Adverse weather monitoring
- SIMOPS with producing facilities
- Fatigue management
- Breathing gas quality
- Deck operations and lifting safety
- Non-spark tool use in hydrocarbon areas
- Hydrocarbon gas detection
- Emergency response and diver recovery drills
- Stop-work authority

### HSE: Key Steps / Key Dangers / Key Mitigations
Three-subsection format:
**Key Steps** (numbered bullet list of operational sequence: mob → familiarisation → PTW → comms check → HIRA → weather check → LOTO → Alpha flag → reporting → demob)
**Key Dangers** (bullet list: weather, miscommunication, diving risks, equipment failure, vessel traffic, SIMOPS)
**Key Mitigations** (bullet list: PTW, TBT, comms, LOTO, weather monitoring, exclusion zone, standby diver, stop-work authority)

### Permit to Work (PTW) Section
Dual-system explanation:
- **Primary — Client PTW**: When operating on or adjacent to client facilities, the client's PTW takes precedence. Defines scope, hazards, controls, isolations, SIMOPS coordination. No dive without signed PTW from client facility rep.
- **Secondary — Vessel PTW**: During transit, anchoring, equipment setup outside client footprint. Covers deck lifts, hot work, confined space, maintenance. Must meet IMCA D 014 minimum.
- **PTW Interface**: Diving Supervisor holds both as applicable. Hierarchy: Client PTW → Vessel PTW → Both where scopes overlap. More stringent governs.

### Weather / Environmental Conditions (Section 10)
Three-subsection format:
- **10.1.1 Operational Area Climate** — Narrative description from SOW (swell patterns, seasonal weather, tidal currents, visibility). Quote or paraphrase the SOW directly.
- **10.1.2 Operational Weather Limits** — Table with columns: Activity | Max Swell/Wave Height | Max Wind Speed | Max Current. Typical rows: Personnel transfer, Vessel mooring, Diver deployment and diving activity.
- **10.1.3 Weather Monitoring & Decision-Making** — Radar watch (16nm), squall reporting protocol (VHF, 10nm trigger), Diving Supervisor override authority.
- **10.1.4 Seasonal Planning** — Per SOW: dry season (Nov-May, CONTRACTOR weather risk) vs wet season (May-Oct, COMPANY pays after 12hrs). Slack tide planning for current-limited operations.

## Scope of Work Format

Use TWO tables matching the user's template exactly:

**Table 1 — General Activities** (columns: `#️⃣ | 🏗️ Activity | 📝 Description`)
- Numbered rows 1-10: Project Management & Documentation, Pre-Mobilisation Inspection, Equipment Mobilisation, Personnel Mobilisation, Community Marine Equipment Engagement, Facility Entry & LOTO, HIRA Level 1 & 2, Kick-off Meeting, Daily Reporting & Communications, Demobilisation
- Each row has bullet-point sub-items in the Description column

**Table 2 — Inspection Activities** (columns: `#️⃣ | 🔎 Activity | 📋 Key Tasks`)
- Numbered rows 1-13: GVI, Marine Growth Survey, Anode Survey, CP Readings, USWT, Debris Survey, Scour Survey, Pipeline & Riser Survey, Video Survey, Level 3 Survey, ACFM, Preliminary Field Reporting, Final Inspection Report
- Confirm specific SOW wording: "Video shall not include cleaning activity, only inspection work" and "PDF preliminary reports within 24 hours of completion of offshore inspections per facility"

## Introduction Pattern (Section 2)

5-paragraph exact structure:
1. "[Contractor] have been contracted by [Client], to provide [services] for [project] across [specific fields/areas], in water depths ranging from [X] to [Y] metres."
2. "This involves risk-assessed underwater inspections, surveys and non-destructive testing (NDT) on critical structural components of [facilities] in accordance with [standards], to ensure safe and continued operations of the producing asset base."
3. "The scope complies fully with [list standards — API, IMCA, ISO, Client-specific]... Non-destructive testing for Level 3 inspections will be carried out using Alternating Current Field Measurement (ACFM) as the primary technique in response to the poor-to-zero visibility conditions typical of the operating area."
4. "All diving operations will be performed from a Client-approved Dive Support Vessel (DSV) with [mooring/DP capability], utilising a Launch and Recovery System (LARS) for diver deployment and a Scuba Replacement Package (SRP) system for shallow-water and auxiliary access, and shall be conducted in strict compliance with all applicable company policies and procedures approved by [Client]."
5. "The safe execution and efficiency of operations is of the essence to allow [Client]'s facilities to remain in production while inspections are performed with minimal disruption to ongoing operations."

## Asset History Section (Section 4)

Two subsections:
- **4.1 Asset Information** — List fields/facilities per SOW, water depth range, access methods, nearest ports
- **4.2 Asset History** — Per-field narrative: discovery year, first production, platform vintage, notable integrity context (aging infrastructure). Reference SOW marine conditions (visibility, currents, seabed). Use Perplexity API (`sonar-pro` model) for public-domain field data — but NEVER override SOW data.

## Organigram

Mermaid flowchart with `:::classname` tags on EVERY node. Standard classes from Atlantic Marine examples:
- `onshore` (dark navy) — Managing Director
- `Sky` (deep blue) — Executive Directors, CNL client team
- `Ash` (dark grey) — Equipment Manager, DPA, Logistics, AutoCAD
- `main` (steel blue) — HSE Manager, Dive Supervisors, Vessel Crew
- `combination` (purple) — HR Officer, Offshore HSE
- `Aqua` (teal) — Project Coordinator
- `sub` (dark slate) — PM, OCM, dive team, inspection team

All nodes need font-size 26-28px, white text on dark backgrounds.
Client team gets a separate subgraph with Sky class.

## HSE: Key Steps / Key Dangers / Key Mitigations

Three-subsection format matching Atlantic Marine examples:

**Key Steps:** (ordered bullet list: Mobilisation → PTW → Safety Brief → Comms Check → HIRA Level 2 → Weather Check → LOTO → Alpha Flag → Reporting → Demob)

**Key Dangers:** (bullet list: Weather/tidal conditions, Miscommunication, Diving risks — DP, pinch points, umbilical entanglement, poor visibility, Equipment failure, Vessel traffic in 500m zone, SIMOPS hazards)

**Key Mitigations:** (bullet list: PTW process, TBT at shift change, Comms checks, LOTO verified by Diving Supervisor, Weather monitoring with defined limits, 500m exclusion zone, Alpha flag + radio broadcast, Standby diver, Stop-work authority)

## Permit to Work Section Format

Dual-system explanation with three subsections:
1. **CNL Permit to Work (Primary)** — when on/adjacent to CNL facilities. Defines scope, hazards, controls, isolations, SIMOPS. No dive without signed PTW from CNL facility rep.
2. **Vessel PTW (Secondary)** — transit, anchoring, equipment setup outside CNL footprint. Covers deck lifts, hot work, confined space, maintenance. IMCA D 014 minimum.
3. **PTW Interface** — Diving Supervisor holds both. Hierarchy: CNL PTW → Vessel PTW → Both. More stringent governs.

## Weather Section Format

Four subsections:
- **10.1.1 Operational Area Climate** — SOW-derived narrative (swell, squalls, currents, visibility, seasonal patterns)
- **10.1.2 Operational Weather Limits** — Table: Activity | Max Swell/Wave | Max Wind | Max Current (3 rows: Personnel transfer, Vessel mooring, Diver deployment)
- **10.1.3 Weather Monitoring & Decision-Making** — 16nm radar, 10nm squall rule, Diving Supervisor override authority
- **10.1.4 Seasonal Planning** — Per SOW: dry season Nov-May (CONTRACTOR risk) vs wet season May-Oct (COMPANY pays after 12hrs). Slack tide planning.

## Mobilisation Section Format

Follow the FPSO/Atlantic Marine example pattern but adapt to the actual project:
- Port/location for loading (e.g. Warri or Onne jetty)
- Pre-mob inspection per client procedure
- Equipment listing — specific to inspection scope (no ROV unless in SOW)
- Community marine equipment procurement via PGPA
- Personnel routing from support base to worksite
- Training requirements (BOSIET, OE, PTW)
- Reference vessel spec sheet and mob/demob procedure

## Roles Section Format

Each role follows this exact block format from Atlantic Marine examples:

```
### X.X [Role Name]

**Authority:**
Reports to [superior].
[Holds Letter of Appointment (LOA) where applicable]
[Specific authority statements]

**Responsibilities:**
[Paragraph or bullet list of duties]
```

## Gap Analysis Workflow

When asked to compare PEP against SOW:
1. Extract all SOW requirements section by section
2. Cross-reference against PEP content
3. Categorise into: Missing from PEP, Partially Covered, Covered
4. Present as a table with SOW reference, requirement, and status
5. Summarise top 10 items to add

## SOW Attachment Cross-Reference

Build a table of all 13+ attachments from the SOW and mark which are referenced in the PEP. Flag missing ones.

## Delivery Iteration Pattern

1. User asks for a section → produce it in the chat
2. User may correct the format → adjust and re-deliver
3. Only after user says "put it in the document" should you write to the .docx
4. When user provides their own example format, match it exactly — column headers, emojis, numbering, table layout

## Research Sources
- Perplexity API key is stored in memory as `PERPLEXITY_API_KEY` — use `sonar-pro` model for asset history, field data, and regulatory research
- SOW tender document is the authoritative source — Perplexity is supplementary for public-domain context (discovery years, field names, platform vintages)
- Never override SOW data with Perplexity results — if SOW says 2m-60m and Perplexity says "30-400m", the SOW wins

## Pitfalls
- Do NOT produce a generic PEP template — the user wants specific operational answers
- When data isn't in the SOW, use `[TBC]` or `[Contractor to Confirm]` — do not fabricate
- Keep step-by-step inspection methodology HIGH-LEVEL — enough for tender, not enough for client to reuse as their own procedure
- Always propose ACFM over MPI for low-visibility environments, with rationale from the SOW itself
- The user will walk through section by section — accept corrections and iterate, don't defend the first pass
- Vessel name, team composition, and specific contractor capabilities are the user's input — ask explicitly
- Do NOT auto-update the .docx — produce content in the interface for the user to paste themselves
- Contract number, dates, and company name are placeholders — tag them clearly
- When the user says "give me the answers here in the interface" — stop writing to documents and deliver in chat
- Patch the `generate_pep.py` output guard: check if user wants docx output or chat delivery before generating
