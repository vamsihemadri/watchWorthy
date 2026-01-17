# Football Match Recommendation System

A modular, LangChain-style Python system that uses an online LLM to fetch the latest match summary for a football team, analyzes the summary, and recommends whether you should watch the match.

## Features

- User-configurable team and analysis criteria
- Prompt optimization for LLM queries
- Integration with fastrouter.ai API (Perplexity Sonar Pro model)
- Modular summary analysis (excitement, drama, notable events, player performance, tactics, crowd, rivalry, stats, emotional impact, post-match reactions)
- Rule-based (and extensible to LLM-based) recommendation logic

## Architecture

```mermaid
flowchart TD
    A[User Input: Team Name & Preferences] --> B[Prompt Optimization Module]
    B --> C[LLM/API Fetch Module (fastrouter.ai)]
    C --> D[Summary Analysis Module]
    D --> E[Judge Module (Rule-based or LLM-based)]
    E --> F[Recommendation Output Module]
    subgraph Analysis Criteria
        D1[Excitement Level]
        D2[Drama/Turning Points]
        D3[Notable Events]
        D4[Player Performance]
        D5[Tactical Analysis]
        D6[Crowd Atmosphere]
        D7[Rivalry/Context]
        D8[Statistical Highlights]
        D9[Emotional Impact]
        D10[Post-match Reactions]
    end
    D --> D1
    D --> D2
    D --> D3
    D --> D4
    D --> D5
    D --> D6
    D --> D7
    D --> D8
    D --> D9
    D --> D10
```

## Usage

1. Install dependencies:
    ```bash
    pip install requests
    ```
2. Set your fastrouter.ai API key as an environment variable:
    ```bash
    export FASTR_OUTER_API_KEY=sk-REPLACE_ME
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

## File Structure

- `main.py` - Orchestrates the workflow
- `prompt_optimization.py` - Generates the LLM prompt
- `llm_api.py` - Handles API calls to fastrouter.ai
- `summary_analysis.py` - Analyzes the match summary
- `judge.py` - Makes the recommendation
- `config.py` - User preferences and criteria
- `README.md` - Project documentation

## Extending

- Add new analysis criteria in `summary_analysis.py`
- Adjust or add new recommendation logic in `judge.py`
- Support more user input methods in `config.py`
- Swap out the LLM/API in `llm_api.py`

---

© 2026 Football Match Recommendation System