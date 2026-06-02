# Zeebrugge Logistics Intel

Public market-intelligence snapshot of logistics companies, terminal operators, and digital infrastructure around Zeebrugge / Port of Antwerp-Bruges.

This project combines desk research, source scraping, and structured analysis to map where logistics-tech opportunities are likely to sit: yard visibility, customs digitization, terminal orchestration, intermodal planning, and data interoperability.

**Snapshot date:** 2026-06-02  
**Scope:** Zeebrugge-focused logistics ecosystem, with Port of Antwerp-Bruges context  
**Status:** Portfolio-ready research prototype, not a complete commercial database

## Project Outputs

- [Portfolio page](docs/index.html): static GitHub Pages-ready project overview.
- [Company dataset](data/companies.csv): 20 seed companies/platforms with service categories and public tech-stack signals.
- [Source register](data/sources.csv): 23 public sources used for the first snapshot.
- [Scraped extracts](data/scraped): text extracts generated from the source register.
- [Analysis report](reports/analysis.md): market map, technology signals, opportunities, and 2026 outlook.
- [Scraper](scripts/scrape_seed.py): dependency-free Python scraper for the seed URLs.

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
│   ├── sources.csv
│   └── scraped/
├── docs/
│   ├── index.html
│   └── styles.css
├── reports/
│   └── analysis.md
└── scripts/
    └── scrape_seed.py
```

## Run The Scraper

```sh
python3 scripts/scrape_seed.py
```

Latest scrape result:

- 23 seed sources attempted.
- 22 sources produced text extracts.
- 1 temporary failure: Notman Logistics returned HTTP 503.
- APZI confirms roughly 160 Zeebrugge port companies, but its public member page exposes mostly categories/search UI to this simple HTML scraper. A complete member export needs browser/API scraping or direct APZI data.

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
- Logistics-domain analysis
- Clear separation between observed facts and inferred signals
- A static data-story page suitable for GitHub Pages
