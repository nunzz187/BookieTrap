import streamlit as st

def get_qualification_status(team, pts, gd):
    # Logic to handle team status based on points and group context
    if pts >= 4:
        return "Qualified"
    elif pts == 3:
        return "Fighting to qualify"
    else:
        return "Eliminated"

def get_scenarios(team, pts, gd, is_qualified, is_eliminated):
    """Generates the simple bullet points for qualification needs."""
    if is_eliminated:
        return [f"* **Status:** Eliminated. Playing for pride."]
    
    if is_qualified:
        return [
            f"* **Win:** Secures top seeding for the Round of 32.",
            f"* **Draw:** Already through; maintains group standing.",
            f"* **Loss:** Already through; awaits final seeding outcome."
        ]
    
    # Logic for teams still fighting (like Croatia)
    return [
        f"* **Win:** Reaches 6 points; guaranteed qualification.",
        f"* **Draw:** Reaches 4 points; relies on third-place ranking table.",
        f"* **Loss:** Stays on 3 points; likely eliminated due to negative GD."
    ]

def get_predictions(home_team, away_team, h_pts, a_pts, h_qual, a_qual):
    """Generates simple score predictions based on team status."""
    # Croatia vs Ghana example logic
    if (home_team == "Croatia" and h_pts == 3) and (away_team == "Ghana" and a_qual):
        return [
            {"score": "2 – 1", "reasoning": "- Need to Win (Croatia) & other team qualified (Ghana)"},
            {"score": "1 – 0", "reasoning": "- Need to Win (Croatia) & clean sheet focus"},
            {"score": "0 – 0", "reasoning": "- Resting players (Ghana) & brick wall defense"}
        ]
    # Default fallback
    return [{"score": "1 – 1", "reasoning": "- Standard match progression"}]

# Database
group_l = {
    "England": {"pts": 4, "gd": 2, "qual": True, "elim": False},
    "Ghana": {"pts": 4, "gd": 1, "qual": True, "elim": False},
    "Croatia": {"pts": 3, "gd": -1, "qual": False, "elim": False},
    "Panama": {"pts": 0, "gd": -2, "qual": False, "elim": True}
}

st.title("⚽ World Cup Qualification Matrix")

col1, col2 = st.columns(2)
home = col1.selectbox("Home Team", list(group_l.keys()))
away = col2.selectbox("Away Team", list(group_l.keys()))

if home != away:
    h_data = group_l[home]
    a_data = group_l[away]
    
    st.subheader(f"📋 What {home} Needs")
    for s in get_scenarios(home, h_data['pts'], h_data['gd'], h_data['qual'], h_data['elim']):
        st.write(s)
        
    st.subheader(f"📋 What {away} Needs")
    for s in get_scenarios(away, a_data['pts'], a_data['gd'], a_data['qual'], a_data['elim']):
        st.write(s)
        
    st.subheader("🎯 Target Correct Score Predictions")
    for pred in get_predictions(home, away, h_data['pts'], a_data['pts'], h_data['qual'], a_data['qual']):
        st.markdown(f"**Score:** {pred['score']}")
        st.markdown(f"**Reasoning:** {pred['reasoning']}")
        st.markdown("---")

