import streamlit as st
import requests

# 1. API CONFIG (Using a conceptual endpoint for World Cup 2026)
API_URL = "https://worldcup26.ir/get" 

def fetch_match_data():
    # Fetching games and standings
    response = requests.get(f"{API_URL}/games")
    return response.json() if response.status_code == 200 else []

def evaluate_motivation(pts, gd):
    if pts >= 6: return "Low (Already Qualified - Trap Risk)"
    if pts == 0: return "High (Desperate/Pride)"
    return "Balanced"

st.title("⚽ Bookie Killer 2026")

# 2. Main Logic
if st.button("Analyze Matches"):
    matches = fetch_match_data()
    for match in matches:
        st.subheader(f"{match['home']} vs {match['away']}")
        
        home_mot = evaluate_motivation(match['home_pts'], match['home_gd'])
        away_mot = evaluate_motivation(match['away_pts'], match['away_gd'])
        
        st.write(f"Home Motivation: **{home_mot}**")
        st.write(f"Away Motivation: **{away_mot}**")
        
        # 3. Trap Detection
        if "Already Qualified" in home_mot and "Desperate" in away_mot:
            st.warning("🚨 TRAP DETECTED: Potential motivation mismatch!")
