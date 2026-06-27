import streamlit as st
import json

def calculate_automated_predictions(home_team, away_team, favorite_team, group_data, wildcard_table):
    """
    Automated Analysis Engine for World Cup Group Stage Finales.
    Evaluates mutual safety thresholds based on the 3rd-place master tracker.
    """
    home_pts = group_data[home_team]["points"]
    away_pts = group_data[away_team]["points"]
    
    # Identify cutoff baseline from the 9th position (Index 8)
    elimination_baseline_pts = wildcard_table[8]["points"] 
    safe_points_line = elimination_baseline_pts + 1
    
    # Calculate conditional outcomes for a draw scenario
    home_safe_with_draw = (home_pts + 1) >= safe_points_line
    away_safe_with_draw = (away_pts + 1) >= safe_points_line
    
    reasoning = []
    reasoning.append("### 🛡️ Automated Safety Line Analysis")
    reasoning.append(f"The live cross-group third-place table dictates that reaching **{safe_points_line} points** guarantees absolute qualification immunity into the Round of 32.")
    
    predictions = []
    if home_safe_with_draw and away_safe_with_draw:
        reasoning.append(
            f"\n* **The Shared Premium:** A draw elevates both teams above the elimination cutoff line. "
            f"Because a single point guarantees safety, an implicit mutual deadlock script is heavily favored. "
            f"Neither manager will take heavy risks past the 75th minute."
        )
        
        # Factor in who the bookies favored to adjust the targeted variations
        if favorite_team == home_team:
            controlled_score = "1 – 0"
            favored_desc = f"The odds favor **{home_team}** to dictate the game. They claim a narrow tactical advantage, immediately dropping into a low block to run out the clock."
        elif favorite_team == away_team:
            controlled_score = "0 – 1"
            favored_desc = f"The odds favor **{away_team}** to punish on transition. They secure a thin lead and shut down the match cleanly."
        else:
            controlled_score = "1 – 0"
            favored_desc = "With no clear bookie edge, a tight, defensive breakthrough manages the qualification."

        predictions = [
            {"score": "0 – 0", "type": "Cooperative Stalemate", "desc": "Both sides minimize horizontal risk, maintaining low defensive structures to secure progression."},
            {"score": "1 – 1", "type": "Restored Parity", "desc": "An early individual mistake prompts an equalizer, after which both teams down tools to share the points."},
            {"score": controlled_score, "type": "Controlled Edge", "desc": favored_desc}
        ]
    else:
        reasoning.append("\n* **Asymmetrical Motivation:** Match parameters require an open, high-risk script because a draw fails to protect both teams simultaneously.")
        
    return {
        "safety_threshold_points": safe_points_line,
        "automated_reasoning": "\n".join(reasoning),
        "target_scores": predictions
    }

# --- STREAMLIT UI INTERFACE ---
st.title("⚽ BookieTrap: Grand Finale Matrix")
st.markdown("Select your matching pair to calculate tactical script vulnerabilities based on the tournament wildcard thresholds.")

# Real-time data storage arrays
tournament_teams = ["Croatia", "Ghana", "England", "Panama", "Sweden", "Ecuador", "Senegal"]

group_stage_database = {
    "Croatia": {"points": 3, "gd": -1},
    "Ghana": {"points": 4, "gd": 1},
    "England": {"points": 4, "gd": 2},
    "Panama": {"points": 0, "gd": -2},
    "Sweden": {"points": 4, "gd": 0},
    "Ecuador": {"points": 4, "gd": 0},
    "Senegal": {"points": 3, "gd": 2}
}

master_wildcard_standings = [
    {"rank": 1, "team": "Sweden", "points": 4, "gd": 0},
    {"rank": 2, "team": "Ecuador", "points": 4, "gd": 0},
    {"rank": 3, "team": "Bosnia", "points": 4, "gd": -1},
    {"rank": 4, "team": "Paraguay", "points": 4, "gd": -2},
    {"rank": 5, "team": "Senegal", "points": 3, "gd": 2},
    {"rank": 6, "team": "South Korea", "points": 3, "gd": -1},
    {"rank": 7, "team": "Iran", "points": 3, "gd": 0},
    {"rank": 8, "team": "Scotland", "points": 3, "gd": -3},
    {"rank": 9, "team": "Uruguay", "points": 2, "gd": -1}
]

# Interactive Form Selectors
col1, col2 = st.columns(2)
with col1:
    team_a = st.selectbox("Select Home Team", options=tournament_teams, index=0)
with col2:
    team_b = st.selectbox("Select Away Team", options=tournament_teams, index=1)

# Bookmaker Variable Injector
odds_favorite = st.radio(
    "Who do the bookies have put as favourites to win?",
    options=[team_a, team_b, "Even / No Favorite"],
    index=2
)

if team_a == team_b:
    st.error("Error: Please select two different competing teams.")
else:
    # Trigger calculation dynamically on state change
    analytics = calculate_automated_predictions(
        home_team=team_a, 
        away_team=team_b, 
        favorite_team=odds_favorite,
        group_data=group_stage_database, 
        wildcard_table=master_wildcard_standings
    )

    # Render Output Nodes
    st.markdown("---")
    st.markdown(analytics["automated_reasoning"])
    
    if analytics["target_scores"]:
        st.markdown("### 🎯 Target Correct Score Presets")
        for target in analytics["target_scores"]:
            st.info(f"**{target['score']}** ({target['type']}) — {target['desc']}")
