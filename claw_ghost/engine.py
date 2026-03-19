from __future__ import annotations

from .models import InputPayload, TrustedExecutionReport
from .parser import parse_intent, extract_policy_tree
from .heuristics import (
    build_abort_conditions,
    build_feedback_loop,
    build_main_risks,
    build_monitoring_plan,
    build_native_action_flow,
    build_privacy_considerations,
    build_summary,
    build_trusted_execution_plan,
)


class ClawGhostEngine:
    def analyze(self, payload: InputPayload) -> TrustedExecutionReport:
        intent = parse_intent(payload.intent)
        report = TrustedExecutionReport(
            user_intent=payload.intent,
            intent_extraction=intent,
            policy_tree_summary=extract_policy_tree(intent),
            monitoring_plan=build_monitoring_plan(payload, intent),
            trusted_execution_plan=build_trusted_execution_plan(intent),
            native_action_flow=build_native_action_flow(payload, intent),
            privacy_considerations=build_privacy_considerations(payload),
            main_risks=build_main_risks(payload),
            abort_conditions=build_abort_conditions(intent),
            feedback_loop=build_feedback_loop(intent),
            final_action_summary=build_summary(intent),
            confidence="Medium",
        )
        return report
