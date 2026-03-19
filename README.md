# Claw-Ghost
Trusted Private Execution Agent

Claw-Ghost is a lightweight open-source demo kit that showcases how a trusted private execution agent for Claw / Onchain OS can translate natural language intent into policy trees, monitor raw on-chain state, and generate bounded self-custodied execution plans with privacy and risk-awareness in mind.

## Why this project
Most on-chain AI agents focus on analysis. Real users worry about execution:
- private key exposure
- strategy leakage
- MEV visibility
- liquidation / health factor protection
- slippage and congestion during stressful conditions

Claw-Ghost is designed as a **trusted intent execution workflow demo** rather than a prediction bot. It accepts natural language goals, extracts policy boundaries, proposes a native action flow, and generates an explainable execution report.

## Core modules
- **Intent Parser** — turns natural language into structured policy logic
- **On-Chain Monitor** — defines which protocol and account signals matter
- **Trusted Signer** — explains how execution should be validated in an isolated environment
- **Anti-MEV Router** — reduces strategy exposure and attack surface where possible
- **Risk Guardian** — adds abort, delay, and feedback logic around execution

## Example workflow
1. Parse natural language intent
2. Build a policy tree and allowed action set
3. Define on-chain monitoring requirements
4. Generate trusted execution flow using native Claw / Onchain OS style modules
5. Produce risk, abort, and feedback logic

## Quick start
```bash
pip install -r requirements.txt
python -m src.demo --input examples/intent_snapshot_1.json
```

## Demo scenarios
- Aave health factor monitoring and auto-collateral protection
- Liquidity pool TVL outflow and defensive exit logic
- Leveraged position deleveraging under volatility stress

## Sample output sections
- Intent Extraction
- Policy Tree Summary
- On-Chain Monitoring Plan
- Trusted Execution Plan
- Native Claw / Onchain OS Action Flow
- Privacy / Anti-MEV Considerations
- Abort Conditions
- User Feedback Loop

## Repository structure
```text
Claw-Ghost/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ .gitignore
├─ prompts/
├─ examples/
├─ assets/
├─ src/
└─ claw_ghost/
```

## Scope
This repository is a workflow demo kit, **not production trading infrastructure** and not a live trading deployment.
