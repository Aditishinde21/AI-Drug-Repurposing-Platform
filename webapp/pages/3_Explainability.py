import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Explainability",
    page_icon="📊"
)

st.title("📊 Explainable AI (SHAP)")

st.write("""
This page explains **why** the AI predicted a molecule as Active or Inactive.

SHAP (SHapley Additive exPlanations) measures the contribution of each molecular descriptor to the prediction.
""")

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS = BASE_DIR / "assets"

# -------------------------------
# SHAP Summary Plot
# -------------------------------

st.header("Global Feature Importance")

summary = Image.open(ASSETS / "shap_summary_plot.png")

st.image(
    summary,
    caption="SHAP Summary Plot",
    use_container_width=True
)

st.info("""
The SHAP summary plot ranks molecular descriptors according to their overall influence on predictions.

Features near the top have the greatest impact on identifying antimicrobial activity.
""")

st.divider()

# -------------------------------
# Waterfall Plot
# -------------------------------

st.header("Individual Molecule Explanation")

waterfall = Image.open(
    ASSETS / "molecule_explanation.png"
)

st.image(
    waterfall,
    caption="SHAP Waterfall Plot",
    use_container_width=True
)

st.success("""
This plot explains how each descriptor pushes the prediction toward either
an Active or Inactive classification.
""")