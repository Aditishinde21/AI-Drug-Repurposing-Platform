import streamlit as st
from rdkit import Chem
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
Visualize molecular properties using a SMILES string.

If you searched a drug in **PubChem Search**, its SMILES will appear here automatically.
""")

# -------------------------------------------------
# Get SMILES from PubChem Search
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

        st.success("✅ Molecule Parsed Successfully")

        st.subheader("🧪 Molecular Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Molecular Weight", f"{Descriptors.MolWt(mol):.2f}")
            st.metric("LogP", f"{Descriptors.MolLogP(mol):.2f}")
            st.metric("TPSA", f"{Descriptors.TPSA(mol):.2f}")
            st.metric("H-Bond Donors", Descriptors.NumHDonors(mol))

        with col2:
            st.metric("H-Bond Acceptors", Descriptors.NumHAcceptors(mol))
            st.metric("Rotatable Bonds", Descriptors.NumRotatableBonds(mol))
            st.metric("Ring Count", Descriptors.RingCount(mol))
            st.metric("Heavy Atoms", Descriptors.HeavyAtomCount(mol))

        st.divider()

        st.subheader("🧬 Canonical SMILES")

        st.code(Chem.MolToSmiles(mol), language="text")

        st.divider()

        st.info("""
This deployment uses RDKit to calculate molecular descriptors.

The 2D structure image has been disabled because the Streamlit Cloud RDKit build does not include the drawing backend (`rdMolDraw2D`).
""")