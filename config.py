"""
Config Module

Handles user preferences and criteria configuration for the recommendation system.
"""

def get_user_preferences() -> dict:
    """
    Get user preferences for the system.
    In a real implementation, this could prompt the user, read from a config file, or accept CLI args.

    Returns:
        dict: User preferences and criteria.
    """
    return {
        "team_name": "Chelsea Football Club",
        "focus_areas": "excitement, drama, and notable events",
        "summary_length": 1000,
        "excitement_threshold": 4,
        "drama_threshold": 3,
        "notable_events_required": ["red card", "late goal"],
        # Add more preferences as needed
    }