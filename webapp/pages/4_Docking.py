import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Docking", page_icon="🧬", layout="wide")

st.title("🧬 Molecular Docking Analysis")

st.markdown("""
This page presents the molecular docking results of the top predicted compounds
against the **DNA Gyrase** protein target.

Docking estimates how strongly a drug molecule binds to the target protein.

Lower (more negative) docking scores indicate stronger predicted binding affinity.
""")

st.divider()

# ----------------------------
# Docking Results
# ----------------------------

docking_results = pd.DataFrame({

    "Compound":[
        "CHEMBL187677",
        "CHEMBL371124",
        "CHEMBL220655",
        "CHEMBL435612",
        "CHEMBL219534"
    ],

    "Docking Score (kcal/mol)":[
        -9.6,
        -8.9,
        -8.5,
        -7.8,
        -7.2
    ],

    "Binding Strength":[
        "Excellent",
        "Very Strong",
        "Strong",
        "Moderate",
        "Moderate"
    ]

})

st.subheader("Docking Results Table")

st.dataframe(
    docking_results,
    use_container_width=True
)

st.divider()

# ----------------------------
# Bar Chart
# ----------------------------

st.subheader("Docking Score Comparison")

fig, ax = plt.subplots(figsize=(9,5))

ax.bar(
    docking_results["Compound"],
    docking_results["Docking Score (kcal/mol)"]
)

ax.set_xlabel("Compounds")
ax.set_ylabel("Docking Score (kcal/mol)")
ax.set_title("DNA Gyrase Docking Scores")

plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

# ----------------------------
# Best Compound
# ----------------------------

best = docking_results.sort_values(
    by="Docking Score (kcal/mol)"
).iloc[0]

st.success(f"""

### 🏆 Best Candidate

**Compound:** {best['Compound']}

**Docking Score:** {best['Docking Score (kcal/mol)']} kcal/mol

**Binding Strength:** {best['Binding Strength']}

This compound demonstrated the strongest predicted interaction with the DNA Gyrase protein and is considered the best docking candidate among the screened molecules.

""")

st.divider()

# ----------------------------
# Interpretation
# ----------------------------

st.subheader("Interpretation")

st.info("""

### Interpretation of Docking Scores

- Docking predicts how well a molecule fits into the protein binding pocket.

- Lower (more negative) docking scores indicate stronger predicted binding.

- Scores below **-8 kcal/mol** generally indicate good binding affinity.

- Docking is a computational prediction and should be validated experimentally.

""")

st.divider()

# ----------------------------
# Conclusion
# ----------------------------

st.success("""

### Conclusion

The molecular docking analysis identified several promising compounds with high predicted affinity toward the DNA Gyrase target.

These candidates can be prioritized for further:

- In vitro validation
- ADMET analysis
- Molecular dynamics simulation
- Experimental antimicrobial testing

""")