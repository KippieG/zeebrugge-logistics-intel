# Zeebrugge Logistics Intel

Publieke marktintelligentie over logistieke bedrijven, terminal operators en digitale/operationele tech rond Zeebrugge / Port of Antwerp-Bruges.

Status: eerste desk-research snapshot op 2026-06-02.

## Inhoud

- `data/companies.csv`: seed-lijst van belangrijke spelers met diensten, publieke tech-signalen en inschatting.
- `data/sources.csv`: gebruikte publieke bronnen.
- `reports/analysis.md`: analyse, kansen, risico's en vooruitzicht.
- `scripts/scrape_seed.py`: eenvoudige scraper voor seed-URLs zonder externe Python dependencies.

## Gebruik

```sh
python3 scripts/scrape_seed.py
```

De scraper schrijft ruwe tekstextracten naar `data/scraped/`. Gebruik die output om de CSV verder aan te vullen of om sales/marktanalyses te maken.

Laatste scrape-resultaat:

- 23 seed-bronnen geprobeerd.
- 22 bronnen met tekstextract.
- 1 tijdelijke failure: Notman Logistics gaf HTTP 503.
- APZI bevestigt circa 160 Zeebrugse havenbedrijven, maar de publieke ledenpagina geeft in deze eenvoudige HTML-scrape vooral categorieën/zoekinterface. Voor een volledige ledenlijst is een browser/API-scrape of directe APZI-export nodig.

## Belangrijke beperking

Tech stacks van logistieke bedrijven zijn zelden volledig publiek. Dit project maakt daarom onderscheid tussen:

- `observed`: expliciet publiek genoemd, bijvoorbeeld NxtPort, APICS, ZEDIS, IRP, Zscaler, Microsoft Analytics.
- `inferred`: logisch afgeleid uit diensten zoals customs, terminal operations, warehousing, intermodal planning of track-and-trace.
- `unknown`: geen betrouwbaar publiek signaal gevonden.

Voor commerciële beslissingen moeten inferred tech stacks worden gevalideerd via vacatures, klantcases, Wappalyzer/BuiltWith, aanbestedingen, vendor-case studies of directe interviews.
