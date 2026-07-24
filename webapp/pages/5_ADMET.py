import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ADMET Analysis",
    page_icon="💊",
    layout="wide"
)

st.title("💊 ADMET Analysis")

st.markdown("""
ADMET stands for:

- **A**bsorption
- **D**istribution
- **M**etabolism
- **E**xcretion
- **T**oxicity

Drug candidates with good ADMET properties are more likely to become successful medicines.
""")

st.divider()

st.header("Drug-Likeness Evaluation")

admet = pd.DataFrame({

"Property":[
"Molecular Weight",
"LogP",
"H Bond Donors",
"H Bond Acceptors",
"TPSA",
"Lipinski Rule"
],

"Observed":[
431.3,
2.87,
4,
5,
124.2,
"Pass"
],

"Recommended":[
"<500",
"<5",
"≤5",
"≤10",
"<140",
"Pass"
]

})

st.dataframe(admet,use_container_width=True)

st.divider()

st.header("ADMET Summary")

col1,col2,col3,col4=st.columns(4)

col1.metric("Absorption","Good")
col2.metric("Distribution","Good")
col3.metric("Metabolism","Acceptable")
col4.metric("Toxicity","Low")

st.divider()

st.success("""

### Overall Assessment

✅ Lipinski Rule Passed

✅ Drug-Like Molecule

✅ Suitable for Further Validation

The molecule demonstrates favorable physicochemical properties and
is a promising antimicrobial drug candidate.

""")