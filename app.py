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

# --- OFFICIAL 48-TEAM COMPREHENSIVE WORLD CUP DATABASE ---
group_stage_database = {
    # Group A
    "Mexico": {"points": 9, "gd": 6}, "South Africa": {"points": 4, "gd": -1},
    "South Korea": {"points": 3, "gd": -1}, "Czechia": {"points": 1, "gd": -4},
    # Group B
    "Switzerland": {"points": 7, "gd": 4}, "Canada": {"points": 4, "gd": 5},
    "Bosnia and Herzegovina": {"points": 4, "gd": -1}, "Qatar": {"points": 1, "gd": -8},
    # Group C
    "Brazil": {"points": 7, "gd": 6}, "Morocco": {"points": 7, "gd": 3},
    "Scotland": {"points": 3, "gd": -3}, "Haiti": {"points": 0, "gd": -6},
    # Group D
    "United States": {"points": 6, "gd": 4}, "Australia": {"points": 4, "gd": 0},
    "Paraguay": {"points": 4, "gd": -2}, "Turkey": {"points": 3, "gd": -2},
    # Group E
    "Germany": {"points": 6, "gd": 6}, "Ivory Coast": {"points": 6, "gd": 2},
    "Ecuador": {"points": 4, "gd": 0}, "Curaçao": {"points": 1, "gd": -8},
    # Group F
    "Netherlands": {"points": 7, "gd": 6}, "Japan": {"points": 5, "gd": 4},
    "Sweden": {"points": 4, "gd": 0}, "Tunisia": {"points": 0, "gd": -10},
    # Group G
    "Belgium": {"points": 5, "gd": 4}, "Egypt": {"points": 5, "gd": 2},
    "Iran": {"points": 3, "gd": 0}, "New Zealand": {"points": 1, "gd": -6},
    # Group H
    "Spain": {"points": 7, "gd": 5}, "Cape Verde": {"points": 3, "gd": 0},
    "Uruguay": {"points": 2, "gd": -1}, "Saudi Arabia": {"points": 2, "gd": -4},
    # Group I
    "France": {"points": 9, "gd": 8}, "Norway": {"points": 6, "gd": 1},
    "Senegal": {"points": 3, "gd": 2}, "Iraq": {"points": 0, "gd": -11},
    # Group J (Live Matches In-Progress)
    "Argentina": {"points": 6, "gd": 5}, "Austria": {"points": 3, "gd": 0},
    "Algeria": {"points": 3, "gd": -2}, "Jordan": {"points": 0, "gd": -3},
    # Group K (Live Matches In-Progress)
    "Colombia": {"points": 6, "gd": 3}, "Portugal": {"points": 4, "gd": 5},
    "DR Congo": {"points": 1, "gd": -1}, "Uzbekistan": {"points": 0, "gd": -7},
    # Group L (Live Matches In-Progress)
    "England": {"points": 4, "gd": 2}, "Ghana": {"points": 4, "gd": 1},
    "Croatia": {"points": 3, "gd": -1}, "Panama": {"points": 0, "gd": -2}
}

# Alphabetically sorted list of all teams for clean UI selection
all_teams_list = sorted(list(group_stage_database.keys()))

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

# Interactive Form Selectors populated with the complete 48 teams
col1, col2 = st.columns(2)
with col1:
    # Defaults to Croatia
    team_a = st.selectbox("Select Home Team", options=all_teams_list, index=12)
with col2:
    # Defaults to Ghana
    team_b = st.selectbox("Select Away Team", options=all_teams_list, index=19)

# Bookmaker Variable Injector
odds_favorite = st.radio(
    "Who do the bookies have put as favourites to win?",
    options=[team_a, team_b, "Even / No Favorite"],
    index=2
)

if team_a == team_b:
    st.error("Error: Please select two different competing teams.")
else:
    # Trigger calculation dynamically on selection change
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
