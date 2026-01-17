"""
Prompt Optimization Module

Generates the most effective prompt for the LLM to retrieve a high-quality, relevant match summary for the specified football team.
"""

def generate_prompt(team_name: str, user_prefs: dict) -> str:
    """
    Generate an optimized prompt for the LLM/API fetch stage.

    Args:
        team_name (str): The football team to query.
        user_prefs (dict): User preferences and criteria.

    Returns:
        str: The optimized prompt string.
    """
    # Basic template; can be extended for more advanced prompt engineering
    focus_areas = user_prefs.get("focus_areas", "excitement, drama, and notable events")
    summary_length = user_prefs.get("summary_length", 1000)
    prompt = (
        f"Can you tell me what the latest match of {team_name} was and give its match summary "
        f"in {summary_length} words? Focus on {focus_areas}."
    )
    return prompt