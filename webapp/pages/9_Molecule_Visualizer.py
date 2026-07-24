import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Molecule Visualizer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Molecule Structure Visualizer")

st.write("""
Visualize the molecular structure using a SMILES string.

If you searched a drug in **PubChem Search**, its SMILES will appear here automatically.
""")

# -------------------------------------------------
# Get SMILES from PubChem Search (if available)
# -------------------------------------------------

default_smiles = st.session_state.get(
    "smiles",
    "CC(=O)OC1=CC=CC=C1C(=O)O"
)

smiles = st.text_input(
    "Enter SMILES",
    value=default_smiles
)

# -------------------------------------------------
# Visualize
# -------------------------------------------------

if st.button("Visualize Molecule"):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        st.error("❌ Invalid SMILES string.")

    else:

        st.success("✅ Molecule Generated Successfully")

        img = Draw.MolToImage(mol, size=(500, 500))

        st.image(
            img,
            caption="2D Molecular Structure"
        )

        st.divider()

        st.subheader("📊 Molecular Properties")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Molecular Weight",
                f"{Descriptors.MolWt(mol):.2f}"
            )

            st.metric(
                "LogP",
                f"{Descriptors.MolLogP(mol):.2f}"
            )

            st.metric(
                "TPSA",
                f"{Descriptors.TPSA(mol):.2f}"
            )

        with col2:

            st.metric(
                "H-Bond Donors",
                Descriptors.NumHDonors(mol)
            )

            st.metric(
                "H-Bond Acceptors",
                Descriptors.NumHAcceptors(mol)
            )

            st.metric(
                "Rotatable Bonds",
                Descriptors.NumRotatableBonds(mol)
            )

        st.divider()

        st.info("""
RDKit was used to generate the molecular structure and calculate the molecular descriptors.
""")