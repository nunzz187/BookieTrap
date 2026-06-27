import streamlit as st

# --- DATABASE ---
# Team data: Points, Goal Difference (GD), Qualification Status
group_l = {
    "England": {"pts": 4, "gd": 2, "qual": True, "elim": False},
    "Ghana": {"pts": 4, "gd": 1, "qual": True, "elim": False},
    "Croatia": {"pts": 3, "gd": -1, "qual": False, "elim": False},
    "Panama": {"pts": 0, "gd": -2, "qual": False, "elim": True}
}

# Valid remaining group stage matches
valid_matches = {
    "England": ["Panama"], "Panama": ["England"],
    "Ghana": ["Croatia"], "Croatia": ["Ghana"]
}

def get_scenarios(team, data):
    if data['elim']:
        return [f"* **Status:** Already eliminated. Playing for pride."]
    if data['qual']:
        return [
            f"* **Win:** Moves to {data['pts']+3} points. Secures top seeding.",
            f"* **Draw:** Already through; maintains group standing.",
            f"* **Loss:** Already through; awaits final seeding outcome."
        ]
    return [
        f"* **Win:** Moves to {data['pts']+3} points. Automatically qualifies.",
        f"* **Draw:** Moves to {data['pts']+1} points. Depends on third-place rankings; GD ({data['gd']}) is critical.",
        f"* **Loss:** Stays on {data['pts']} points. Likely eliminated."
    ]

def get_predictions(home, away, h_data, a_data):
    # Logic for match predictions with team names included
    if home == "England" or away == "England":
        return [
            {"score": f"{home} 3 – 0 {away}", "reasoning": "- Group leader dominance & high-scoring win"},
            {"score": f"{home} 2 – 0 {away}", "reasoning": "- Controlled win to secure top seed"},
            {"score": f"{home} 1 – 1 {away}", "reasoning": "- Late rotation allowing a consolation goal"}
        ]
    elif home == "Croatia" or away == "Croatia":
        return [
            {"score": f"{home} 2 – 1 {away}", "reasoning": "- Survival mode (Croatia) & high intensity"},
            {"score": f"{home} 1 – 1 {away}", "reasoning": "- Desperate attack vs qualified defense"},
            {"score": f"{home} 1 – 2 {away}", "reasoning": "- Counter-attack efficiency from the qualified team"}
        ]
    return [{"score": f"{home} 1 – 1 {away}", "reasoning": "- Standard match progression"}]

# --- UI ---
st.title("⚽ World Cup Qualification Matrix")
all_teams = sorted(list(group_l.keys()))
col1, col2 = st.columns(2)
home = col1.selectbox("Home Team", all_teams)
away = col2.selectbox("Away Team", all_teams)

if st.button("Go"):
    if home == away:
        st.error("Please select two different teams.")
    elif away not in valid_matches.get(home, []):
        st.error("Invalid Match: These teams are not scheduled to play each other in this round.")
    else:
        h_d, a_d = group_l[home], group_l[away]
        
        st.subheader(f"📋 What {home} Needs")
        for s in get_scenarios(home, h_d): st.write(s)
            
        st.subheader(f"📋 What {away} Needs")
        for s in get_scenarios(away, a_d): st.write(s)
            
        st.subheader("🎯 Target Correct Score Predictions")
        for pred in get_predictions(home, away, h_d, a_d):
            st.markdown(f"**Score:** {pred['score']}")
            st.markdown(f"**Reasoning:** {pred['reasoning']}")
            st.markdown("---")
