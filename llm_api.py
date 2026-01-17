"""
LLM/API Fetch Module

Handles communication with the fastrouter.ai API to retrieve the latest match summary for the specified team.
"""

import os
import requests

FASTR_OUTER_API_URL = "https://api.fastrouter.ai/api/v1/chat/completions"
FASTR_OUTER_API_KEY = os.environ.get("FASTR_OUTER_API_KEY", "sk-REPLACE_ME")

def fetch_match_summary(prompt: str) -> str:
    """
    Fetch the latest match summary for the given prompt using the fastrouter.ai API.

    Args:
        prompt (str): The prompt to send to the LLM.

    Returns:
        str: The match summary as returned by the LLM/API.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {FASTR_OUTER_API_KEY}"
    }
    data = {
        "model": "perplexity/sonar-pro",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }
    try:
        response = requests.post(FASTR_OUTER_API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        # Extract the summary from the response structure
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error fetching match summary: {e}")
        return "Error: Could not fetch match summary."