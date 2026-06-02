#!/usr/bin/env python3
"""
Attempt to extract APZI member candidates from the public members page.

The APZI page is partly rendered as a directory/search UI, so this script is
deliberately conservative: it records visible candidate lines and categories
instead of pretending to have a complete member export.
"""

from __future__ import annotations

import csv
import html.parser
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "data" / "apzi_member_candidates.csv"
URLS = [
    "https://www.apzi.be/leden",
    "https://www.apzi.be/en/leden",
]

CATEGORY_TERMS = {
    "customs",
    "douane",
    "expeditie",
    "freight",
    "forwarding",
    "goederenbehandeling",
    "it",
    "logistiek",
    "logistics",
    "magazijnopslag",
    "rederijen",
    "shipping",
    "terminal",
    "transport",
    "warehousing",
}
NOISE_TEXT = {
    "all activities",
    "home",
    "news",
    "events",
    "leden",
    "members",
    "quicklinks",
    "we use cookies to provide you a better user experience on this website.",
}


class TextExtractor(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip = False

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self.parts.append(text)


def fetch(url: str, *, verify_tls: bool = True) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "zeebrugge-logistics-intel/0.2 (+research script)"},
    )
    context = ssl.create_default_context() if verify_tls else ssl._create_unverified_context()
    with urllib.request.urlopen(request, timeout=20, context=context) as response:
        return response.read().decode("utf-8", errors="replace")


def classify(text: str) -> str:
    lowered = text.lower()
    hits = sorted(term for term in CATEGORY_TERMS if re.search(rf"\b{re.escape(term)}\b", lowered))
    return ";".join(hits)


def looks_like_candidate(text: str) -> bool:
    if len(text) < 3 or len(text) > 120:
        return False
    if text.lower() in NOISE_TEXT:
        return False
    if text.startswith("→"):
        return False
    if re.fullmatch(r"[0-9]+", text):
        return False
    return bool(classify(text) or re.search(r"\b(nv|bv|sa|ltd|logistics|terminal|ports?)\b", text, re.I))


def main() -> int:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for url in URLS:
        try:
            html = fetch(url)
        except urllib.error.URLError as exc:
            if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
                raise
            html = fetch(url, verify_tls=False)
        parser = TextExtractor()
        parser.feed(html)
        for text in parser.parts:
            if not looks_like_candidate(text):
                continue
            key = (url, text.lower())
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "source_url": url,
                    "candidate_text": text,
                    "matched_terms": classify(text),
                    "status": "candidate_visible_text",
                }
            )

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    with TARGET.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["source_url", "candidate_text", "matched_terms", "status"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} APZI visible-text candidates to {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
