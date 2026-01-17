"""
Summary Analysis Module

Analyzes the match summary to extract and score key aspects (excitement, drama, notable events, player performance, etc.).
"""

from typing import Dict

def analyze_summary(
    summary: str,
    user_prefs: dict,
    team_name: str = "Chelsea Football Club",
    sport: str = "football"
) -> Dict[str, any]:
    """
    Analyze the match summary and extract scores/tags for each configured criterion.

    Args:
        summary (str): The match summary text.
        user_prefs (dict): User preferences and selected criteria.
        team_name (str): The team name provided by the user.
        sport (str): The sport (e.g., football, cricket).

    Returns:
        Dict[str, any]: Structured analysis object with scores/tags for each criterion.
    """
    # Try to extract opponent, match date, and venue from the first three lines of the summary
    lines = summary.strip().splitlines()
    opponent = lines[0].replace("Opponent:", "").strip() if len(lines) > 0 and "opponent" in lines[0].lower() else "Unknown"
    match_date = lines[1].replace("Match Date:", "").strip() if len(lines) > 1 and "date" in lines[1].lower() else "Unknown"
    venue = lines[2].replace("Venue:", "").strip() if len(lines) > 2 and "venue" in lines[2].lower() else "Unknown"

    # The rest of the analysis is still placeholder/dummy
    if sport == "cricket":
        analysis = {
            "team": team_name,
            "match_date": match_date,
            "opponent": opponent,
            "venue": venue,
            "excitement": 5,
            "drama": 4,
            "notable_events": ["hat-trick", "super over"],
            "player_performance": {"MVP": "Player Z", "underperformer": "Player Y"},
            "tactics": "Aggressive batting in powerplay",
            "crowd": "Packed stadium, loud cheers",
            "rivalry": f"{team_name} vs {opponent}",
            "stats": {"runs": 320, "wickets": 8},
            "emotional_impact": "Very High",
            "post_match_reactions": ["Captain praised bowlers", "Fans thrilled"]
        }
    else:
        analysis = {
            "team": team_name,
            "match_date": match_date,
            "opponent": opponent,
            "venue": venue,
            "excitement": 4,
            "drama": 3,
            "notable_events": ["red card", "late goal"],
            "player_performance": {"MVP": "Player X", "underperformer": "Player Y"},
            "tactics": "Switched to 3-5-2 in second half",
            "crowd": "Lively, sold-out stadium",
            "rivalry": f"{team_name} vs {opponent}",
            "stats": {"possession": "55%", "shots": 15},
            "emotional_impact": "High",
            "post_match_reactions": ["Coach praised defense", "Fans ecstatic"]
        }
    return analysis