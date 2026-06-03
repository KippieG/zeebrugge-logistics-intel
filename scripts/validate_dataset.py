#!/usr/bin/env python3
"""
Validate the seed dataset and source register.

The checks stay dependency-free so they can run in CI or on a clean machine.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPANIES = ROOT / "data" / "companies.csv"
SOURCES = ROOT / "data" / "sources.csv"
SCRAPED = ROOT / "data" / "scraped"
STACK_TAXONOMY = ROOT / "data" / "stack_taxonomy.csv"
OPPORTUNITIES = ROOT / "data" / "opportunities.csv"
COMPANY_ENRICHMENT = ROOT / "data" / "company_enrichment.csv"
APZI_BOARD_SIGNALS = ROOT / "data" / "apzi_board_signals.csv"
RESEARCH_BACKLOG = ROOT / "data" / "research_backlog.csv"
APZI_MEMBER_CANDIDATES = ROOT / "data" / "apzi_member_candidates.csv"
WEB_TECH_SCAN = ROOT / "data" / "web_tech_scan.csv"
COMPANY_STACK_SIGNALS = ROOT / "data" / "company_stack_signals.csv"
FIRECRAWL_TARGETS = ROOT / "data" / "firecrawl_targets.csv"
FIRECRAWL_EVIDENCE = ROOT / "data" / "firecrawl_evidence.csv"
TECH_STACK_VENDOR_RESEARCH = ROOT / "data" / "tech_stack_vendor_research.csv"

COMPANY_FIELDS = {
    "company",
    "category",
    "location_signal",
    "services",
    "tech_stack_public_signal",
    "tech_stack_assessment",
    "confidence",
    "sources",
}

SOURCE_FIELDS = {"id", "title", "url", "source_type", "notes"}
STACK_FIELDS = {"layer", "systems", "where_it_shows_up", "why_it_matters", "evidence_level"}
OPPORTUNITY_FIELDS = {
    "opportunity",
    "buyer_segments",
    "pain_signal",
    "product_angle",
    "go_to_market_notes",
    "priority",
}
ENRICHMENT_FIELDS = {
    "company",
    "domain",
    "web_tech_signal",
    "job_signal",
    "registry_or_vat_signal",
    "financial_signal",
    "contact_roles_signal",
    "enrichment_status",
    "sources",
}
APZI_BOARD_FIELDS = {"segment", "person", "organization", "role_signal", "tech_relevance", "sources"}
BACKLOG_FIELDS = {"workstream", "task", "why_it_matters", "method", "status"}
APZI_MEMBER_FIELDS = {"source_url", "candidate_text", "matched_terms", "status"}
WEB_TECH_FIELDS = {"company", "domain", "status", "signals", "error"}
COMPANY_STACK_FIELDS = {
    "company",
    "segment",
    "observed_stack_tags",
    "inferred_stack_tags",
    "visible_web_tags",
    "job_or_hiring_signal",
    "confidence",
    "source_ids",
}
FIRECRAWL_TARGET_FIELDS = {
    "id",
    "label",
    "url",
    "mode",
    "scope",
    "limit",
    "max_depth",
    "why_it_matters",
    "source_ids",
}
FIRECRAWL_EVIDENCE_FIELDS = {
    "id",
    "firecrawl_action",
    "query_or_target",
    "result_url",
    "evidence_summary",
    "commercial_signal",
    "source_ids",
    "status",
}
TECH_STACK_VENDOR_FIELDS = {
    "stack_family",
    "vendor_or_product",
    "companies_or_segments",
    "evidence_status",
    "why_it_matters",
    "source_ids",
}
CONFIDENCE_VALUES = {"high", "medium", "low"}
PRIORITY_VALUES = {"high", "medium", "low"}
FIRECRAWL_MODES = {"scrape", "crawl"}
FIRECRAWL_STATUSES = {"successful", "attempted", "planned"}
VENDOR_EVIDENCE_STATUSES = {"observed_public", "mixed", "inferred_vendor_family", "category_reference", "research_target"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header row")
        return list(reader)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    companies = read_csv(COMPANIES)
    sources = read_csv(SOURCES)
    stack_layers = read_csv(STACK_TAXONOMY)
    opportunities = read_csv(OPPORTUNITIES)
    enrichment = read_csv(COMPANY_ENRICHMENT)
    apzi_board = read_csv(APZI_BOARD_SIGNALS)
    backlog = read_csv(RESEARCH_BACKLOG)
    apzi_member_candidates = read_csv(APZI_MEMBER_CANDIDATES)
    web_tech_scan = read_csv(WEB_TECH_SCAN)
    company_stack_signals = read_csv(COMPANY_STACK_SIGNALS)
    firecrawl_targets = read_csv(FIRECRAWL_TARGETS)
    firecrawl_evidence = read_csv(FIRECRAWL_EVIDENCE)
    tech_stack_vendor_research = read_csv(TECH_STACK_VENDOR_RESEARCH)

    company_fields = set(companies[0].keys()) if companies else set()
    source_fields = set(sources[0].keys()) if sources else set()
    stack_fields = set(stack_layers[0].keys()) if stack_layers else set()
    opportunity_fields = set(opportunities[0].keys()) if opportunities else set()
    enrichment_fields = set(enrichment[0].keys()) if enrichment else set()
    apzi_board_fields = set(apzi_board[0].keys()) if apzi_board else set()
    backlog_fields = set(backlog[0].keys()) if backlog else set()
    apzi_member_fields = set(apzi_member_candidates[0].keys()) if apzi_member_candidates else set()
    web_tech_fields = set(web_tech_scan[0].keys()) if web_tech_scan else set()
    company_stack_fields = set(company_stack_signals[0].keys()) if company_stack_signals else set()
    firecrawl_target_fields = set(firecrawl_targets[0].keys()) if firecrawl_targets else set()
    firecrawl_evidence_fields = set(firecrawl_evidence[0].keys()) if firecrawl_evidence else set()
    tech_stack_vendor_fields = set(tech_stack_vendor_research[0].keys()) if tech_stack_vendor_research else set()

    if company_fields != COMPANY_FIELDS:
        fail(f"companies.csv fields mismatch: {sorted(company_fields)}", failures)
    if source_fields != SOURCE_FIELDS:
        fail(f"sources.csv fields mismatch: {sorted(source_fields)}", failures)
    if stack_fields != STACK_FIELDS:
        fail(f"stack_taxonomy.csv fields mismatch: {sorted(stack_fields)}", failures)
    if opportunity_fields != OPPORTUNITY_FIELDS:
        fail(f"opportunities.csv fields mismatch: {sorted(opportunity_fields)}", failures)
    if enrichment_fields != ENRICHMENT_FIELDS:
        fail(f"company_enrichment.csv fields mismatch: {sorted(enrichment_fields)}", failures)
    if apzi_board_fields != APZI_BOARD_FIELDS:
        fail(f"apzi_board_signals.csv fields mismatch: {sorted(apzi_board_fields)}", failures)
    if backlog_fields != BACKLOG_FIELDS:
        fail(f"research_backlog.csv fields mismatch: {sorted(backlog_fields)}", failures)
    if apzi_member_fields != APZI_MEMBER_FIELDS:
        fail(f"apzi_member_candidates.csv fields mismatch: {sorted(apzi_member_fields)}", failures)
    if web_tech_fields != WEB_TECH_FIELDS:
        fail(f"web_tech_scan.csv fields mismatch: {sorted(web_tech_fields)}", failures)
    if company_stack_fields != COMPANY_STACK_FIELDS:
        fail(f"company_stack_signals.csv fields mismatch: {sorted(company_stack_fields)}", failures)
    if firecrawl_target_fields != FIRECRAWL_TARGET_FIELDS:
        fail(f"firecrawl_targets.csv fields mismatch: {sorted(firecrawl_target_fields)}", failures)
    if firecrawl_evidence_fields != FIRECRAWL_EVIDENCE_FIELDS:
        fail(f"firecrawl_evidence.csv fields mismatch: {sorted(firecrawl_evidence_fields)}", failures)
    if tech_stack_vendor_fields != TECH_STACK_VENDOR_FIELDS:
        fail(f"tech_stack_vendor_research.csv fields mismatch: {sorted(tech_stack_vendor_fields)}", failures)

    source_ids = {row["id"] for row in sources}
    if len(source_ids) != len(sources):
        fail("sources.csv contains duplicate source ids", failures)

    company_names = [row["company"] for row in companies]
    if len(set(company_names)) != len(company_names):
        fail("companies.csv contains duplicate company names", failures)

    stack_layer_names = [row["layer"] for row in stack_layers]
    if len(set(stack_layer_names)) != len(stack_layer_names):
        fail("stack_taxonomy.csv contains duplicate layer names", failures)

    opportunity_names = [row["opportunity"] for row in opportunities]
    if len(set(opportunity_names)) != len(opportunity_names):
        fail("opportunities.csv contains duplicate opportunity names", failures)

    for row in companies:
        name = row["company"]
        if row["confidence"] not in CONFIDENCE_VALUES:
            fail(f"{name}: invalid confidence '{row['confidence']}'", failures)

        refs = [ref.strip() for ref in row["sources"].split(";") if ref.strip()]
        if not refs:
            fail(f"{name}: no source references", failures)
        for ref in refs:
            if ref not in source_ids:
                fail(f"{name}: unknown source reference '{ref}'", failures)

    for row in opportunities:
        if row["priority"] not in PRIORITY_VALUES:
            fail(
                f"{row['opportunity']}: invalid priority '{row['priority']}'",
                failures,
            )

    company_set = set(company_names)
    for row in enrichment:
        if row["company"] not in company_set:
            fail(f"company_enrichment.csv contains unknown company '{row['company']}'", failures)
        refs = [ref.strip() for ref in row["sources"].split(";") if ref.strip()]
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['company']} enrichment: unknown source reference '{ref}'", failures)

    for row in apzi_board:
        refs = [ref.strip() for ref in row["sources"].split(";") if ref.strip()]
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['organization']} APZI signal: unknown source reference '{ref}'", failures)

    for row in web_tech_scan:
        if row["company"] not in company_set:
            fail(f"web_tech_scan.csv contains unknown company '{row['company']}'", failures)

    stack_signal_companies = [row["company"] for row in company_stack_signals]
    if len(set(stack_signal_companies)) != len(stack_signal_companies):
        fail("company_stack_signals.csv contains duplicate company names", failures)
    missing_stack_signal_companies = sorted(company_set - set(stack_signal_companies))
    if missing_stack_signal_companies:
        fail(
            "company_stack_signals.csv missing companies: "
            f"{', '.join(missing_stack_signal_companies)}",
            failures,
        )
    for row in company_stack_signals:
        if row["company"] not in company_set:
            fail(f"company_stack_signals.csv contains unknown company '{row['company']}'", failures)
        if row["confidence"] not in CONFIDENCE_VALUES:
            fail(
                f"{row['company']} stack signal: invalid confidence '{row['confidence']}'",
                failures,
            )
        refs = [ref.strip() for ref in row["source_ids"].split(";") if ref.strip()]
        if not refs:
            fail(f"{row['company']} stack signal: no source references", failures)
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['company']} stack signal: unknown source reference '{ref}'", failures)

    firecrawl_target_ids = [row["id"] for row in firecrawl_targets]
    if len(set(firecrawl_target_ids)) != len(firecrawl_target_ids):
        fail("firecrawl_targets.csv contains duplicate ids", failures)
    for row in firecrawl_targets:
        if row["mode"] not in FIRECRAWL_MODES:
            fail(f"{row['id']}: invalid Firecrawl mode '{row['mode']}'", failures)
        for field in ("limit", "max_depth"):
            if not row[field].isdigit():
                fail(f"{row['id']}: {field} is not numeric", failures)
        refs = [ref.strip() for ref in row["source_ids"].split(";") if ref.strip()]
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['id']} Firecrawl target: unknown source reference '{ref}'", failures)

    firecrawl_evidence_ids = [row["id"] for row in firecrawl_evidence]
    if len(set(firecrawl_evidence_ids)) != len(firecrawl_evidence_ids):
        fail("firecrawl_evidence.csv contains duplicate ids", failures)
    for row in firecrawl_evidence:
        if row["status"] not in FIRECRAWL_STATUSES:
            fail(f"{row['id']}: invalid Firecrawl evidence status '{row['status']}'", failures)
        refs = [ref.strip() for ref in row["source_ids"].split(";") if ref.strip()]
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['id']} Firecrawl evidence: unknown source reference '{ref}'", failures)

    vendor_keys = [
        (row["stack_family"], row["vendor_or_product"])
        for row in tech_stack_vendor_research
    ]
    if len(set(vendor_keys)) != len(vendor_keys):
        fail("tech_stack_vendor_research.csv contains duplicate stack/vendor rows", failures)
    for row in tech_stack_vendor_research:
        if row["evidence_status"] not in VENDOR_EVIDENCE_STATUSES:
            fail(
                f"{row['stack_family']} / {row['vendor_or_product']}: "
                f"invalid evidence status '{row['evidence_status']}'",
                failures,
            )
        refs = [ref.strip() for ref in row["source_ids"].split(";") if ref.strip()]
        if not refs:
            fail(f"{row['vendor_or_product']}: no vendor research source references", failures)
        for ref in refs:
            if ref not in source_ids:
                fail(f"{row['vendor_or_product']} vendor research: unknown source reference '{ref}'", failures)

    scraped_files = list(SCRAPED.glob("S*.txt"))
    scraped_ids = {path.name.split("_", 1)[0] for path in scraped_files}
    missing_extracts = sorted(source_ids - scraped_ids)
    if missing_extracts:
        fail(f"missing scraped extracts for: {', '.join(missing_extracts)}", failures)

    if failures:
        print("Dataset validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print(
        "Dataset validation passed: "
        f"{len(companies)} companies, {len(sources)} sources, "
        f"{len(stack_layers)} stack layers, {len(opportunities)} opportunities, "
        f"{len(enrichment)} enrichment rows, {len(apzi_board)} APZI board signals, "
        f"{len(apzi_member_candidates)} APZI page candidates, {len(web_tech_scan)} web tech rows, "
        f"{len(company_stack_signals)} company stack rows, "
        f"{len(firecrawl_targets)} Firecrawl targets, {len(firecrawl_evidence)} Firecrawl evidence rows, "
        f"{len(tech_stack_vendor_research)} vendor stack rows, "
        f"{len(scraped_files)} scraped extracts."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
