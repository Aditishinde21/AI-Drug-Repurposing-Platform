import streamlit as st
import requests

st.set_page_config(
    page_title="PubChem Drug Search",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 PubChem Drug Search")

st.write("""
Search any drug available in the **PubChem Database**.

Examples

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

        url = (
            "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
            f"{drug}/property/"
            "CID,MolecularFormula,MolecularWeight,CanonicalSMILES,"
            "XLogP,TPSA/JSON"
        )

        response = requests.get(url, timeout=20)

        if response.status_code != 200:
            st.error("Drug not found.")
            st.stop()

        data = response.json()

        prop = data["PropertyTable"]["Properties"][0]

        cid = prop.get("CID")
        formula = prop.get("MolecularFormula")
        mw = prop.get("MolecularWeight")
        smiles = prop.get("CanonicalSMILES")
        xlogp = prop.get("XLogP")
        tpsa = prop.get("TPSA")

        st.session_state["drug_name"] = drug
        st.session_state["cid"] = cid
        st.session_state["formula"] = formula
        st.session_state["mw"] = mw
        st.session_state["smiles"] = smiles
        st.session_state["xlogp"] = xlogp
        st.session_state["tpsa"] = tpsa

        st.success("Drug Found Successfully")

        c1, c2 = st.columns(2)

        with c1:

            st.metric("CID", cid)
            st.metric("Formula", formula)
            st.metric("Molecular Weight", mw)

        with c2:

            st.metric("XLogP", xlogp)
            st.metric("TPSA", tpsa)
            st.metric("SMILES Length", len(smiles))

        st.divider()

        st.subheader("Canonical SMILES")

        st.code(smiles)

        st.success("SMILES automatically saved for Molecule Visualizer and Prediction.")

    except Exception as e:

        st.error(str(e))