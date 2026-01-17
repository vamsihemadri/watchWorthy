"""
Judge Module

Decides whether to recommend watching the match, based on the structured analysis and user-configurable criteria.
Supports both rule-based and LLM-based judging.
"""

from typing import Tuple, Dict

def judge_match(analysis: Dict[str, any], user_prefs: dict) -> Tuple[bool, str]:
    """
    Make a recommendation based on the analysis and user preferences.

    Args:
        analysis (Dict[str, any]): Structured analysis of the match.
        user_prefs (dict): User-configurable criteria and thresholds.

    Returns:
        Tuple[bool, str]: (recommendation, explanation)
            recommendation: True if recommended to watch, False otherwise.
            explanation: Reasoning for the decision.
    """
    # Rule-based logic (default)
    excitement_threshold = user_prefs.get("excitement_threshold", 4)
    drama_threshold = user_prefs.get("drama_threshold", 3)
    notable_events_required = user_prefs.get("notable_events_required", ["red card", "late goal"])

    recommend = (
        analysis.get("excitement", 0) >= excitement_threshold or
        analysis.get("drama", 0) >= drama_threshold or
        any(event in analysis.get("notable_events", []) for event in notable_events_required)
    )

    explanation = (
        f"Excitement: {analysis.get('excitement')}, "
        f"Drama: {analysis.get('drama')}, "
        f"Notable Events: {', '.join(analysis.get('notable_events', []))}. "
    )
    if recommend:
        explanation += "Meets criteria for recommendation."
    else:
        explanation += "Does not meet criteria for recommendation."

    # LLM-based judging could be added here as an alternative

    return recommend, explanation