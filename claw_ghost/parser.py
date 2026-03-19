from __future__ import annotations

from .models import IntentExtraction


def parse_intent(text: str) -> IntentExtraction:
    lower = text.lower()

    objective = "Automate on-chain account protection"
    if "aave" in lower and "health factor" in lower:
        objective = "Monitor Aave account health factor and defend account safety"
    elif "liquidity pool" in lower or "tvl" in lower:
        objective = "Protect liquidity pool position under abnormal outflow"
    elif "leveraged" in lower:
        objective = "Defend leveraged on-chain position"

    trigger_condition = "Trigger when monitored risk metrics cross policy thresholds"
    if "below 1.5" in lower:
        trigger_condition = "Trigger when health factor drops below 1.5"
    elif "drains too fast" in lower:
        trigger_condition = "Trigger when TVL outflow and volatility shock exceed tolerance"

    risk_boundary = "Do not execute when slippage, congestion, or policy ambiguity exceed safe limits"

    allowed_actions = []
    if "add collateral" in lower:
        allowed_actions.append("Add collateral")
    if "reduce debt" in lower:
        allowed_actions.append("Reduce debt exposure")
    if "deleveraging" in lower or "reduce leverage" in lower:
        allowed_actions.append("Reduce leverage")
    if "exit the pool" in lower or "exit" in lower:
        allowed_actions.append("Exit position")
    if not allowed_actions:
        allowed_actions.append("Execute bounded protective action")

    stop_conditions = ["Policy conditions incomplete or conflicting", "Unsafe slippage or congestion"]
    if "pause execution" in lower:
        stop_conditions.append("User-defined slippage threshold breached")
    if "do not expose" in lower:
        stop_conditions.append("Execution visibility too high")

    return IntentExtraction(
        objective=objective,
        trigger_condition=trigger_condition,
        risk_boundary=risk_boundary,
        allowed_actions=allowed_actions,
        stop_conditions=stop_conditions,
    )


def extract_policy_tree(intent: IntentExtraction) -> list[str]:
    tree = [
        f"Observe monitored state until trigger condition is met: {intent.trigger_condition}",
        "Validate risk boundary before any action",
    ]
    for action in intent.allowed_actions:
        tree.append(f"If policy remains valid, allow action: {action}")
    tree.append("If stop condition is detected, pause or abort execution")
    return tree
