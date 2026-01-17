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
    # Step 1: Get user preferences (team, criteria, etc.)
    user_prefs = get_user_preferences()
    default_team = user_prefs.get("team_name", "Chelsea Football Club")
    team_name = input(f"Enter team name (default: {default_team}): ").strip()
    if not team_name:
        team_name = default_team
    print(f"[1/6] Team selected: {team_name}")

    # Step 2: Generate prompt for LLM
    prompt = generate_prompt(team_name, user_prefs)
    print("[2/6] Prompt generated.")

    # Step 3: Fetch match summary from LLM/API
    print("[3/6] Fetching match summary from LLM/API...")
    summary = fetch_match_summary(prompt)
    print("[4/6] Match summary fetched.")

    # Step 4: Analyze the summary
    print("[5/6] Analyzing match summary...")
    analysis = analyze_summary(summary, user_prefs)
    print("[6/6] Analysis complete. Judging...")

    # Step 5: Judge/recommend
    recommendation, explanation = judge_match(analysis, user_prefs)

    # Step 6: Output result
    print("\n=== Match Details ===")
    print(f"Match Date: {analysis.get('match_date', 'N/A')}")
    print(f"Opponent: {analysis.get('opponent', 'N/A')}")
    print(f"Venue: {analysis.get('venue', 'N/A')}")
    print(f"Recommendation: {'WATCH' if recommendation else 'SKIP'}")
    print(f"Reason: {explanation}")

if __name__ == "__main__":
    main()