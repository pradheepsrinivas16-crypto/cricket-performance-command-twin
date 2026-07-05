import streamlit as st
import pandas as pd
import numpy as np
import cv2
import requests
import json
import matplotlib.pyplot as plt
from google import genai

# ==========================================================
# 📡 CLOUD INTELLIGENCE SERVER ENGINE (Replaces Local Ollama)
# ==========================================================

# This looks for your Gemini API Key in Streamlit Secrets, 
# or adds a secure password box in your app's sidebar so you can paste it live.
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

def query_local_ollama(prompt, model_name="gemini-2.5-flash"):
    """
    We kept the exact same function name so that your 22,000+ characters 
    of code below won't break when buttons look for it!
    """
    if not api_key:
        return "⚠️ Cloud GenAI node unconfigured. Please enter your Gemini API Key in the sidebar input box to activate the intelligence engine."
    
    try:
        # Routes the tactical coach prompt directly to the live cloud API
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"⚠️ Cloud Generation Fault: {str(e)}"

# ==========================================================
# 🎨 Franchise Level Custom Theme (Your original code continues below)
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