import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Dataset", page_icon="🧬")

st.title("🧬 Dataset Overview")

st.markdown(
"""
This page displays the dataset used for training the AI model for
drug repurposing against antimicrobial resistance.
"""
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed/gyrase_activity_dataset.csv")

# -----------------------------
# Dataset Summary
# -----------------------------
st.header("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Molecules", len(df))

with col2:
    st.metric("Target", "DNA Gyrase")

with col3:
    st.metric("Source", "ChEMBL")

st.divider()

# -----------------------------
# Activity Distribution
# -----------------------------
st.header("Activity Distribution")

activity_counts = df["Activity"].value_counts()

st.bar_chart(activity_counts)

col1, col2 = st.columns(2)

with col1:
    st.metric("Active Molecules",
              activity_counts.get("Active", 0))

with col2:
    st.metric("Inactive Molecules",
              activity_counts.get("Inactive", 0))

st.divider()

# -----------------------------
# Dataset Preview
# -----------------------------
st.header("Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.divider()

# -----------------------------
# Search Molecule
# -----------------------------
st.header("Search Molecule")

search = st.text_input(
    "Enter CHEMBL ID",
    placeholder="CHEMBL3094348"
)

if search:

    result = df[
        df["molecule_chembl_id"]
        .str.contains(search, case=False)
    ]

    if len(result) > 0:
        st.success(f"{len(result)} molecule found")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No molecule found.")

st.divider()

# -----------------------------
# Download Dataset
# -----------------------------
st.header("Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Dataset",
    data=csv,
    file_name="AMR_Dataset.csv",
    mime="text/csv"
)