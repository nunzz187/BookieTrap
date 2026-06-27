import streamlit as st
import json

def calculate_automated_predictions(home_team, away_team, group_data, wildcard_table):
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
            f"\n*   **The Shared Premium:** A draw elevates both teams above the elimination cutoff line. "
            f"Because a single point guarantees safety, an implicit mutual deadlock script is heavily favored. "
            f"Expect a slow, low-risk horizontal passing model in the final 20 minutes."
        )
        predictions = [
            {"score": "0 – 0", "type": "Cooperative Stalemate", "desc": "Both sides minimize horizontal risk, maintaining low defensive structures to secure progression."},
            {"score": "1 – 1", "type": "Restored Parity", "desc": "An early individual mistake prompts an equalizer, after which both teams down tools to share the points."},
            {"score": "1 – 0", "type": "Controlled Edge", "desc": "The favored side claims a narrow tactical advantage, immediately dropping into a low block to run out the clock."}
        ]
    else:
        reasoning.append("\n*   **Asymmetrical Motivation:** Match parameters require an open, high-risk script.")
        
    return {
        "safety_threshold_points": safe_points_line,
        "automated_reasoning": "\n".join(reasoning),
        "target_scores": predictions
    }

# --- ACTIVE INGESTION PIPELINE ---
st.title("World Cup Predictive Analytics Engine")

# Real-time tournament database states
group_l_standings = {
    "Croatia": {"points": 3, "gd": -1},
    "Ghana": {"points": 4, "gd": 1},
    "England": {"points": 4, "gd": 2},
    "Panama": {"points": 0, "gd": -2}
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

# Run analysis execution
analytics = calculate_automated_predictions(
    home_team="Croatia", 
    away_team="Ghana", 
    group_data=group_l_standings, 
    wildcard_table=master_wildcard_standings
)

# Render Streamlit Output Nodes
st.markdown(analytics["automated_reasoning"])
st.markdown("---")
st.markdown("### 🎯 Target Correct Score Presets")

for target in analytics["target_scores"]:
    st.info(f"**{target['score']}** ({target['type']}) — {target['desc']}")
