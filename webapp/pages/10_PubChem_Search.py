import streamlit as st
import requests
from urllib.parse import quote

st.set_page_config(
    page_title="PubChem Drug Search",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 PubChem Drug Search")

st.write("""
Search any drug available in the **PubChem Database**.

Examples:
- Aspirin
- Ibuprofen
- Paracetamol
- Metformin
- Ciprofloxacin
""")

drug = st.text_input(
    "Enter Drug Name",
    value="Aspirin"
)

if st.button("🔍 Search Drug"):

    try:

        drug = drug.strip()

        if not drug:
            st.warning("Please enter a drug name.")
            st.stop()

        url = (
            f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
            f"{quote(drug)}/property/"
            "CID,MolecularFormula,MolecularWeight,"
            "CanonicalSMILES,XLogP,TPSA/JSON"
        )

        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            timeout=20,
        )

        if response.status_code != 200:
            st.error("❌ Drug not found.")
            st.code(response.text)
            st.stop()

        data = response.json()

        if (
            "PropertyTable" not in data
            or "Properties" not in data["PropertyTable"]
            or len(data["PropertyTable"]["Properties"]) == 0
        ):
            st.error("❌ Drug not found.")
            st.json(data)
            st.stop()

        prop = data["PropertyTable"]["Properties"][0]

        cid = prop.get("CID", "N/A")
        formula = prop.get("MolecularFormula", "N/A")
        mw = prop.get("MolecularWeight", "N/A")
        smiles = prop.get("CanonicalSMILES", "")
        xlogp = prop.get("XLogP", "N/A")
        tpsa = prop.get("TPSA", "N/A")

        st.session_state["drug_name"] = drug
        st.session_state["cid"] = cid
        st.session_state["formula"] = formula
        st.session_state["mw"] = mw
        st.session_state["smiles"] = smiles
        st.session_state["xlogp"] = xlogp
        st.session_state["tpsa"] = tpsa

        st.success("✅ Drug Found Successfully")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("CID", cid)
            st.metric("Formula", formula)
            st.metric("Molecular Weight", mw)

        with col2:
            st.metric("XLogP", xlogp)
            st.metric("TPSA", tpsa)
            st.metric("SMILES Length", len(smiles))

        st.divider()

        st.subheader("🧬 Canonical SMILES")
        st.code(smiles)

        st.success(
            "SMILES automatically saved for Molecule Visualizer and Prediction."
        )

    except Exception as e:
        st.error(f"❌ {e}")