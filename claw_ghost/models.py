from __future__ import annotations

from typing import List
from pydantic import BaseModel, Field


class OnChainSnapshot(BaseModel):
    protocol_state: str = "unknown"
    account_state: str = "unknown"
    liquidity_state: str = "unknown"
    slippage_state: str = "unknown"
    volatility_state: str = "unknown"


class InputPayload(BaseModel):
    intent: str
    onchain_snapshot: OnChainSnapshot = Field(default_factory=OnChainSnapshot)


class IntentExtraction(BaseModel):
    objective: str
    trigger_condition: str
    risk_boundary: str
    allowed_actions: List[str]
    stop_conditions: List[str]


class TrustedExecutionReport(BaseModel):
    user_intent: str
    intent_extraction: IntentExtraction
    policy_tree_summary: List[str]
    monitoring_plan: List[str]
    trusted_execution_plan: List[str]
    native_action_flow: List[str]
    privacy_considerations: List[str]
    main_risks: List[str]
    abort_conditions: List[str]
    feedback_loop: List[str]
    final_action_summary: str
    confidence: str
