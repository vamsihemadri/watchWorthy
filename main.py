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
    # Step 1: Get user preferences (team, criteria, etc.)
    user_prefs = get_user_preferences()
    team_name = user_prefs.get("team_name", "Chelsea Football Club")

    # Step 2: Generate prompt for LLM
    prompt = generate_prompt(team_name, user_prefs)

    # Step 3: Fetch match summary from LLM/API
    summary = fetch_match_summary(prompt)

    # Step 4: Analyze the summary
    analysis = analyze_summary(summary, user_prefs)

    # Step 5: Judge/recommend
    recommendation, explanation = judge_match(analysis, user_prefs)

    # Step 6: Output result
    print(f"Recommendation: {'WATCH' if recommendation else 'SKIP'}")
    print(f"Reason: {explanation}")

if __name__ == "__main__":
    main()