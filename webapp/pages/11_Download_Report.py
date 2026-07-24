import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from datetime import datetime

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Download Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Drug Repurposing Report")

st.write("""
Generate a professional report using the results obtained from the platform.
""")

# -------------------------------------------------
# Read values from previous pages
# -------------------------------------------------

drug = st.session_state.get("drug_name", "Unknown Drug")
formula = st.session_state.get("formula", "N/A")
mw = st.session_state.get("mw", "N/A")
prediction = st.session_state.get("prediction", "Not Predicted")
confidence = st.session_state.get("confidence", "N/A")
cid = st.session_state.get("cid", "N/A")

# Static values (replace later with real ones if desired)
docking = "-9.6 kcal/mol"
admet = "PASS"
rank = "1"

# -------------------------------------------------
# Display Summary
# -------------------------------------------------

st.subheader("Drug Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Drug Name", drug)
    st.metric("PubChem CID", cid)
    st.metric("Formula", formula)
    st.metric("Molecular Weight", mw)

with col2:
    st.metric("Prediction", prediction)
    st.metric("Confidence", f"{confidence}%")
    st.metric("Docking", docking)
    st.metric("ADMET", admet)

st.divider()

# -------------------------------------------------
# Generate PDF
# -------------------------------------------------

if st.button("📄 Generate PDF"):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Drug Repurposing Platform</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Drug Name:</b> {drug}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>PubChem CID:</b> {cid}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Molecular Formula:</b> {formula}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Molecular Weight:</b> {mw}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Prediction:</b> {prediction}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Confidence:</b> {confidence}%", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Docking Score:</b> {docking}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>ADMET:</b> {admet}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Drug Rank:</b> {rank}", styles["BodyText"])
    )

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/><br/>", styles["BodyText"])
    )

    story.append(
        Paragraph(
            "This report was automatically generated using the AI Drug Repurposing Platform.",
            styles["Italic"]
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    st.success("✅ PDF Generated Successfully")

    st.download_button(
        "⬇ Download PDF",
        pdf,
        file_name=f"{drug}_Report.pdf",
        mime="application/pdf"
    )