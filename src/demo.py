from __future__ import annotations

import argparse
import json
from pathlib import Path

from claw_ghost import ClawGhostEngine
from claw_ghost.models import InputPayload
from claw_ghost.render import to_execution_card, to_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Claw-Ghost demo pipeline.")
    parser.add_argument("--input", required=True, help="Path to a JSON file with intent and on-chain snapshot.")
    parser.add_argument("--json-out", help="Optional path to write JSON report.")
    parser.add_argument("--md-out", help="Optional path to write markdown report.")
    parser.add_argument("--card-out", help="Optional path to write execution card.")
    args = parser.parse_args()

    payload_dict = json.loads(Path(args.input).read_text(encoding="utf-8"))
    payload = InputPayload.model_validate(payload_dict)

    engine = ClawGhostEngine()
    report = engine.analyze(payload)

    report_json = report.model_dump_json(indent=2)
    report_md = to_markdown(report)
    card_md = to_execution_card(report)

    print("=== JSON REPORT ===")
    print(report_json)
    print("\n=== MARKDOWN REPORT ===\n")
    print(report_md)
    print("\n=== EXECUTION CARD ===\n")
    print(card_md)

    if args.json_out:
        Path(args.json_out).write_text(report_json, encoding="utf-8")
    if args.md_out:
        Path(args.md_out).write_text(report_md, encoding="utf-8")
    if args.card_out:
        Path(args.card_out).write_text(card_md, encoding="utf-8")


if __name__ == "__main__":
    main()
