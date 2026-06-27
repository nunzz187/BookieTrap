import streamlit as st

def generate_dynamic_analytics(home_team, away_team, favorite_team, group_data):
    """
    Simplified World Cup Analytics Engine.
    Outputs clean, high-impact bullets and ultra-short correct score lines.
    """
    home_pts = group_data[home_team]["points"]
    away_pts = group_data[away_team]["points"]
    home_gd = group_data[home_team]["gd"]
    away_gd = group_data[away_team]["gd"]
    home_ga = group_data[home_team]["ga"]
    away_ga = group_data[away_team]["ga"]
    
    # --- DYNAMIC TEAM SCENARIOS (WHAT THEY NEED) ---
    scenarios = []
    
    # Home Team Scenarios
    scenarios.append(f"### 📋 What {home_team} Needs")
    if home_pts >= 4:
        scenarios.append(f"* **Win:** Moves to {home_pts + 3} points. Secures top seeding for the Round of 32.")
        scenarios.append(f"* **Draw:** Moves to {home_pts + 1} points. Automatically secures a knockout spot regardless of other results.")
        scenarios.append(f"* **Loss:** Stays on {home_pts} points. Still highly likely to qualify, but depends on goal difference rankings.")
    else:
        scenarios.append(f"* **Win:** Moves to {home_pts + 3} points. Automatically securing a knockout spot regardless of other results.")
        scenarios.append(f"* **Draw:** Moves to {home_pts + 1} points. Moves to {home_pts + 1} points on the third-place ranking table, but because of goal difference ({home_gd}), they risk being surpassed by other teams.")
        scenarios.append(f"* **Loss:** Stays on {home_pts} points. With {home_pts} points and a negative goal difference, it is statistically very unlikely to rank in the top 8 of third-placed teams, meaning elimination.")

    # Away Team Scenarios
    scenarios.append(f"### 📋 What {away_team} Needs")
    if away_pts >= 4:
        scenarios.append(f"* **Win:** Moves to {away_pts + 3} points. Secures top seeding for the Round of 32.")
        scenarios.append(f"* **Draw:** Moves to {away_pts + 1} points. Automatically secures a knockout spot regardless of other results.")
        scenarios.append(f"* **Loss:** Stays on {away_pts} points. Still highly likely to qualify, but depends on goal difference rankings.")
    else:
        scenarios.append(f"* **Win:** Moves to {away_pts + 3} points. Automatically securing a knockout spot regardless of other results.")
        scenarios.append(f"* **Draw:** Moves to {away_pts + 1} points. Moves to {away_pts + 1} points on the third-place ranking table, but because of goal difference ({away_gd}), they risk being surpassed by other teams.")
        scenarios.append(f"* **Loss:** Stays on {away_pts} points. With {away_pts} points and a negative goal difference, it is statistically very unlikely to rank in the top 8 of third-placed teams, meaning elimination.")

    # --- ULTRA-SIMPLE SCORE PREDICTIONS ---
    predictions = []
    
    # Logic if one team is desperate and the other is qualified/safe
    if home_pts < 4 and away_pts >= 4:
        # e.g., Croatia vs Ghana scenario
        predictions = [
            {"score": "2 – 1", "reasoning": f"- Need to Win ({home_team}) & other team qualified ({away_team})"},
            {"score": "1 – 0", "reasoning": f"- Need to Win ({home_team}) & clean sheet focus"},
            {"score": "0 – 0", "reasoning": f"- Resting players ({away_team}) & brick wall defense"}
        ]
    elif away_pts < 4 and home_pts >= 4:
        predictions = [
            {"score": "1 – 2", "reasoning": f"- Need to Win ({away_team}) & other team qualified ({home_team})"},
            {"score": "0 – 1", "reasoning": f"- Need to Win ({away_team}) & clean sheet focus"},
            {"score": "0 – 0", "reasoning": f"- Resting players ({home_team}) & brick wall defense"}
        ]
    elif home_pts >= 4 and away_pts >= 4:
        # Both already qualified
        predictions = [
            {"score": "0 – 0", "reasoning": "- Both teams qualified & resting key players"},
            {"score": "1 – 1", "reasoning": "- Both teams qualified & low intensity cruise"}
        ]
    else:
        # Both desperate
        predictions = [
            {"score": "1 – 0", "reasoning": f"- Winner takes all & survival mode"},
            {"score": "0 – 1", "reasoning": f"- Winner takes all & survival mode"},
            {"score": "1 – 1", "reasoning": f"- High risk draw leaving both vulnerable"}
        ]
        
    return {
        "text_scenarios": "\n".join(scenarios),
        "scores": predictions
    }

# --- STREAMLIT USER INTERFACE ---
st.set_page_config(page_title="BookieTrap Matrix", layout="centered")
st.title("⚽ BookieTrap: Grand Finale Matrix")
st.markdown("Select your matching pair to instantly get qualification stakes and target score presets.")

# --- OFFICIAL COMPREHENSIVE 48-TEAM DATABASE ---
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
    "England": {"points": 4, "gd": 2, "ga": 2}, "Ghana": {"points": 4, "gd": 1, "ga": 0},
    "Croatia": {"points": 3, "gd": -1, "ga": 4}, "Panama": {"points": 0, "gd": -2, "ga": 2}
}

all_teams_list = sorted(list(group_stage_database.keys()))

# Match Selector UI Elements
col1, col2 = st.columns(2)
with col1:
    team_a = st.selectbox("Select Home Team", options=all_teams_list, index=12)  # Croatia
with col2:
    team_b = st.selectbox("Select Away Team", options=all_teams_list, index=19)  # Ghana

odds_favorite = st.radio(
    "Who do the bookies have put as favourites to win?",
    options=[team_a, team_b, "Even / No Favorite"],
    index=0
)

if team_a == team_b:
    st.error("Error: Please select two different competing teams.")
else:
    # Run simple prediction calculation
    analytics = generate_dynamic_analytics(
        home_team=team_a, 
        away_team=team_b, 
        favorite_team=odds_favorite,
        group_data=group_stage_database
    )

    # --- RENDER OUTPUT STAGE ---
    st.markdown("---")
    st.markdown(analytics["text_scenarios"])
    
    st.markdown("### 🎯 Target Correct Score Predictions")
    for target in analytics["scores"]:
        st.markdown(f"**Score:** {target['score']}")
        st.markdown(f"**Reasoning:** {target['reasoning']}")
        st.markdown("")
