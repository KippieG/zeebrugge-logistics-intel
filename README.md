# Zeebrugge Logistics Intel

Public market-intelligence snapshot of logistics companies, terminal operators, and digital infrastructure around Zeebrugge / Port of Antwerp-Bruges.

This project combines desk research, source scraping, and structured analysis to map where logistics-tech opportunities are likely to sit: yard visibility, customs digitization, terminal orchestration, intermodal planning, and data interoperability.

**Snapshot date:** 2026-06-02  
**Scope:** Zeebrugge-focused logistics ecosystem, with Port of Antwerp-Bruges context  
**Status:** Portfolio-ready research prototype, not a complete commercial database

## Project Outputs

- [Portfolio page](docs/index.html): static GitHub Pages-ready project overview.
- [Company dataset](data/companies.csv): 20 seed companies/platforms with service categories and public tech-stack signals.
- [Source register](data/sources.csv): 33 public sources used for the current snapshot.
- [Stack taxonomy](data/stack_taxonomy.csv): reusable map of port-logistics technology layers.
- [Opportunity dataset](data/opportunities.csv): product opportunities, buyer segments, pain signals, and go-to-market notes.
- [Company enrichment](data/company_enrichment.csv): webtech, job, VAT/registry, financial and contact-role signals.
- [Webtech scan](data/web_tech_scan.csv): lightweight local scan of public company domains.
- [APZI board signals](data/apzi_board_signals.csv): APZI segment representation mapped to tech relevance.
- [APZI member candidates](data/apzi_member_candidates.csv): visible-text extraction from the public APZI members page.
- [Scraped extracts](data/scraped): text extracts generated from the source register.
- [Analysis report](reports/analysis.md): market map, technology signals, opportunities, and 2026 outlook.
- [Opportunity playbook](reports/opportunity-playbook.md): practical product and sales hypotheses derived from the dataset.
- [Enrichment guide](reports/enrichment-guide.md): workflow for APZI expansion, webtech checks, job signals, registry research and contact-role mapping.
- [Scraper](scripts/scrape_seed.py): dependency-free Python scraper for the seed URLs.
- [APZI extractor](scripts/extract_apzi_members.py): conservative visible-text extractor for APZI member/category pages.
- [Webtech detector](scripts/detect_web_tech.py): lightweight website fingerprint collector.
- [Dataset validator](scripts/validate_dataset.py): dependency-free consistency checks for company rows, source IDs, and scraped extracts.

## Why This Is Useful

Zeebrugge is a specialized logistics gateway with strong activity in:

- Automotive and RoRo logistics
- UK/Ireland shortsea and intermodal flows
- Container and paper logistics
- LNG and energy logistics
- Customs, forwarding, and shipping agency workflows

The most visible technology layer is ecosystem-level rather than company-level: APICS, ZEDIS, NxtPort/RX-SeaPort, IRP, APICA digital twin, smart cameras, and terminal APIs. Company-level stacks are often inferred from operations unless vendors are publicly named.

## Repository Structure

```text
.
├── data/
│   ├── companies.csv
│   ├── company_enrichment.csv
│   ├── opportunities.csv
│   ├── apzi_board_signals.csv
│   ├── apzi_member_candidates.csv
│   ├── sources.csv
│   ├── stack_taxonomy.csv
│   ├── research_backlog.csv
│   ├── web_tech_scan.csv
│   └── scraped/
├── docs/
│   ├── index.html
│   └── styles.css
├── reports/
│   ├── analysis.md
│   ├── enrichment-guide.md
│   └── opportunity-playbook.md
└── scripts/
    ├── detect_web_tech.py
    ├── extract_apzi_members.py
    ├── scrape_seed.py
    └── validate_dataset.py
```

## Run The Scraper

```sh
python3 scripts/scrape_seed.py
```

Latest scrape result:

- 33 seed sources attempted.
- 31 sources produced text extracts.
- 2 temporary failures were captured as error extracts: Notman Logistics returned HTTP 503; one industry-news source failed DNS resolution locally.
- APZI confirms roughly 160 Zeebrugge port companies, but its public member page exposes mostly categories/search UI to this simple HTML scraper. A complete member export needs browser/API scraping or direct APZI data.

## Run Enrichment Scripts

```sh
python3 scripts/extract_apzi_members.py
python3 scripts/detect_web_tech.py
```

The APZI extractor writes conservative visible-text candidates rather than claiming a full member export. The webtech detector is not a Wappalyzer replacement; it records reproducible local signals from headers, scripts and generator tags.

## Validate The Dataset

```sh
python3 scripts/validate_dataset.py
```

The validator checks required CSV headers, duplicate records, confidence values, company-to-source references, opportunity priorities, stack-taxonomy structure, and scraped extract coverage.

## Methodology

Tech-stack labels are deliberately conservative:

- `observed`: explicitly mentioned in public sources, for example NxtPort, APICS, ZEDIS, IRP, Microsoft Analytics.
- `inferred`: operationally likely from services such as terminal operations, customs, warehousing, intermodal planning, or track-and-trace.
- `unknown`: no reliable public signal found.

For investment, sales, or partnership decisions, validate inferred tech stacks with job postings, vendor case studies, Wappalyzer/BuiltWith, procurement data, company interviews, or direct outreach.

## Portfolio Angle

This repo demonstrates:

- Market research from public sources
- Structured CSV data modeling
- Lightweight scraping without dependencies
- Dataset validation and reproducibility
- Logistics-domain analysis
- Clear separation between observed facts and inferred signals
- A static data-story page suitable for GitHub Pages

## Next Improvements

- Add APZI member export through browser/API scraping or direct data access.
- Add job-posting signals for ERP, TMS, WMS, BI, cloud, and cybersecurity vendors.
- Add Wappalyzer/BuiltWith checks for company web stacks.
- Add Belgian registry identifiers, VAT numbers, financial signals, and contact roles.
