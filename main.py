"""
Main entry point for the Football Match Recommendation System.
Orchestrates the LangChain-style workflow.
"""

from prompt_optimization import generate_prompt
from llm_api import fetch_match_summary
from summary_analysis import analyze_summary
from judge import judge_match
from config import get_user_preferences

def main():
    print("=== Match Recommendation System ===")
    # Step 0: Get user ID
    user_id = input("Enter user ID (default: guest): ").strip()
    if not user_id:
        user_id = "guest"
    print(f"User ID: {user_id}")

    # Step 1: Get user preferences (team, criteria, etc.)
    user_prefs = get_user_preferences()
    default_sport = user_prefs.get("sport", "football")
    sport = input(f"Enter sport (default: {default_sport}): ").strip().lower()
    if not sport:
        sport = default_sport
    print(f"[1/7] Sport selected: {sport}")

    default_team = user_prefs.get("team_name", "Chelsea Football Club")
    team_name = input(f"Enter team name (default: {default_team}): ").strip()
    if not team_name:
        team_name = default_team
    print(f"[2/7] Team selected: {team_name}")

    # Step 1.5: Load and display recent user history
    try:
        from user_history import load_user_history, save_user_history
        history = load_user_history(user_id)
        if history:
            print(f"\nRecent history for {user_id}:")
            for entry in history[-3:]:
                print(f"- {entry['timestamp']}: {entry['team']} vs {entry.get('opponent', 'N/A')} on {entry.get('match_date', 'N/A')} | Recommendation: {entry['recommendation']}")
        else:
            print(f"No history found for {user_id}.")
    except ImportError:
        print("User history module not found. Skipping history display.")

    # Step 2: Generate prompt for LLM
    prompt = generate_prompt(team_name, user_prefs, sport)
    print("[3/7] Prompt generated.")

    # Step 3: Fetch match summary from LLM/API
    print("[4/7] Fetching match summary from LLM/API...")
    summary = fetch_match_summary(prompt)
    print("[5/7] Match summary fetched.")

    # Step 4: Analyze the summary
    print("[6/7] Analyzing match summary...")
    analysis = analyze_summary(summary, user_prefs, team_name, sport)
    print("[7/7] Analysis complete. Judging...")

    # Step 5: Judge/recommend
    recommendation, explanation = judge_match(analysis, user_prefs, sport)

    # Step 5.5: Save to user history
    try:
        save_user_history(user_id, team_name, analysis, recommendation, explanation)
        print("Session saved to user history.")
    except Exception as e:
        print(f"Could not save history: {e}")

    # Step 6: Output result
    print("\n=== Match Details ===")
    print(f"Match Date: {analysis.get('match_date', 'N/A')}")
    print(f"Opponent: {analysis.get('opponent', 'N/A')}")
    print(f"Venue: {analysis.get('venue', 'N/A')}")
    print(f"Recommendation: {'WATCH' if recommendation else 'SKIP'}")
    print(f"Reason: {explanation}")

if __name__ == "__main__":
    main()