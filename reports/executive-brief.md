# Executive Brief: Zeebrugge Port Tech Intelligence

Snapshot date: 2026-06-02

## 1-Page Executive Summary

Zeebrugge is a compact but commercially rich logistics cluster inside the Port of Antwerp-Bruges ecosystem. Its mix of automotive/RoRo, UK-Ireland shortsea, container handling, intermodal warehousing, customs activity and LNG/energy logistics creates repeated operational friction around visibility, release status, document flow, yard coordination and data interoperability.

This project turns public-source signals into a structured intelligence product: company mapping, scraped source extracts, technology-stack taxonomy, enrichment signals, opportunity analysis and a visual dashboard. The main business value is not only the dataset, but the translation layer from public evidence to buyer segments, operational pain and software hypotheses.

## Top 5 Findings

1. **The strongest verified stack signals are ecosystem-level.** APICS, ZEDIS, NxtPort/RX-SeaPort, IRP, APICA digital twin, smart cameras and terminal API tooling are clearer than most company-level vendor disclosures.
2. **Company operational stacks are mostly not publicly named.** TOS, YMS, WMS, TMS, EDI/API and customs software are often inferred from operational activity rather than directly observed.
3. **Yard visibility and release-status clarity are recurring pains.** RoRo, automotive, trailer, terminal and warehouse flows all create value for better dwell, handover and exception visibility.
4. **Customs workflows are becoming platform-led.** IRP and NxtPort/RX-SeaPort suggest that future tools should integrate with the port-community layer instead of building isolated document portals.
5. **Webtech signals help with maturity scoring, but are not operational proof.** Drupal, WordPress, Next.js, React, Cloudflare, Google Tag Manager, Cookiebot and OneTrust indicate digital-channel maturity, not terminal or back-office stack confirmation.

## Top 5 Opportunities

| Opportunity | Best-fit buyers | Why it matters |
| --- | --- | --- |
| Yard visibility | RoRo terminals, automotive yards, trailer yards, warehouses | Reduces uncertainty around dwell, location, release and handover status. |
| Customs automation | Forwarders, customs brokers, UK/Ireland operators, shipping agents | Reduces repeated manual checks, missing-document friction and release chasing. |
| ETA and dwell-time forecasting | Terminals, warehouses, transport planners, ferry operators | Turns vessel, gate, rail and warehouse signals into operational decisions. |
| Sales intelligence | SaaS vendors, consultants, integrators, investors | Prioritizes accounts by segment, pain likelihood, digital maturity and source evidence. |
| API/data readiness audit | Terminal operators, forwarders, shipper-facing logistics companies | Shows which operators can expose reliable event data and where integration gaps remain. |

## Risks And Unknowns

- APZI public pages do not expose a clean full member export through simple HTML scraping.
- Many operational stack labels remain inferred until validated by interviews, job postings, vendor cases or direct system evidence.
- Webtech scans can identify public website technology, but they do not prove TOS/WMS/TMS or operational architecture.
- VAT, registry and financial signals need official KBO/BCE and NBB verification before commercial use.
- Opportunity sizing is hypothesis-driven and needs customer discovery before product investment.

## Recommended Next Research

1. Pull a full APZI member export through direct APZI/Voka access or browser/API inspection.
2. Run Wappalyzer/BuiltWith checks and compare them with the lightweight webtech scan.
3. Add job-posting signals for ERP, TOS, TMS, WMS, BI, cloud, cybersecurity, EDI and terminal planning.
4. Verify registry, VAT and financial signals through official Belgian sources.
5. Interview or directly validate a small sample of operators across RoRo, forwarding, warehousing, customs and terminal segments.
6. Repeat the same research model for Antwerp, Rotterdam, Hamburg or Dunkirk to prove transferability.
