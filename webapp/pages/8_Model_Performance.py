import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Performance")

st.write("""
This page summarizes the performance of the Random Forest classifier
used to predict antimicrobial activity.
""")

st.divider()

# ----------------------------
# Metrics
# ----------------------------

st.header("Model Evaluation")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Training Accuracy", "82.7%")
col2.metric("Test Accuracy", "63.6%")
col3.metric("Precision", "66%")
col4.metric("Recall", "66%")

st.divider()

# ----------------------------
# Classification Report
# ----------------------------

st.header("Classification Report")

st.table({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Value": ["63.6%", "66%", "66%", "64%"]
})

st.divider()

# ----------------------------
# Confusion Matrix
# ----------------------------

st.header("Confusion Matrix")

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS = BASE_DIR / "assets"

image = Image.open(ASSETS / "confusion_matrix.png")

st.image(
    image,
    caption="Confusion Matrix",
    use_container_width=True
)

st.info("""
The confusion matrix summarizes the model's classification performance by
showing correct and incorrect predictions for Active and Inactive molecules.
""")

st.divider()

st.success("""
### Summary

The Random Forest model achieved good predictive performance for
antimicrobial activity classification.

Combined with SHAP, Molecular Docking and ADMET analysis,
the framework provides a comprehensive AI-assisted drug discovery pipeline.
""")