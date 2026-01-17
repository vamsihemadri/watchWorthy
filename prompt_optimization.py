"""
Prompt Optimization Module

Generates the most effective prompt for the LLM to retrieve a high-quality, relevant match summary for the specified football team.
"""

def generate_prompt(team_name: str, user_prefs: dict, sport: str = "football") -> str:
    """
    Generate an optimized prompt for the LLM/API fetch stage.

    Args:
        team_name (str): The team to query.
        user_prefs (dict): User preferences and criteria.
        sport (str): The sport (e.g., football, cricket).

    Returns:
        str: The optimized prompt string.
    """
    focus_areas = user_prefs.get("focus_areas", "excitement, drama, and notable events")
    summary_length = user_prefs.get("summary_length", 1000)
    if sport == "cricket":
        prompt = (
            f"Can you tell me what the latest {sport} match of {team_name} was and give its match summary "
            f"in {summary_length} words? Focus on {focus_areas}, key moments, and player performances. "
            f"Also, explicitly state the opponent, match date, and venue in the first three lines of your response."
        )
    else:
        prompt = (
            f"Can you tell me what the latest {sport} match of {team_name} was and give its match summary "
            f"in {summary_length} words? Focus on {focus_areas}. "
            f"Also, explicitly state the opponent, match date, and venue in the first three lines of your response."
        )
    return prompt