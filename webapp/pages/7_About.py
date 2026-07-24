import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="About Project",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    padding-top:2rem;
}

.big-title{
    font-size:52px;
    font-weight:700;
    color:#1f2937;
}

.section-title{
    font-size:34px;
    font-weight:600;
    color:#1f2937;
    margin-top:20px;
}

.card{
    background:#f8fafc;
    padding:22px;
    border-radius:15px;
    border-left:6px solid #2563eb;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
    height:180px;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:35px;
    padding-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown("<div class='big-title'>🧬 AI Drug Repurposing Platform</div>",
            unsafe_allow_html=True)

st.markdown("<div class='section-title'>About the Project</div>",
            unsafe_allow_html=True)

st.write("""

This project presents an **AI-driven Drug Repurposing Framework**
developed to identify promising antimicrobial drug candidates
against **DNA Gyrase**, an important bacterial target involved in
DNA replication.

The platform integrates modern Artificial Intelligence and
Bioinformatics approaches to accelerate drug discovery while reducing
cost and experimental effort.

The complete workflow combines:

- 🤖 Machine Learning
- 🔍 Explainable AI (SHAP)
- 🧪 Molecular Docking
- 💊 ADMET Analysis
- 🏆 AI-based Drug Ranking

to prioritize compounds for future laboratory validation.

""")

st.divider()

# -----------------------------
# Statistics
# -----------------------------
st.markdown("<div class='section-title'>📊 Project Statistics</div>",
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class='card'>

### 📁 Dataset Size

# 602

Drug Molecules

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class='card'>

### 🎯 Target Protein

# DNA Gyrase

MRSA Drug Target

</div>
""", unsafe_allow_html=True)

st.write("")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
<div class='card'>

### 🤖 AI Model

# Random Forest

Machine Learning Classifier

</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class='card'>

### 🧪 Best Docking Score

# -9.6 kcal/mol

Excellent Binding Affinity

</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Workflow
# -----------------------------
st.markdown("<div class='section-title'>🔬 Project Workflow</div>",
            unsafe_allow_html=True)

workflow = """
Drug Dataset

        ↓

Machine Learning Prediction

        ↓

Explainable AI (SHAP)

        ↓

Molecular Docking

        ↓

ADMET Screening

        ↓

Drug Candidate Ranking

        ↓

Top Drug Selection
"""

st.code(workflow)

st.divider()

# -----------------------------
# Technologies
# -----------------------------
st.markdown("<div class='section-title'>🛠 Technologies Used</div>",
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### Programming

• Python

• Streamlit

• Pandas

• NumPy
""")

with col2:
    st.success("""
### Machine Learning

• Scikit-Learn

• Random Forest

• SHAP

• PyTorch Geometric
""")

with col3:
    st.success("""
### Bioinformatics

• RDKit

• Molecular Docking

• DNA Gyrase

• ADMET Analysis
""")

st.divider()

# -----------------------------
# Objectives
# -----------------------------
st.markdown("<div class='section-title'>🎯 Project Objectives</div>",
            unsafe_allow_html=True)

st.info("""

✔ Predict antimicrobial activity using Artificial Intelligence.

✔ Explain model decisions using Explainable AI (SHAP).

✔ Estimate molecular binding using docking analysis.

✔ Evaluate pharmacokinetic properties using ADMET.

✔ Rank candidate molecules for future laboratory validation.

""")

st.divider()

# -----------------------------
# Future Scope
# -----------------------------
st.markdown("<div class='section-title'>🚀 Future Scope</div>",
            unsafe_allow_html=True)

st.write("""

Future improvements may include:

- Deep Learning (Graph Neural Networks)
- Molecular Dynamics Simulation
- Multi-target Drug Repurposing
- Protein Structure Prediction
- Cloud Deployment
- Integration with ChEMBL and DrugBank APIs
- Real-time Molecular Visualization

""")

st.divider()

# -----------------------------
# Developer
# -----------------------------
st.markdown("<div class='section-title'>👩‍💻 Developed By</div>",
            unsafe_allow_html=True)

st.success("""

**Aditi Shinde**

M.Tech Biotechnology

National Institute of Technology Warangal

Project:

**AI Drug Repurposing Platform for Antimicrobial Resistance using Machine Learning, Explainable AI, Molecular Docking and ADMET Analysis**

""")

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class='footer'>

AI Drug Repurposing Platform © 2026

Developed for Academic Research & Demonstration

</div>
""", unsafe_allow_html=True)