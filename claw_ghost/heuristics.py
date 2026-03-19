from __future__ import annotations

from .models import InputPayload, IntentExtraction


def build_monitoring_plan(payload: InputPayload, intent: IntentExtraction) -> list[str]:
    snapshot = payload.onchain_snapshot
    plan = [
        f"Monitor protocol state: {snapshot.protocol_state}",
        f"Monitor account state: {snapshot.account_state}",
        f"Monitor liquidity state: {snapshot.liquidity_state}",
        f"Monitor slippage environment: {snapshot.slippage_state}",
        f"Monitor volatility state: {snapshot.volatility_state}",
    ]
    if "health factor" in payload.intent.lower():
        plan.append("Track Aave health factor and collateral availability in real time")
    if "liquidity pool" in payload.intent.lower() or "tvl" in payload.intent.lower():
        plan.append("Track pool TVL outflow, volatility shock, and residual exposure")
    return plan


def build_trusted_execution_plan(intent: IntentExtraction) -> list[str]:
    return [
        "Validate trigger condition and policy boundaries before any signing request",
        "Use isolated signing flow inside a TEE-like trusted execution environment",
        "Verify allowed actions against policy tree before producing authorization",
        "Only proceed if risk boundary remains satisfied at execution time",
    ]


def build_native_action_flow(payload: InputPayload, intent: IntentExtraction) -> list[str]:
    flow = [
        "Connector listens to raw protocol and account events",
        "Strategy Module evaluates policy tree against current on-chain state",
        "Wallet Manager prepares bounded signing request for the approved action",
    ]
    for action in intent.allowed_actions:
        flow.append(f"Execution Router carries out protective step: {action}")
    flow.append("Notification interface reports result and updated risk state to the user")
    return flow


def build_privacy_considerations(payload: InputPayload) -> list[str]:
    points = [
        "Isolate signing and policy evaluation from the normal host process",
        "Avoid exposing full strategy path before execution is necessary",
        "Reduce attack surface by preferring lower-visibility execution flow where possible",
    ]
    if "slippage" in payload.intent.lower() or "drains too fast" in payload.intent.lower():
        points.append("Delay or split execution when market conditions increase visibility and impact")
    return points


def build_main_risks(payload: InputPayload) -> list[str]:
    risks = [
        "Protocol risk or incomplete on-chain visibility",
        "Slippage deterioration at execution time",
        "Chain congestion delaying protective actions",
        "Collateral shortfall or account stress worsening faster than expected",
        "Policy misfire if user intent is ambiguous",
    ]
    if "liquidity pool" in payload.intent.lower() or "tvl" in payload.intent.lower():
        risks.append("Residual exposure after partial pool exit")
    return risks


def build_abort_conditions(intent: IntentExtraction) -> list[str]:
    return intent.stop_conditions + [
        "Trusted validation fails",
        "Observed state no longer matches policy assumptions",
    ]


def build_feedback_loop(intent: IntentExtraction) -> list[str]:
    return [
        "Report whether trigger condition was met",
        "Report whether execution was completed, delayed, or aborted",
        "Return updated account and risk state after each major decision point",
        "Notify user if additional manual intervention is required",
    ]


def build_summary(intent: IntentExtraction) -> str:
    actions = ", ".join(intent.allowed_actions)
    return (
        f"Claw-Ghost would monitor the defined on-chain risk signals, validate the policy tree in a trusted "
        f"execution environment, and only perform bounded protective actions such as {actions} when the trigger "
        f"condition is met and execution remains within safe risk boundaries."
    )
