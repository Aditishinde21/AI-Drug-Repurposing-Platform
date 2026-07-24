import streamlit as st
import pubchempy as pcp

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="PubChem Drug Search",
    page_icon="🌐",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌐 PubChem Drug Search")

st.write("""
Search any drug available in the **PubChem Database**.

Examples:
- Aspirin
- Paracetamol
- Ibuprofen
- Ciprofloxacin
- Metformin
""")

# -----------------------------
# Drug Input
# -----------------------------
drug_name = st.text_input(
    "Enter Drug Name",
    "Aspirin"
)

# -----------------------------
# Search Button
# -----------------------------
if st.button("🔍 Search Drug"):

    try:

        compounds = pcp.get_compounds(drug_name, "name")

        if len(compounds) == 0:
            st.error("❌ Drug not found.")

        else:

            compound = compounds[0]

            # ====================================================
            # Save values so other pages can use them automatically
            # ====================================================

            st.session_state["drug_name"] = drug_name
            st.session_state["smiles"] = compound.canonical_smiles
            st.session_state["formula"] = compound.molecular_formula
            st.session_state["mw"] = compound.molecular_weight
            st.session_state["cid"] = compound.cid
            st.session_state["xlogp"] = compound.xlogp
            st.session_state["tpsa"] = compound.tpsa

            # ====================================================

            st.success("✅ Drug Found Successfully")

            st.header("📋 Basic Information")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "PubChem CID",
                    compound.cid
                )

                st.metric(
                    "Molecular Formula",
                    compound.molecular_formula
                )

                st.metric(
                    "Molecular Weight",
                    compound.molecular_weight
                )

            with col2:

                st.metric(
                    "Canonical SMILES",
                    compound.canonical_smiles
                )

                st.metric(
                    "XLogP",
                    compound.xlogp if compound.xlogp else "N/A"
                )

                st.metric(
                    "TPSA",
                    compound.tpsa if compound.tpsa else "N/A"
                )

            st.divider()

            st.subheader("🧬 Canonical SMILES")

            st.code(compound.canonical_smiles)

            st.info("""
Copy this SMILES into the Molecule Visualizer.

In the next step, we'll make this happen automatically.
""")

    except Exception as e:

        st.error(f"❌ Error: {e}")