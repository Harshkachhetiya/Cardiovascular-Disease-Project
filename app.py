"""
CardioPredict - AI-Powered Heart Disease Risk Assessment Platform
Standard Operating Procedure (SOP) Compliant Application
Department of Computer Engineering, Darshan University
Student: Harsh Kachhetiya • Semester 5 Machine Learning
"""
import streamlit as st
from styles.theme import inject_theme
from components.navbar import render_navbar
from pages_app import (
    overview,
    prediction,
    analytics,
    evaluation,
    guidance,
    about
)

# -------------------------------------------------------------
# APPLICATION CONFIGURATION
# -------------------------------------------------------------
st.set_page_config(
    page_title="CardioPredict — Heart Disease Risk Assessment",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom modern dark Tailwind/Shadcn Vercel theme
inject_theme()

# Top Navigation Bar with active indicator
current_page = render_navbar()

# -------------------------------------------------------------
# ROUTER: Clean Multi-View Routing
# -------------------------------------------------------------
if current_page in ("Assess Risk", "Overview", "Risk Prediction"):
    overview.render()
elif current_page == "Analytics":
    analytics.render()
elif current_page in ("Model Evaluation", "Evaluation"):
    evaluation.render()
elif current_page in ("Clinical Guidance", "Health Guidance", "Guidance"):
    guidance.render()
elif current_page in ("About Project", "About"):
    about.render()
else:
    overview.render()

# -------------------------------------------------------------
# ACADEMIC SOP FOOTER (DARK SLATE THEME)
# -------------------------------------------------------------
st.markdown("""<footer style="padding: 40px 0 24px 0; border-top: 1px solid #1E1B3A; margin-top: 64px;">
<div style="display: grid; grid-template-columns: 1fr 1fr 2fr; gap: 32px; margin-bottom: 24px;">
<div>
<div style="font-size: 14px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">SOP Sections</div>
<div style="display: flex; flex-direction: column; gap: 6px; font-size: 13px; color: #94A3B8;">
<span>• Heart Disease Risk Assessment</span>
<span>• Exploratory Data Analysis (EDA)</span>
<span>• Model Evaluation & Overfitting Audit</span>
<span>• Dual Ensemble Hyperparameter Tuning</span>
<span>• Clinical Health Guidance</span>
<span>• Academic Viva Defense Guide</span>
</div>
</div>
<div>
<div style="font-size: 14px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Academic Context</div>
<p style="font-size: 13px; color: #94A3B8; line-height: 1.6; margin: 0;">
<b style="color: #FFFFFF;">Darshan University</b><br>
Department of Computer Engineering<br>
Semester 5 Machine Learning Project<br>
Student: <b style="color: #A78BFA;">Harsh Kachhetiya</b><br>
Academic Year: 2025–26
</p>
</div>
<div>
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
<div style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #A78BFA 0%, #6D28D9 100%); display: flex; align-items: center; justify-content: center; font-size: 16px; box-shadow: 0 0 12px rgba(124, 58, 237, 0.45);">🫀</div>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; font-family: 'Outfit', sans-serif;">Cardio<span style="color: #A78BFA;">Predict</span></span>
</div>
<p style="font-size: 13px; color: #94A3B8; max-width: 440px; line-height: 1.6; margin: 0 0 12px 0;">
AI-powered heart disease risk assessment platform. Powered exclusively by Random Forest and AdaBoost dual ensemble machine learning architectures.
</p>
<div style="display: inline-flex; gap: 8px; align-items: center; font-size: 12px; color: #A78BFA; font-weight: 600;">
<span>Holdout Accuracy: 73.1%</span> &bull; <span>70,000 Patient Records</span> &bull; <span>5-Fold CV Verified</span>
</div>
</div>
</div>
<div style="border-top: 1px solid #1E1B3A; padding-top: 18px; text-align: center; font-size: 12px; color: #64748B;">
&copy; 2026 CardioPredict &bull; Educational screening demonstrator &bull; Developed by Harsh Kachhetiya under CE Department ML SOP.
</div>
</footer>""", unsafe_allow_html=True)