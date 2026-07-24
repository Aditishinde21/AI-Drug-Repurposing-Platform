import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Drug Activity Prediction")

st.write("""
This page predicts whether the selected molecule is **Active** or **Inactive**.

If you searched a drug in **PubChem Search**, the molecular descriptors
are calculated automatically.
""")

# -------------------------------------------------
# Load Model
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
model_path = BASE_DIR / "models" / "random_forest_model.pkl"

model = joblib.load(model_path)

# -------------------------------------------------
# Read SMILES from PubChem Search
# -------------------------------------------------
smiles = st.session_state.get("smiles", "")

if smiles:

    mol = Chem.MolFromSmiles(smiles)

    if mol:

        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = rdMolDescriptors.CalcNumHBD(mol)
        hba = rdMolDescriptors.CalcNumHBA(mol)
        tpsa = rdMolDescriptors.CalcTPSA(mol)
        rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
        rings = rdMolDescriptors.CalcNumRings(mol)
        aromatic = rdMolDescriptors.CalcNumAromaticRings(mol)

    else:

        mw = 350
        logp = 2.5
        hbd = 2
        hba = 5
        tpsa = 90
        rot = 4
        rings = 3
        aromatic = 2

else:

    mw = 350
    logp = 2.5
    hbd = 2
    hba = 5
    tpsa = 90
    rot = 4
    rings = 3
    aromatic = 2

# -------------------------------------------------
# Save descriptors for Report Page
# -------------------------------------------------
st.session_state["mw"] = round(mw, 2)
st.session_state["logp"] = round(logp, 2)
st.session_state["tpsa"] = round(tpsa, 2)

# -------------------------------------------------
# Show Molecular Descriptors
# -------------------------------------------------
st.subheader("📊 Calculated Molecular Descriptors")

col1, col2 = st.columns(2)

with col1:
    st.metric("Molecular Weight", f"{mw:.2f}")
    st.metric("LogP", f"{logp:.2f}")
    st.metric("H-Bond Donors", hbd)
    st.metric("H-Bond Acceptors", hba)

with col2:
    st.metric("TPSA", f"{tpsa:.2f}")
    st.metric("Rotatable Bonds", rot)
    st.metric("Ring Count", rings)
    st.metric("Aromatic Rings", aromatic)

st.divider()

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("🚀 Predict Drug Activity"):

    X = pd.DataFrame([[
        mw,
        logp,
        hbd,
        hba,
        tpsa,
        rot,
        rings,
        aromatic
    ]],
    columns=[
        "MolecularWeight",
        "LogP",
        "HBD",
        "HBA",
        "TPSA",
        "RotatableBonds",
        "RingCount",
        "AromaticRings"
    ])

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0]

    confidence = np.max(probability) * 100

    # -----------------------------------------
    # Save results for other pages
    # -----------------------------------------
    st.session_state["prediction"] = (
        "ACTIVE" if prediction == 1 else "INACTIVE"
    )

    st.session_state["confidence"] = round(confidence, 2)

    st.session_state["probability"] = probability.tolist()

    # -----------------------------------------

    if prediction == 1:
        st.success("✅ Predicted ACTIVE Molecule")
    else:
        st.error("❌ Predicted INACTIVE Molecule")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.subheader("Prediction Probability")

    chart = pd.DataFrame(
        {
            "Probability": probability
        },
        index=["Inactive", "Active"]
    )

    st.bar_chart(chart)

    st.success("""
Prediction has been saved.

The Download Report page will automatically use these values.
""")