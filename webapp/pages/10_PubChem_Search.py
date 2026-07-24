import streamlit as st
import pubchempy as pcp

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="PubChem Drug Search",
    page_icon="🌐",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
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

# --------------------------------------------------
# Drug Input
# --------------------------------------------------
drug_name = st.text_input(
    "Enter Drug Name",
    value="Aspirin"
)

# --------------------------------------------------
# Search Button
# --------------------------------------------------
if st.button("🔍 Search Drug"):

    try:

        compounds = pcp.get_compounds(drug_name, "name")

        if not compounds:
            st.error("❌ Drug not found.")

        else:

            compound = compounds[0]

            # --------------------------------------------------
            # Get SMILES safely
            # --------------------------------------------------
            smiles = None

            try:
                smiles = compound.canonical_smiles
            except:
                pass

            if not smiles:
                try:
                    smiles = compound.isomeric_smiles
                except:
                    pass

            # --------------------------------------------------
            # Save into Session State
            # --------------------------------------------------
            st.session_state["drug_name"] = drug_name
            st.session_state["smiles"] = smiles
            st.session_state["formula"] = compound.molecular_formula
            st.session_state["mw"] = compound.molecular_weight
            st.session_state["cid"] = compound.cid
            st.session_state["xlogp"] = compound.xlogp
            st.session_state["tpsa"] = compound.tpsa

            # --------------------------------------------------
            # Display Results
            # --------------------------------------------------

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
                    "SMILES",
                    smiles if smiles else "Not Available"
                )

                st.metric(
                    "XLogP",
                    compound.xlogp if compound.xlogp is not None else "N/A"
                )

                st.metric(
                    "TPSA",
                    compound.tpsa if compound.tpsa is not None else "N/A"
                )

            st.divider()

            st.subheader("🧬 Canonical SMILES")

            if smiles:

                st.code(smiles)

                st.success("✅ SMILES saved successfully for other pages.")

            else:

                st.error("❌ PubChem did not return a SMILES string for this compound.")

            st.info("""
The SMILES string has been saved automatically.

You can now directly open:

• Molecule Visualizer
• Prediction

without copying anything.
""")

    except Exception as e:

        st.error(f"❌ Error: {e}")