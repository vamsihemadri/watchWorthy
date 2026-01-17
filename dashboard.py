"""
Dashboard CLI for Match Recommendation System

Displays the history of all users, with options to filter by user ID or sport.
"""

import json
import os

HISTORY_FILE = "user_history.json"

def load_all_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def filter_history(history, user_id=None, sport=None):
    filtered = history
    if user_id:
        filtered = [h for h in filtered if h.get("user_id", "").lower() == user_id.lower()]
    if sport:
        filtered = [h for h in filtered if h.get("sport", "football").lower() == sport.lower()]
    return filtered

def print_table(history):
    if not history:
        print("No history found for the given filter.")
        return
    # Print header
    print(f"{'User':<10} {'Sport':<10} {'Team':<15} {'Opponent':<15} {'Date':<12} {'Venue':<15} {'Rec':<6} {'Exc':<3} {'Drama':<3}")
    print("-" * 90)
    for h in history:
        print(f"{h.get('user_id','')[:10]:<10} {h.get('sport','football')[:10]:<10} {h.get('team','')[:15]:<15} {h.get('opponent','')[:15]:<15} {h.get('match_date','')[:12]:<12} {h.get('venue','')[:15]:<15} {h.get('recommendation','')[:6]:<6} {str(h.get('excitement',''))[:3]:<3} {str(h.get('drama',''))[:3]:<3}")

def main():
    print("=== Match Recommendation Dashboard ===")
    user_id = input("Filter by user ID (leave blank for all): ").strip()
    sport = input("Filter by sport (leave blank for all): ").strip().lower()
    history = load_all_history()
    filtered = filter_history(history, user_id if user_id else None, sport if sport else None)
    print_table(filtered)

if __name__ == "__main__":
    main()