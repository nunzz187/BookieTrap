import json

def generate_match_analytics(home_team, away_team, group_data, wildcard_table):
    """
    Automated Analysis Engine for World Cup Group Stage Finales.
    Evaluates mutual safety thresholds based on the 3rd-place master tracker.
    """
    # 1. Automate Standings Context Extraction
    home_pts = group_data[home_team]["points"]
    away_pts = group_data[away_team]["points"]
    home_gd = group_data[home_team]["gd"]
    away_gd = group_data[away_team]["gd"]
    
    # 2. Compute Wildcard Safety Line from Completed Groups
    # Find the point tally of the current 9th place team (first team eliminated)
    elimination_threshold_pts = wildcard_table[8]["points"] 
    safe_points_line = elimination_threshold_pts + 1
    
    # Calculate scenarios
    pts_if_draw_home = home_pts + 1
    pts_if_draw_away = away_pts + 1
    
    # Check if a draw secures absolute qualification immunity for both
    home_safe_with_draw = pts_if_draw_home >= safe_points_line
    away_safe_with_draw = pts_if_draw_away >= safe_points_line
    
    # 3. Automated Tactical Reasoning Generator
    reasoning = []
    reasoning.append(f"### 🛡️ Automated Safety Line Analysis")
    reasoning.append(f"The live cross-group third-place table dictates that reaching **{safe_points_line} points** guarantees absolute qualification immunity into the Round of 32.")
    
    if home_safe_with_draw and away_safe_with_draw:
        reasoning.append(
            f"\n*   **The Shared Premium:** A draw pushes {home_team} to {pts_if_draw_home} points and {away_team} to {pts_if_draw_away} points. "
            f"Because both teams completely clear the {elimination_threshold_pts}-point cutoff, an implicit late-game deadlock logic is highly active. "
            f"Neither manager will green-light high-risk offensive phases past the 75th minute."
        )
    else:
        reasoning.append(f"\n*   **Asymmetrical Motivation:** One or both teams require a maximum victory to guarantee progression, forcing an open match script.")

    # 4. Correct Score Prediction Matrix Generator
    predictions = []
    if home_safe_with_draw and away_safe_with_draw:
        predictions = [
            {"score": "0 – 0", "type": "Cooperative Stalemate", "desc": "Both sides minimize horizontal risk, maintaining low defensive structures to secure progression."},
            {"score": "1 – 1", "type": "Restored Parity", "desc": "An early individual mistake prompts an equalizer, after which both teams down tools to share the points."},
            {"score": "1 – 0", "type": "Controlled Edge", "desc": "The favored side claims a narrow tactical advantage, immediately dropping into a low block to run out the clock."}
        ]
        
    return {
        "summary": f"{home_team} vs {away_team} Analytics Pipeline",
        "safety_threshold_points": safe_points_line,
        "automated_reasoning": "\n".join(reasoning),
        "target_scores": predictions
    }

# --- EXAMPLE LIVE APPLICATION LIVE DEPLOYMENT ---
if __name__ == "__main__":
    # Live Live-Group L Standings Data Before Kickoff
    group_l_data = {
        "Croatia": {"points": 3, "gd": -1},
        "Ghana": {"points": 4, "gd": 1},
        "England": {"points": 4, "gd": 2},
        "Panama": {"points": 0, "gd": -2}
    }

    # Live Scraped Master Third-Place Leaderboard Tracker
    scraped_wildcard_table = [
        {"rank": 1, "team": "Sweden", "points": 4, "gd": 0},
        {"rank": 2, "team": "Ecuador", "points": 4, "gd": 0},
        {"rank": 3, "team": "Bosnia", "points": 4, "gd": -1},
        {"rank": 4, "team": "Paraguay", "points": 4, "gd": -2},
        {"rank": 5, "team": "Senegal", "points": 3, "gd": 2},
        {"rank": 6, "team": "South Korea", "points": 3, "gd": -1},
        {"rank": 7, "team": "Iran", "points": 3, "gd": 0},
        {"rank": 8, "team": "Scotland", "points": 3, "gd": -3},
        {"rank": 9, "team": "Uruguay", "points": 2, "gd": -1} # Rank 9 is the cutoff line (Eliminated)
    ]

    # Run Analysis Pipeline for the User's Target Teams
    output = generate_match_analytics(
        home_team="Croatia", 
        away_team="Ghana", 
        group_data=group_l_data, 
        wildcard_table=scraped_wildcard_table
    )

    # Print the structured output to be pushed to your app's frontend component layout
    print(output["automated_reasoning"])
    print("\n### 🎯 Target Correct Score Presets:")
    for pred in output["target_scores"]:
        print(f"*   **{pred['score']}** ({pred['type']}): {pred['desc']}")

