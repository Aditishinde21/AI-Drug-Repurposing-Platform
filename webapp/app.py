import streamlit as st

st.set_page_config(
    page_title="AI Drug Repurposing Platform",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.hero{
background:linear-gradient(90deg,#0f172a,#1e3a8a,#2563eb);
padding:35px;
border-radius:18px;
color:white;
}

.card{
background:#f8fafc;
padding:20px;
border-radius:15px;
border-left:6px solid #2563eb;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
height:220px;
}

.footer{
text-align:center;
color:gray;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class='hero'>

# 🧬 AI Drug Repurposing Platform

### Artificial Intelligence Assisted Drug Discovery Against Antimicrobial Resistance

Machine Learning • Explainable AI • Molecular Docking • ADMET • Drug Ranking

</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Overview
# -----------------------------
st.header("📖 Project Overview")

st.write("""
This platform integrates Artificial Intelligence and Bioinformatics
to identify promising drug candidates against antimicrobial resistance.

The workflow combines machine learning prediction,
Explainable AI (SHAP), molecular docking,
ADMET analysis and final drug ranking.
""")

st.divider()

# -----------------------------
# Statistics
# -----------------------------
st.header("📊 Platform Statistics")

c1,c2,c3,c4=st.columns(4)

c1.metric("Dataset","602 Drugs")
c2.metric("AI Model","Random Forest")
c3.metric("Target","DNA Gyrase")
c4.metric("Best Docking","-9.6")

st.divider()

# -----------------------------
# Workflow
# -----------------------------
st.header("🔬 Workflow")

st.code("""
Drug Search

↓

Molecule Visualization

↓

Machine Learning Prediction

↓

Explainable AI

↓

Molecular Docking

↓

ADMET Analysis

↓

Drug Ranking

↓

PDF Report
""")

st.divider()

# -----------------------------
# Feature Cards
# -----------------------------
st.header("🚀 Platform Features")

col1,col2,col3=st.columns(3)

with col1:
    st.info("""
### 🤖 AI Prediction

Predict antimicrobial activity using Machine Learning.
""")

    st.info("""
### 🔍 Explainability

Interpret predictions using SHAP values.
""")

with col2:
    st.info("""
### 🧪 Docking

Evaluate binding affinity with DNA Gyrase.
""")

    st.info("""
### 💊 ADMET

Assess drug-likeness and pharmacokinetics.
""")

with col3:
    st.info("""
### 🌐 PubChem Search

Retrieve molecular information directly from PubChem.
""")

    st.info("""
### 📄 PDF Report

Generate downloadable drug analysis reports.
""")

st.divider()

# -----------------------------
# Top Candidate
# -----------------------------
st.header("🏆 Best Drug Candidate")

st.success("""
**CHEMBL187677**

Prediction: Active

Docking Score: -9.6 kcal/mol

ADMET: Pass

Final Rank: 1
""")

st.divider()

# -----------------------------
# Developer
# -----------------------------
st.header("👩‍💻 Developer")

st.write("""
**Aditi Shinde**

M.Tech Biotechnology

National Institute of Technology Warangal
""")

st.divider()

st.markdown("""
<div class='footer'>

AI Drug Repurposing Platform © 2026

Developed for Academic Research

</div>
""", unsafe_allow_html=True)