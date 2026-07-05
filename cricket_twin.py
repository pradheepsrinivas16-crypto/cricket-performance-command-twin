import streamlit as st
import pandas as pd
import numpy as np
import cv2
import requests
import json
import matplotlib.pyplot as plt
from google import genai

# ==========================================================
# 📡 GLOBAL CLOUD INTELLIGENCE SERVER ENGINE
# ==========================================================
# Using .get() prevents Streamlit from throwing a KeyError if the secret doesn't exist yet!
secret_key = st.secrets.get("GEMINI_API_KEY", None)

# If it's not in secrets, show the password input box in the sidebar
if not secret_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
else:
    api_key = secret_key

if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

def query_local_ollama(prompt, model_name="gemini-2.5-flash"):
    """Global handler ensuring all engine metrics route out of localhost"""
    if not api_key:
        return "⚠️ Cloud GenAI node unconfigured. Please enter your Gemini API Key in the sidebar input box to activate the intelligence engine."
    try:
        response = client.models.generate_content(model=model_name, contents=prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Cloud Generation Fault: {str(e)}"

# ==========================================================
# 🎨 Franchise Level Custom Theme
# ==========================================================
st.markdown("""
<style>
.reportview-container { background: #070d19; }
.broadcast-header {
    background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
    padding: 25px; border-radius: 12px; border-bottom: 4px solid #3b82f6;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.5); text-align: left; margin-bottom: 25px;
}
.metric-box, .simulator-card {
    background: #1e293b; padding: 22px; border-radius: 10px;
    border: 1px solid rgba(59, 130, 246, 0.2); border-left: 5px solid #3b82f6;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.4); text-align: center; margin-bottom: 15px;
}
.label-title { color: #94a3b8; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
.value-display { color: #ffffff; font-size: 32px; font-weight: 800; margin-top: 4px; font-family: monospace; }
.status-alert { padding: 12px; border-radius: 6px; text-align: center; font-weight: 700; font-size: 16px; margin: 15px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="broadcast-header">
    <h1 style="color: #ffffff; margin: 0; font-size: 28px;">🏏 ELITE SQUAD PERFORMANCE ENGINE</h1>
    <p style="color: #3b82f6; margin: 5px 0 0 0; font-weight: 600;">Franchise Analytics & Live Tactical Sandbox Platform</p>
</div>
""", unsafe_allow_html=True)

# Setup Dashboard Tabs
tab1, tab4 = st.tabs(["🎯 STRATEGY SANDBOX", "🏥 ATHLETE BASE & RECOVERY MATRIX"])

# ==========================================================
# 🎯 MODULE 1: STRATEGY SANDBOX
# ==========================================================
with tab1:
    st.markdown("### 🔍 Strategic Opponent Weakness Dossier")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("#### 📋 Targeted Setup")
        batsman_profile = st.selectbox(
            "Select Opposition Batsman Profile",
            ["Chris Gayle (LHB - Power Opening Anchor)", "Virat Kohli (RHB - Technical Accumulator)", "AB de Villiers (RHB - 360 Dynamic Finisher)"]
        )
        attack_option = st.selectbox(
            "Our Tactical Attack Option",
            ["Express Right-Arm Fast-Bowler", "Left-Arm Orthodox Spinner", "Mystery Off-Break Variant"]
        )
        match_location = st.selectbox(
            "Match Location / Ground Analytics",
            ["M. Chinnaswamy Stadium, Bengaluru (Small Boundaries / Flat Deck)", "M.A. Chidambaram Stadium, Chennai (Slow Turner)", "Wankhede Stadium, Mumbai (High Bounce / Dew Factor)"]
        )
        balls_faced = st.slider("Batsman Lifecycle Progression (Balls Faced)", 1, 60, 5)

    with col2:
        st.markdown("#### 📋 Pro Analyst Intelligence Streams")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="metric-box"><div class="label-title">Core Leakage Sector Zone</div><div class="value-display" style="font-size: 18px; color: #3b82f6;">Covers & Square Leg Arc</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-box"><div class="label-title">Lifecycle Performance Curve</div><div class="value-display" style="font-size: 16px;">SR 90 (First 25 Balls) -> SR 110 (Post 25)</div></div>', unsafe_allow_html=True)
            
        st.markdown("<p style='color: #4ade80; font-weight: 600;'>⚡ Current Technical Vulnerability Vector: <span style='color: #ffffff;'>High vulnerability to incoming rapid full deliveries hitting the pads early on.</span></p>", unsafe_allow_html=True)
        
        if st.button("🔥 Compile Head-Coach Pre-Match Kill-Plan"):
            with st.spinner("Processing match data variables..."):
                kill_prompt = f"""
                Act as an elite T20 Head Coach and Principal Data Analyst. 
                Develop a highly aggressive match-plan targeting an opposition batsman with these profile metrics:
                - Batsman Profile: {batsman_profile}
                - Bowler Option Handled: {attack_option}
                - Playing Venue Context: {match_location}
                - Match State (Balls Faced): {balls_faced} balls faced.
                
                Provide real tactical fielding deployment advice and delivery lines. Keep it crisp, structured, and punchy.
                """
                strategy_res = query_local_ollama(kill_prompt)
                st.markdown(strategy_res)

# ==========================================================
# 🏥 MODULE 4: ATHLETE BASE & RECOVERY MATRIX
# ==========================================================
with tab4:
    st.markdown("### 🏥 Acute-to-Chronic Clinical Fatigue & Prescription Suite")
    st.write("---")
    col_l1, col_l2 = st.columns([1, 1.2])
    
    with col_l1:
        st.subheader("🧬 High-Performance Telemetry Inputs")
        p_name = st.text_input("Registered Athlete Profile", "Jasprit Bumrah (Fast Bowler)")
        acute = st.slider("7-Day Acute Fatigue Loading Index", 1.0, 15.0, 9.2, step=0.1)
        chronic = st.slider("28-Day Chronic Base Capacity Index", 1.0, 15.0, 5.8, step=0.1)
        injuries = st.multiselect(
            "Pathological History Registry", 
            ["Lumbar Spine Stress Fracture", "Patellar Tendonitis", "Grade 2 Hamstring Strain"], 
            default=["Lumbar Spine Stress Fracture"]
        )
        sleep_efficiency = st.slider("Polysomnographic Sleep Efficiency Level (%)", 30, 100, 74)
        
        calc_acwr = round(acute / max(0.1, chronic), 2)
        risk_pct = min(98, int((calc_acwr * 38) + (len(injuries) * 12) - (sleep_efficiency - 70) * 0.2))

    with col_l2:
        st.subheader("📊 Workload Matrix Outputs")
        cl1, cl2 = st.columns(2)
        cl1.markdown(f'<div class="metric-box"><div class="label-title">Calculated Workload Ratio (ACWR)</div><div class="value-display">{calc_acwr}</div></div>', unsafe_allow_html=True)
        cl2.markdown(f'<div class="metric-box"><div class="label-title">Tissue Breakdown Risk Probability</div><div class="value-display">{risk_pct}%</div></div>', unsafe_allow_html=True)
        
        st.write("---")
        if st.button("📋 Compile Clinical Recovery & Selection Manifesto"):
            with st.spinner("Processing medical variables and loading scripts..."):
                load_prompt = f"""
                Act as the Chief Medical Officer and Elite Sports Scientist for a national cricket team.
                Analyze player: {p_name}. ACWR: {calc_acwr}. Pathological History: {injuries}. Sleep Efficiency: {sleep_efficiency}%.
                Generate a comprehensive, team-management ready recovery directive using these exact markdown headers:
                
                ### 🏋️ HIGH-PERFORMANCE WORKLOAD RECONSTRUCTION
                ### 🥗 CLINICAL NUTRITION & BIO-INFUSION PLAN
                ### 📅 MATCH AVAILABILITY CONCLUSION
                """
                load_res = query_local_ollama(load_prompt)
                st.markdown(load_res)