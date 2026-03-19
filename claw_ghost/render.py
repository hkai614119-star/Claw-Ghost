from __future__ import annotations

from .models import TrustedExecutionReport


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def to_markdown(report: TrustedExecutionReport) -> str:
    ie = report.intent_extraction
    return f"""# Claw-Ghost Trusted Execution Report

## User Intent
{report.user_intent}

## 1. Intent Extraction
- Objective: {ie.objective}
- Trigger condition: {ie.trigger_condition}
- Risk boundary: {ie.risk_boundary}
- Allowed actions: {', '.join(ie.allowed_actions)}
- Stop conditions: {', '.join(ie.stop_conditions)}

## 2. Policy Tree Summary
{_bullets(report.policy_tree_summary)}

## 3. On-Chain Monitoring Plan
{_bullets(report.monitoring_plan)}

## 4. Trusted Execution Plan
{_bullets(report.trusted_execution_plan)}

## 5. Native Claw / Onchain OS Action Flow
{_bullets(report.native_action_flow)}

## 6. Privacy / Anti-MEV Considerations
{_bullets(report.privacy_considerations)}

## 7. Main Risks
{_bullets(report.main_risks)}

## 8. Invalidation / Abort Conditions
{_bullets(report.abort_conditions)}

## 9. User Feedback Loop
{_bullets(report.feedback_loop)}

## 10. Final Action Summary
{report.final_action_summary}

## 11. Confidence
{report.confidence}
"""


def to_execution_card(report: TrustedExecutionReport) -> str:
    ie = report.intent_extraction
    return f"""# Claw-Ghost Execution Card

- Intent: {ie.objective}
- Trigger: {ie.trigger_condition}
- Allowed action: {', '.join(ie.allowed_actions)}
- Abort condition: {report.abort_conditions[0]}
- Trusted execution note: signing and policy validation should occur in an isolated trusted environment
- User feedback: {report.feedback_loop[0]}
"""
