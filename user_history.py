"""
User History Module

Handles saving and loading user history to/from a local JSON file.
"""

import json
import os
from datetime import datetime

HISTORY_FILE = "user_history.json"

def load_user_history(user_id: str):
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        all_history = json.load(f)
    return [entry for entry in all_history if entry.get("user_id") == user_id]

def save_user_history(user_id: str, team_name: str, analysis: dict, recommendation: bool, explanation: str):
    entry = {
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat(),
        "team": team_name,
        "match_date": analysis.get("match_date"),
        "opponent": analysis.get("opponent"),
        "venue": analysis.get("venue"),
        "excitement": analysis.get("excitement"),
        "drama": analysis.get("drama"),
        "notable_events": analysis.get("notable_events"),
        "recommendation": "WATCH" if recommendation else "SKIP",
        "explanation": explanation
    }
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            all_history = json.load(f)
    else:
        all_history = []
    all_history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(all_history, f, indent=2)