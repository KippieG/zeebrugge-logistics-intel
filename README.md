# Zeebrugge Port Tech Intelligence

An executive-ready intelligence repo that turns public Zeebrugge port-logistics signals into structured datasets, technology-stack hypotheses, scraped source evidence and commercial software opportunities.

[![Validate dataset](https://github.com/KippieG/zeebrugge-logistics-intel/actions/workflows/validate.yml/badge.svg)](https://github.com/KippieG/zeebrugge-logistics-intel/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/KippieG/zeebrugge-logistics-intel/actions/workflows/pages.yml/badge.svg)](https://github.com/KippieG/zeebrugge-logistics-intel/actions/workflows/pages.yml)

![Zeebrugge Port Tech Intelligence dashboard hero](docs/assets/zeebrugge-intelligence-hero.png)

**Live dashboard:** https://kippieg.github.io/zeebrugge-logistics-intel/  
**Snapshot date:** 2026-06-02  
**Scope:** Zeebrugge-focused logistics ecosystem, with Port of Antwerp-Bruges context  
**What this is:** market intelligence, data modeling, source scraping, tech-stack inference and commercial opportunity mapping in one portfolio project

## Project Labels

![Market Intelligence](https://img.shields.io/badge/market-intelligence-1f6f5b?style=for-the-badge)
![Port Operations](https://img.shields.io/badge/port-operations-1f7f8f?style=for-the-badge)
![Web Scraping](https://img.shields.io/badge/web-scraping-b05b35?style=for-the-badge)
![Data Validation](https://img.shields.io/badge/data-validation-566b7a?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/github-pages-24302b?style=for-the-badge)
![Playwright QA](https://img.shields.io/badge/playwright-QA-1f6f5b?style=for-the-badge)

![Tech Stack Mapping](https://img.shields.io/badge/tech--stack-mapping-1f7f8f?style=for-the-badge)
![Customs Workflows](https://img.shields.io/badge/customs-workflows-b05b35?style=for-the-badge)
![Yard Visibility](https://img.shields.io/badge/yard-visibility-1f6f5b?style=for-the-badge)
![Supply Chain](https://img.shields.io/badge/supply-chain-566b7a?style=for-the-badge)
![Commercial Analysis](https://img.shields.io/badge/commercial-analysis-24302b?style=for-the-badge)

## What I Built

- Collected, registered and scraped **33 public sources** into reviewable source extracts.
- Modeled **9 structured datasets** with source IDs, confidence labels and automated validation.
- Translated public signals into **5 commercial software opportunities** for logistics-tech buyers.

## The Short Version

Zeebrugge is a dense logistics gateway with automotive/RoRo, UK-Ireland shortsea, container handling, intermodal warehousing, customs workflows and LNG/energy logistics. That mix creates recurring operational pain around visibility, release status, yard coordination, document flow and data interoperability.

This repo maps that ecosystem from public sources and turns it into:

- a polished GitHub Pages intelligence dashboard
- 20 seed companies and platforms
- 33 registered public sources
- 33 scraped text extracts
- 9 structured CSV datasets
- 6 port-logistics technology layers
- 5 commercial software opportunity areas
- validation scripts, CI checks and Playwright visual smoke tests

The result is not just a list of companies. It is a repeatable research system that shows how public information can become a useful commercial view of a logistics market.

## Why This Repo Stands Out

This project is built to show end-to-end ownership, not only research.

| Capability | What the repo proves |
| --- | --- |
| Market research | Finds useful signals in port, terminal, APZI, company, job, registry and platform sources. |
| Data engineering | Normalizes findings into CSV datasets with source IDs, confidence labels and validation rules. |
| Scraping | Captures text extracts from seed URLs and keeps scraped evidence available for review. |
| Tech-stack analysis | Separates observed platform signals from inferred operational systems such as TOS, YMS, WMS, TMS, EDI and APIs. |
| Commercial thinking | Converts findings into buyer segments, pain signals, product angles and go-to-market notes. |
| Delivery quality | Ships a dashboard, README, reports, scripts, CI validation and visual smoke tests. |

For a recruiter, this shows practical execution.  
For a manager, it shows judgment and communication.  
For a commercial team, it shows how research can point toward real software opportunities.

## Key Findings

### 1. The strongest technology signals are ecosystem-level

The clearest verified stack signals sit around the port-community and data-sharing layer:

- **APICS** for port/vessel operational information
- **ZEDIS** as a Zeebrugge port-community system signal
- **NxtPort / RX-SeaPort** for data sharing and customs-related coordination
- **IRP** for import release and customs digitization across Belgian ports
- **APICA digital twin**, smart cameras, ETA tooling and terminal APIs from Port of Antwerp-Bruges

This matters because software vendors should not treat each company as an isolated island. The commercial opportunity is often about integrating with the port data layer, not replacing it.

### 2. Company-level operational stacks are mostly hidden

Most terminals, forwarders and logistics operators do not publicly name their operational software vendors. The repo therefore avoids overclaiming.

Instead, each company is scored using:

- `observed`: a public source names the system, platform, product or vendor
- `inferred`: the operational stack is likely from the business activity, but no vendor is named
- `unknown`: no reliable public signal was found

Example: ECS / 2XL has an observed Microsoft Analytics / Reporting Services signal. Many other operators likely use TOS, YMS, WMS, TMS, EDI, gate tooling or customs systems, but those are marked as inferred unless the source evidence is explicit.

### 3. Zeebrugge has strong software pain around visibility and customs

The repeated operational themes are:

- vehicle, trailer and container dwell time
- yard location and handover status
- customs release and missing-document workflows
- UK/Ireland shortsea complexity
- terminal gate coordination
- rail, warehouse and labor planning
- API/data readiness for shippers and partners

That makes Zeebrugge a useful research beachhead for logistics-tech vendors, because the same structure can be reused for Antwerp, Rotterdam, Hamburg, Dunkirk or other North Sea logistics clusters.

### 4. Webtech scans are useful, but not enough

The lightweight scanner found visible web-channel signals such as Drupal, WordPress, Next.js, React, Cloudflare, Google Tag Manager, Cookiebot and OneTrust.

These are not proof of operational systems. They are useful digital-maturity signals, but they must be combined with job postings, vendor cases, registry data, interviews and platform evidence before being used commercially.

### 5. APZI confirms ecosystem density, but not a clean full export

Public APZI pages confirm a broader Zeebrugge port-company ecosystem and expose categories, board/segment representation and visible member-page candidates. A complete member database still needs direct APZI/Voka access, browser/API extraction or another official export.

## Dataset At A Glance

| Area | Count | File |
| --- | ---: | --- |
| Seed companies and platforms | 20 | [`data/companies.csv`](data/companies.csv) |
| Public source register | 33 | [`data/sources.csv`](data/sources.csv) |
| Scraped source extracts | 33 | [`data/scraped/`](data/scraped) |
| Port-logistics stack layers | 6 | [`data/stack_taxonomy.csv`](data/stack_taxonomy.csv) |
| Product opportunities | 5 | [`data/opportunities.csv`](data/opportunities.csv) |
| Company enrichment rows | 20 | [`data/company_enrichment.csv`](data/company_enrichment.csv) |
| APZI board/segment signals | 17 | [`data/apzi_board_signals.csv`](data/apzi_board_signals.csv) |
| APZI public-page candidates | 22 | [`data/apzi_member_candidates.csv`](data/apzi_member_candidates.csv) |
| Webtech scan rows | 20 | [`data/web_tech_scan.csv`](data/web_tech_scan.csv) |

## What Was Scraped And Modeled

The source register and scraper focus on public evidence that can support business analysis:

- Port of Antwerp-Bruges digital product pages and port facts
- APICS, ZEDIS, NxtPort, RX-SeaPort and IRP-related sources
- RoRo, deepsea, container, customs, forwarding and warehousing company pages
- APZI public pages and board/member signals
- company contact, VAT/registry and hiring signals where public snippets expose them
- webtech headers, generators, scripts and visible website metadata

Scraped extracts are stored in [`data/scraped/`](data/scraped), so the dataset is reviewable instead of being a black box.

## Company And Stack Map

The company dataset maps operators into practical segments:

| Segment | Example companies/platforms | Likely stack themes |
| --- | --- | --- |
| Port authority and data layer | Port of Antwerp-Bruges, NxtPort / RX-SeaPort | APICS, ZEDIS, IRP, APIs, digital twin, smart cameras |
| Automotive and RoRo | ICO, Wallenius Wilhelmsen, MOSOLF, UECC, C.RO, KESS | TOS, YMS, vehicle inventory, gate OCR, OEM/customer portals |
| Container and deepsea terminals | CSP Zeebrugge Terminal, PSA Zeebrugge | Container TOS, crane/OCR options, EDI/API, rail/barge planning |
| Intermodal and warehousing | ECS / 2XL, NDQ Logistics, DFDS, CLdN | TMS, WMS, BI, rail planning, customs integration, ETA prediction |
| Forwarders, customs and agencies | Alltraco, Dens Ocean, RBZ, Herfurth / M-Star, Notman | Customs declaration software, freight TMS, document automation, APICS/ZEDIS workflows |
| Energy logistics | Fluxys LNG Terminal Zeebrugge | SCADA/OT, nominations, scheduling, safety systems, compliance reporting |

## Complete Tech Stack Tag View

The repo separates operational technology, ecosystem platforms and visible web-channel signals. This keeps the analysis useful without pretending that a public website stack proves the back-office or terminal stack.

| Layer | Tags |
| --- | --- |
| Observed port and data layer | `APICS`, `ZEDIS`, `NxtPort`, `RX-SeaPort`, `IRP`, `Terminal API`, `APICA digital twin`, `smart cameras`, `ETA Terminal Tool` |
| Terminal, yard and transport systems | `TOS`, `YMS`, `VMS`, `gate OCR`, `crane/OCR options`, `vehicle inventory`, `trailer visibility`, `slot booking`, `rail planning`, `TMS`, `WMS`, `EDI/API` |
| Customs, analytics and energy operations | `customs declaration software`, `document automation`, `release-status queues`, `Microsoft Analytics`, `Reporting Services`, `BI dashboards`, `dwell-time models`, `ETA prediction`, `demand forecasts`, `SCADA/OT`, `nominations`, `compliance reporting` |
| Visible web-channel signals | `Drupal`, `WordPress`, `Next.js`, `React`, `Vue`, `Cloudflare`, `Google Tag Manager`, `Google Analytics`, `Cookiebot`, `OneTrust`, `Bootstrap`, `jQuery` |

Observed stack tags are strongest around the port-community layer. Inferred tags are operationally plausible from the company segment and should be validated through interviews, job postings, vendor cases or direct system evidence.

## Commercial Opportunity Map

The analysis points toward five software opportunities that are narrow enough to be useful and broad enough to be commercially interesting.

| Opportunity | Buyer logic | Product angle |
| --- | --- | --- |
| Yard visibility | RoRo, automotive, trailer and overflow operations need clearer dwell, location and release status. | Overlay existing TOS/YMS instead of replacing it. |
| Customs automation | UK/Ireland and port-community workflows create repeated document and release-status friction. | Build around IRP, NxtPort and RX-SeaPort workflows. |
| ETA and capacity forecasting | Terminals, warehouses and rail planners need predictions tied to gates, labor and capacity. | Forecast dwell risk, gate peaks, rail slots and warehouse load. |
| Sales intelligence | Vendors need a way to prioritize accounts by likely pain and digital maturity. | Score companies by segment, public tech signals, hiring signals and confidence. |
| API/data readiness audit | Operators and shippers need to know where clean event data can be exposed. | Assess integration gaps and recommend API/event-data roadmap steps. |

## Dashboard

The GitHub Pages dashboard in [`docs/`](docs/index.html) turns the research into a visual commercial story:

- executive hero and positioning
- dataset coverage metrics
- manager-facing business interpretation
- technology-signal cards
- company stack matrix
- stack taxonomy
- software opportunity map
- method and artifact links

Live page: https://kippieg.github.io/zeebrugge-logistics-intel/

### Dashboard Screenshots

![Dashboard hero screenshot](docs/assets/dashboard-hero-screenshot.png)

![Full tech-stack tag screenshot](docs/assets/dashboard-stack-tags-screenshot.png)

![Company stack matrix screenshot](docs/assets/dashboard-stack-matrix-screenshot.png)

![Opportunity map screenshot](docs/assets/dashboard-opportunity-screenshot.png)

## Research Outputs

- [`reports/executive-brief.md`](reports/executive-brief.md): one-page manager summary with top findings, opportunities, risks and recommended next research.
- [`reports/analysis.md`](reports/analysis.md): executive take, market map, technology signals, gaps and 2026 outlook.
- [`reports/opportunity-playbook.md`](reports/opportunity-playbook.md): practical product and sales hypotheses for yard visibility, customs automation, forecasting and API readiness.
- [`reports/enrichment-guide.md`](reports/enrichment-guide.md): workflow for APZI expansion, webtech checks, job signals, registry research and contact-role mapping.
- [`data/research_backlog.csv`](data/research_backlog.csv): next research workstreams and status tracking.

## Reproduce The Workflow

Install local tooling:

```sh
npm install
npx playwright install chromium
```

Validate all structured datasets:

```sh
npm run validate:data
```

Run the full local check, including Playwright visual smoke tests:

```sh
npm run check
```

Refresh source extracts:

```sh
npm run scrape:sources
```

Run enrichment scripts:

```sh
npm run scrape:apzi
npm run scan:webtech
```

## Quality Gates

The repo includes automated checks so the project stays presentable:

- `scripts/validate_dataset.py` checks CSV headers, duplicate records, confidence values, source references and scraped extract coverage.
- Playwright verifies that the dashboard renders on desktop and mobile without layout overflow.
- GitHub Actions runs dataset validation and visual smoke tests on pushes.
- GitHub Pages deploys the static dashboard from `docs/`.

## Methodology

The analysis is intentionally conservative:

- Public source evidence is stored and linked by source ID.
- Operational software stacks are not claimed as fact unless a public source names them.
- Inferred systems are labeled as inferred and should be validated before commercial use.
- Webtech findings are treated as digital-channel signals, not proof of back-office or terminal operations software.
- The opportunity map is a hypothesis map, not validated customer discovery.

For investment, sales or partnership decisions, validate the findings with company interviews, official filings, job postings, vendor case studies, Wappalyzer/BuiltWith, procurement data and direct outreach.

## Repository Structure

```text
.
├── data/                  # CSV datasets and scraped source extracts
├── docs/                  # Static GitHub Pages dashboard and visual assets
├── reports/               # Analysis, playbook and enrichment guide
├── scripts/               # Scraping, enrichment and validation scripts
├── tests/                 # Playwright visual smoke tests
└── .github/workflows/     # Dataset validation and Pages deployment
```

## Next Research Moves

- Pull a full APZI member export through browser/API inspection or direct APZI/Voka access.
- Run manual Wappalyzer/BuiltWith checks and compare them with [`data/web_tech_scan.csv`](data/web_tech_scan.csv).
- Add job-posting evidence for ERP, TMS, WMS, BI, cloud, cybersecurity and terminal-planning vendors.
- Verify VAT, registry and financial signals through official KBO/BCE and NBB sources.
- Add role-level outreach mapping for operations, IT, customs, terminal planning and commercial teams.
- Repeat the same research pattern for another logistics cluster to prove transferability.
