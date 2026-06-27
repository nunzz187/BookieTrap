import streamlit as st

def calculate_automated_predictions(home_team, away_team, favorite_team, group_data):
    """
    Simplified Analysis Engine for World Cup Group Stage Finales.
    Outputs clear, high-stakes key qualification points and exact target scores.
    """
    # Pull stats for both teams
    home_pts = group_data[home_team]["points"]
    away_pts = group_data[away_team]["points"]
    home_gd = group_data[home_team]["gd"]
    away_gd = group_data[away_team]["gd"]
    home_ga = group_data[home_team]["ga"]
    away_ga = group_data[away_team]["ga"]
    
    reasoning = []
    reasoning.append(f"### 🛡️ Key Qualification Points")
    
    # 1. Evaluate Home Team Situation
    if home_pts >= 4:
        reasoning.append(f"* **{home_team} ({home_pts} Pts):** They are sitting pretty. **1 point** in this match guarantees absolute safety. ")
    else:
        reasoning.append(f"* **{home_team} ({home_pts} Pts):** They are in a dangerous spot. A draw leaves them vulnerable to goal difference math, so **they must win to be 100% safe**. If they lose this game, **they are completely OUT of the World Cup**.")
        
    # 2. Evaluate Away Team Situation
    if away_pts >= 4:
        reasoning.append(f"* **{away_team} ({away_pts} Pts):** They are sitting pretty. **1 point** in this match guarantees absolute safety. ")
    else:
        reasoning.append(f"* **{away_team} ({away_pts} Pts):** They are in a dangerous spot. A draw leaves them vulnerable to goal difference math, so **they must win to be 100% safe**. If they lose this game, **they are completely OUT of the World Cup**.")

    # 3. Defensive Asset Check (Has anyone not conceded?)
    if home_ga == 0:
        reasoning.append(f"* **Defensive Note:** **{home_team} has not conceded a single goal yet** this tournament. They can easily park the bus, rest players if needed, and cruise to a low-risk draw.")
    if away_ga == 0:
        reasoning.append(f"* **Defensive Note:** **{away_team} has not conceded a single goal yet** this tournament. They can easily park the bus, rest players if needed, and cruise to a low-risk draw.")

    # 4. Correct Score Logic Selection
    predictions = []
    
    # If one team is desperate (must win) and the other is safe with a draw and hasn't conceded (like Croatia vs Ghana)
    if (home_pts < 4 or sorted) or (away_pts < 4):
        if favorite_team == home_team:
            predictions = [
                {"score": "1 – 0", "type": "Controlled Win", "desc": f"Desperate for the points, {home_team} finds a narrow breakthrough and locks down defensively."},
                {"score": "0 – 0", "type": "Frustrated Stalemate", "desc": f"{home_team} attacks but fails to break through the brick wall defense. A draw might leave them sweating on other results."},
                {"score": "1 – 1", "type": "Chased Equalizer", "desc": "One team catches the other out on a counter, forcing a high-intensity scramble to restore parity."}
            ]
        elif favorite_team == away_team:
            predictions = [
                {"score": "0 – 1", "type": "Away Counter", "desc": f"{away_team} sits back comfortably, absorbs the pressure, and stings on a late counter-attack."},
                {"score": "0 – 0", "type": "Defensive Masterclass", "desc": "A quiet, low-tempo game where the safe team completely refuses to open up spaces."},
                {"score": "1 – 1", "type": "Restored Parity", "desc": "A chaotic mistake forces an equalizer, after which both teams manage their physical exertion."}
            ]
        else:
            predictions = [
                {"score": "0 – 0", "type": "Deadlock", "desc": "Neither side opens up. One wants a point to stay safe, the other can't find a gap."},
                {"score": "1 – 0", "type": "Narrow Edge", "desc": "A single set-piece or penalty decides a very tense, low-scoring affair."}
            ]
    else:
        # Both teams are already sitting on 4+ points and just need to stroll through
        predictions = [
            {"score": "0 – 0", "type": "Mutual Stroll", "desc": "Both teams are safe with a point. Zero risks will be taken by either manager."},
            {"score": "1 – 1", "type": "Friendly Draw", "desc": "An early error trades goals, then both teams pass sideways to secure mutual progression."}
        ]
        
    return {
        "automated_reasoning": "\n".join(reasoning),
        "target_scores": predictions
    }

# --- STREAMLIT UI INTERFACE ---
st.title("⚽ BookieTrap: Grand Finale Matrix")
st.markdown("Select two teams to see exactly what they need to qualify, who is facing elimination, and the exact target scores.")

# --- OFFICIAL COMPREHENSIVE WORLD CUP DATABASE ---
group_stage_database = {
    "Mexico": {"points": 9, "gd": 6, "ga": 1}, "South Africa": {"points": 4, "gd": -1, "ga": 4},
    "South Korea": {"points": 3, "gd": -1, "ga": 3}, "Czechia": {"points": 1, "gd": -4, "ga": 6},
    "Switzerland": {"points": 7, "gd": 4, "ga": 2}, "Canada": {"points": 4, "gd": 5, "ga": 1},
    "Bosnia and Herzegovina": {"points": 4, "gd": -1, "ga": 5}, "Qatar": {"points": 1, "gd": -8, "ga": 9},
    "Brazil": {"points": 7, "gd": 6, "ga": 1}, "Morocco": {"points": 7, "gd": 3, "ga": 2},
    "Scotland": {"points": 3, "gd": -3, "ga": 5}, "Haiti": {"points": 0, "gd": -6, "ga": 7},
    "United States": {"points": 6, "gd": 4, "ga": 2}, "Australia": {"points": 4, "gd": 0, "ga": 3},
    "Paraguay": {"points": 4, "gd": -2, "ga": 5}, "Turkey": {"points": 3, "gd": -2, "ga": 4},
    "Germany": {"points": 6, "gd": 6, "ga": 1}, "Ivory Coast": {"points": 6, "gd": 2, "ga": 3},
    "Ecuador": {"points": 4, "gd": 0, "ga": 2}, "Curaçao": {"points": 1, "gd": -8, "ga": 9},
    "Netherlands": {"points": 7, "gd": 6, "ga": 2}, "Japan": {"points": 5, "gd": 4, "ga": 1},
    "Sweden": {"points": 4, "gd": 0, "ga": 3}, "Tunisia": {"points": 0, "gd": -10, "ga": 11},
    "Belgium": {"points": 5, "gd": 4, "ga": 2}, "Egypt": {"points": 5, "gd": 2, "ga": 3},
    "Iran": {"points": 3, "gd": 0, "ga": 3}, "New Zealand": {"points": 1, "gd": -6, "ga": 7},
    "Spain": {"points": 7, "gd": 5, "ga": 2}, "Cape Verde": {"points": 3, "gd": 0, "ga": 3},
    "Uruguay": {"points": 2, "gd": -1, "ga": 4}, "Saudi Arabia": {"points": 2, "gd": -4, "ga": 6},
    "France": {"points": 9, "gd": 8, "ga": 0}, "Norway": {"points": 6, "gd": 1, "ga": 4},
    "Senegal": {"points": 3, "gd": 2, "ga": 4}, "Iraq": {"points": 0, "gd": -11, "ga": 12},
    "Argentina": {"points": 6, "gd": 5, "ga": 1}, "Austria": {"points": 3, "gd": 0, "ga": 3},
    "Algeria": {"points": 3, "gd": -2, "ga": 5}, "Jordan": {"points": 0, "gd": -3, "ga": 4},
    "Colombia": {"points": 6, "gd": 3, "ga": 2}, "Portugal": {"points": 4, "gd": 5, "ga": 1},
    "DR Congo": {"points": 1, "gd": -1, "ga": 3}, "Uzbekistan": {"points": 0, "gd": -7, "ga": 8},
    "England": {"points": 4, "gd": 2, "ga": 2}, "Ghana": {"points": 4, "gd": 1, "ga": 0}, # 0 Goals Conceded
    "Croatia": {"points": 3, "gd": -1, "ga": 4}, "Panama": {"points": 0, "gd": -2, "ga": 2}
}

all_teams_list = sorted(list(group_stage_database.keys()))

# Interactive Layout Forms
col1, col2 = st.columns(2)
with col1:
    team_a = st.selectbox("Select Home Team", options=all_teams_list, index=12) # Defaults to Croatia
with col2:
    team_b = st.selectbox("Select Away Team", options=all_teams_list, index=19) # Defaults to Ghana

odds_favorite = st.radio(
    "Who do the bookies have put as favourites to win?",
    options=[team_a, team_b, "Even / No Favorite"],
    index=0
)

if team_a == team_b:
    st.error("Error: Please select two different competing teams.")
else:
    # Run simple prediction engine
    analytics = calculate_automated_predictions(
        home_team=team_a, 
        away_team=team_b, 
        favorite_team=odds_favorite,
        group_data=group_stage_database
    )

    # Output to Streamlit Page
    st.markdown("---")
    st.markdown(analytics["automated_reasoning"])
    
    if analytics["target_scores"]:
        st.markdown("### 🎯 Target Correct Score Predictions")
        for target in analytics["target_scores"]:
            st.info(f"**{target['score']}** ({target['type']}) — {target['desc']}")
