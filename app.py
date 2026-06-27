import streamlit as st

# Configure the page for a clean mobile-first view
st.set_page_config(page_title="Trap Detective Engine", page_icon="⚽", layout="centered")

# Custom Dark Mode Styling using Streamlit markdown with corrected parameter
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', monospace; }
    .stButton>button { width: 100%; background-color: #00ffcc; color: black; font-weight: bold; border-radius: 8px; }
    .stButton>button:hover { background-color: #00cc99; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ TRAP DETECTIVE ENGINE")
st.write("---")
st.subheader("Analyze Match Motivation & Bookie Traps")

# User Inputs for any custom match
col1, col2 = st.columns(2)
with col1:
    home_team = st.text_input("Home Team Name", "Manchester United")
with col2:
    away_team = st.text_input("Away Team Name", "League Two Underdog")

st.write("---")

# Selection of conditions based on your logic
fav_selection = st.radio("Who is the heavy favorite on paper?", (home_team, away_team))
underdog = away_team if fav_selection == home_team else home_team

st.subheader("Analyze Motivation States")

fav_state = st.selectbox(
    f"What is the motivation state of the favorite ({fav_selection})?",
    ["Coasting / Position Secured / Fixture Congestion", "Must Win / Title Chase / Vital Points"]
)

und_state = st.selectbox(
    f"What is the motivation state of the underdog ({underdog})?",
    ["Desperate / Fighting Relegation / Must Qualify", "Safe Mid-table / Out of Tournament"]
)

st.write("---")

# The Brain: Calculating your exact rules
if st.button("RUN TRAP ANALYSIS"):
    st.subheader("🕵️‍♂️ Detective Breakdown")
    
    # RULE 1: The Adrenaline Upset (Coasting Fav vs Desperate Underdog)
    if fav_state == "Coasting / Position Secured / Fixture Congestion" and und_state == "Desperate / Fighting Relegation / Must Qualify":
        st.error(f"⚠️ CRITICAL BOOKIE TRAP DETECTED: THE ADRENALINE UPSET")
        st.write(f"**The Blueprint:** {fav_selection} has their position locked down or is facing extreme fixture fatigue. They will heavily rotate the squad or play in low-gear to avoid injuries. Meanwhile, {underdog} is fighting for literal survival.")
        st.write(f"**The Reality:** {underdog}'s raw urgency will outwork the favorite's passive quality on the pitch. The public will blindly back the big name, completely burning their betting slips.")
        st.info("💡 **Sharp Market Angle:** Look heavily at Underdog Double Chance (Win or Draw) or Underdog +1.5 Asian Handicap.")
        
    # RULE 2: The Pride-Saving Draw
    elif fav_state == "Coasting / Position Secured / Fixture Congestion" and und_state == "Safe Mid-table / Out of Tournament":
        st.warning(f"⚽ THE PRIDE-SAVING DEADLOCK")
        st.write(f"**The Blueprint:** Neither team has a massive mathematical gun to their head. {fav_selection} is coasting and won't waste energy pursuing a 4-0 win. However, because they are a big club, their pride will not allow an embarrassing defeat.")
        st.write(f"**The Reality:** The favorite will control a slow, horizontal, low-tempo game. They will comfortably accept a flat stalemate to protect their legs.")
        st.success("🎯 **Predicted Outcomes:** Look for low-scoring draws like 0-0 or 1-1.")
        st.info("💡 **Sharp Market Angle:** Under 2.5 Match Goals or Match Result: DRAW.")
        
    # RULE 3: Normal Competitive State
    else:
        st.success(f"🔥 GREEN LIGHT: FULL COMPETITIVE MATCH")
        st.write(f"**The Blueprint:** {fav_selection} strictly needs these points for a title, promotion, or qualification. They cannot afford to coast or heavily rotate.")
        st.write(f"**The Reality:** Motivation is fully aligned with squad quality here. The favorite will play at 100% capacity.")
        st.info(f"💡 **Sharp Market Angle:** Standard on-paper analysis applies. Favorite Straight Win is playable if value exists.")
