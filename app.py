import streamlit as st

# --- 48-TEAM DATABASE & FIXTURES ---
# Only include matches scheduled for the current group stage round
group_data = {
    "England": {"pts": 4, "gd": 2, "qual": True, "elim": False},
    "Ghana": {"pts": 4, "gd": 1, "qual": True, "elim": False},
    "Croatia": {"pts": 3, "gd": -1, "qual": False, "elim": False},
    "Panama": {"pts": 0, "gd": -2, "qual": False, "elim": True},
    # Add other teams here in the same format
}

valid_matches = {
    "England": ["Panama"], "Panama": ["England"],
    "Ghana": ["Croatia"], "Croatia": ["Ghana"],
    # Add other valid match pairs here
}

def get_scenarios(team_name, data):
    if data['elim']:
        return [f"* **Status:** Eliminated. Playing for pride."]
    if data['qual']:
        return [
            f"* **Win:** Secures top seeding for the Round of 32.",
            f"* **Draw:** Already through; maintains group standing.",
            f"* **Loss:** Already through; awaits final seeding outcome."
        ]
    return [
        f"* **Win:** Reaches {data['pts']+3} points; guaranteed qualification.",
        f"* **Draw:** Reaches {data['pts']+1} points; relies on third-place ranking.",
        f"* **Loss:** Stays on {data['pts']} points; likely elimination due to GD ({data['gd']})."
    ]

def get_predictions(home, away, h_data, a_data):
    # Simplified logic based on team status
    if h_data['qual'] and a_data['qual']:
        return [{"score": "1 – 1", "reasoning": "- Both teams qualified & low intensity"}]
    elif not h_data['qual'] and a_data['qual']:
        return [
            {"score": "2 – 1", "reasoning": f"- Need to Win ({home}) & other team qualified ({away})"},
            {"score": "1 – 0", "reasoning": f"- Need to Win ({home}) & clean sheet focus"}
        ]
    else:
        return [{"score": "1 – 0", "reasoning": "- Winner takes all; survival mode"}]

# --- STREAMLIT UI ---
st.title("⚽ World Cup Qualification Matrix")

all_teams = sorted(list(group_data.keys()))
col1, col2 = st.columns(2)
home = col1.selectbox("Home Team", all_teams)
away = col2.selectbox("Away Team", all_teams)

if st.button("Go"):
    if home == away:
        st.error("Please select two different teams.")
    elif away not in valid_matches.get(home, []):
        st.error("Invalid Match: These teams are not scheduled to play each other in this round.")
    else:
        h_d, a_d = group_data[home], group_data[away]
        
        st.subheader(f"📋 What {home} Needs")
        for s in get_scenarios(home, h_d): st.write(s)
            
        st.subheader(f"📋 What {away} Needs")
        for s in get_scenarios(away, a_d): st.write(s)
            
        st.subheader("🎯 Target Correct Score Predictions")
        for pred in get_predictions(home, away, h_d, a_d):
            st.markdown(f"**Score:** {pred['score']}")
            st.markdown(f"**Reasoning:** {pred['reasoning']}")
            st.markdown("---")
