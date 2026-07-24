import streamlit as st
import pubchempy as pcp

st.set_page_config(
    page_title="PubChem Drug Search",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 PubChem Drug Search")

st.write("""
Search any drug from the PubChem database.
""")

drug = st.text_input(
    "Enter Drug Name",
    value="Aspirin"
)

if st.button("🔍 Search"):

    try:

        compounds = pcp.get_compounds(drug, "name")

        if not compounds:
            st.error("Drug not found.")
            st.stop()

        compound = compounds[0]

        st.success("Drug Found Successfully")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("CID", compound.cid)
            st.metric("Formula", compound.molecular_formula)
            st.metric("Molecular Weight", compound.molecular_weight)

        with col2:
            st.metric("XLogP", compound.xlogp if compound.xlogp else "N/A")
            st.metric("TPSA", compound.tpsa if compound.tpsa else "N/A")

        st.info("Drug information retrieved successfully from PubChem.")

    except Exception as e:

        st.error(e)