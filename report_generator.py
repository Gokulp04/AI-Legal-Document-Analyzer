from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(summary):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/AI_Legal_Report.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Legal Document Analysis Report</b>", styles["Heading1"]))
    story.append(Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return filename