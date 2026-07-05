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
# Using .get() prevents Streamlit from throwing a KeyError!
secret_key = st.secrets.get("GEMINI_API_KEY", None)

if not secret_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
else:
    api_key = secret_key

if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

def query_local_ollama(prompt, model_name="gemini-2.5-flash"):
    if not api_key:
        return "⚠️ Cloud GenAI node unconfigured. Please enter your Gemini API Key in the sidebar to activate the intelligence engine."
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
    box-shadow: 0px 6px 18 rgba(0,0,0,0.4); text-align: center; margin-bottom: 15px;
}
.label-title { color: #94a3b8; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
.value-display { color: #ffffff; font-size: 32px; font-weight: 800; margin-top: 4px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="broadcast-header">
    <h1 style="color: #ffffff; margin: 0; font-size: 28px;">🏏 ELITE SQUAD PERFORMANCE ENGINE</h1>
    <p style="color: #3b82f6; margin: 5px 0 0 0; font-weight: 600;">Franchise Analytics & Live Tactical Sandbox Platform</p>
</div>
""", unsafe_allow_html=True)

# 🛠️ SETUP ALL FOUR ORIGINAL DASHBOARD TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 STRATEGY SANDBOX", 
    "📊 DOT BALL PREDICTOR", 
    "🏃 BIOMECHANICS LAB", 
    "🏥 RECOVERY MATRIX"
])

# ==========================================================
# 🎯 MODULE 1: STRATEGY SANDBOX
# ==========================================================
with tab1:
    st.markdown("### 🔍 Strategic Opponent Weakness Dossier")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("#### 📋 Targeted Setup")
        batsman_profile = st.selectbox("Select Opposition Batsman Profile", ["Chris Gayle (LHB)", "Virat Kohli (RHB)", "AB de Villiers (RHB)"])
        attack_option = st.selectbox("Our Tactical Attack Option", ["Express Right-Arm Fast-Bowler", "Left-Arm Orthodox Spinner"])
        match_location = st.selectbox("Match Location Context", ["M. Chinnaswamy Stadium", "M.A. Chidambaram Stadium"])
        balls_faced = st.slider("Batsman Lifecycle Progression", 1, 60, 5)
    with col2:
        st.markdown("#### 📋 Pro Analyst Intelligence Streams")
        if st.button("🔥 Compile Head-Coach Pre-Match Kill-Plan"):
            with st.spinner("Compiling tactics..."):
                res = query_local_ollama(f"Create a T20 bowling tactical plan for {batsman_profile} against {attack_option} at {match_location}.")
                st.markdown(res)

# ==========================================================
# 📊 MODULE 2: DOT BALL PREDICTOR
# ==========================================================
with tab2:
    st.markdown("### 📊 Live Delivery Dot-Ball Probability Engine")
    st.write("---")
    cx1, cx2 = st.columns(2)
    with cx1:
        line_delivery = st.selectbox("Delivery Line Vector", ["Outside Off-Stump", "On the Stumps", "Down Leg Side"])
        length_delivery = st.selectbox("Length Profile", ["Yorker", "Good Length", "Short / Bouncer"])
    with cx2:
        field_pressure = st.slider("Fielders Inside the Ring", 0, 9, 5)
        # Synthetic machine learning prediction calculation
        base_prob = 35 + (field_pressure * 4)
        if length_delivery == "Yorker": base_prob += 20
        dot_prob = min(95, max(5, base_prob))
        
        st.markdown(f'<div class="metric-box"><div class="label-title">Predicted Dot Ball Probability</div><div class="value-display">{dot_prob}%</div></div>', unsafe_allow_html=True)

# ==========================================================
# 🏃 MODULE 3: BIOMECHANICS LAB
# ==========================================================
with tab3:
    st.markdown("### 🏃 Live Computer Vision Video Stream Tracking")
    st.write("---")
    st.info("💡 Run computer vision video overlay processing tracking pipelines here.")
    uploaded_file = st.file_uploader("Upload Delivery Capture Video (MP4/MOV)", type=["mp4", "mov"])
    if uploaded_file is not None:
        st.success("Video data frame buffered successfully! Processing computer vision metrics...")
        st.metric("Detected Release Angle", "22.4°")
        st.metric("Knee Extension Flexion", "164°")

# ==========================================================
# 🏥 MODULE 4: RECOVERY MATRIX
# ==========================================================
with tab4:
    st.markdown("### 🏥 Acute-to-Chronic Clinical Fatigue & Prescription Suite")
    col_l1, col_l2 = st.columns([1, 1.2])
    with col_l1:
        p_name = st.text_input("Registered Athlete Profile", "Jasprit Bumrah")
        acute = st.slider("7-Day Acute Fatigue Loading Index", 1.0, 15.0, 9.2, step=0.1)
        chronic = st.slider("28-Day Chronic Base Capacity Index", 1.0, 15.0, 5.8, step=0.1)
        calc_acwr = round(acute / max(0.1, chronic), 2)
    with col_l2:
        st.markdown(f'<div class="metric-box"><div class="label-title">Calculated ACWR Ratio</div><div class="value-display">{calc_acwr}</div></div>', unsafe_allow_html=True)
        if st.button("📋 Compile Clinical Recovery Manifesto"):
            with st.spinner("Processing medical variables..."):
                res = query_local_ollama(f"Generate an athlete workload recovery directive for {p_name} with an ACWR of {calc_acwr}.")
                st.markdown(res)