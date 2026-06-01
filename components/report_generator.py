import streamlit as st
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df):

    st.subheader("📑 Generate Analytics Report")

    if st.button("Generate PDF Report"):

        report_path = "analytics_report.pdf"

        doc = SimpleDocTemplate(report_path)

        styles = getSampleStyleSheet()

        elements = []

        # Title
        title = Paragraph(
            "AI-Powered Data Analytics Report",
            styles['Title']
        )

        elements.append(title)

        elements.append(Spacer(1, 20))

        # Dataset Shape
        shape_text = Paragraph(
            f"""
            <b>Dataset Shape:</b>
            Rows: {df.shape[0]}
            Columns: {df.shape[1]}
            """,
            styles['BodyText']
        )

        elements.append(shape_text)

        elements.append(Spacer(1, 12))

        # Missing Values
        missing_values = df.isnull().sum().sum()

        missing_text = Paragraph(
            f"""
            <b>Total Missing Values:</b>
            {missing_values}
            """,
            styles['BodyText']
        )

        elements.append(missing_text)

        elements.append(Spacer(1, 12))

        # Statistical Summary
        summary = df.describe().to_string()

        summary_text = Paragraph(
            f"""
            <b>Statistical Summary:</b><br/>
            <pre>{summary}</pre>
            """,
            styles['Code']
        )

        elements.append(summary_text)

        elements.append(Spacer(1, 12))

        # Build PDF
        doc.build(elements)

        st.success("PDF Report Generated Successfully!")

        # Download Button
        with open(report_path, "rb") as file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=file,
                file_name="analytics_report.pdf",
                mime="application/pdf"
            )