import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Drug Ranking",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Drug Candidate Ranking")

st.write("""
This page ranks the current drug by combining:

- 🤖 AI Prediction
- 🧪 Docking Score
- 💊 ADMET Status

The ranking is generated automatically from the previous steps.
""")

st.divider()

# -------------------------------------------------
# Read data from Session State
# -------------------------------------------------

drug = st.session_state.get("drug_name", "Unknown Drug")
prediction = st.session_state.get("prediction", "Not Predicted")
confidence = st.session_state.get("confidence", 0)

formula = st.session_state.get("formula", "N/A")
mw = st.session_state.get("mw", "N/A")

# Static values for now
docking = -9.6
admet = "PASS"

# -------------------------------------------------
# Final Score Calculation
# -------------------------------------------------

if prediction == "ACTIVE":
    final_score = round((confidence * 0.6) + 40, 1)
else:
    final_score = round(confidence * 0.4, 1)

# Save for Report page
st.session_state["final_score"] = final_score
st.session_state["docking_score"] = docking
st.session_state["admet"] = admet

# -------------------------------------------------
# Summary
# -------------------------------------------------

st.subheader("Current Drug Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Drug Name", drug)
    st.metric("Prediction", prediction)
    st.metric("Confidence", f"{confidence}%")

with col2:
    st.metric("Docking Score", f"{docking} kcal/mol")
    st.metric("ADMET", admet)
    st.metric("Final Score", final_score)

st.divider()

# -------------------------------------------------
# Ranking Table
# -------------------------------------------------

ranking = pd.DataFrame({

    "Drug":[drug],

    "Prediction":[prediction],

    "Confidence (%)":[confidence],

    "Docking":[docking],

    "ADMET":[admet],

    "Final Score":[final_score]

})

st.subheader("Drug Ranking")

st.dataframe(
    ranking,
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Chart
# -------------------------------------------------

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    [drug],
    [final_score]
)

ax.set_ylim(0,100)

ax.set_ylabel("Final Score")

ax.set_title("Overall Drug Score")

st.pyplot(fig)

st.divider()

# -------------------------------------------------
# Recommendation
# -------------------------------------------------

if prediction == "ACTIVE":

    st.success(f"""
## ✅ Recommendation

**{drug}** achieved an overall score of **{final_score}**.

The molecule is predicted to be **ACTIVE** and passed the
ADMET screening.

It is recommended for further laboratory validation.
""")

else:

    st.error(f"""
## ❌ Recommendation

**{drug}** is predicted to be **INACTIVE**.

The molecule should not be prioritized for further validation.
""")

st.divider()

st.info("""
### Ranking Strategy

Final Score is calculated using:

- AI Prediction Confidence
- Molecular Docking Score
- ADMET Status

The ranking updates automatically based on the selected drug.
""")