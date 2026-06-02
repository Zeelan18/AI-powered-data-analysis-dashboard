import streamlit as st
import pandas as pd

def upload_dataset():

    st.sidebar.markdown("""
    # 🚀 AI Analytics Dashboard

    Upload ANY CSV dataset for:
    - Visual Analytics
    - AI Insights
    - ML Predictions
    - PDF Reports
    """)

    uploaded_file = st.sidebar.file_uploader(
        "📂 Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            # Try multiple encodings
            try:
                df = pd.read_csv(uploaded_file)

            except:
                uploaded_file.seek(0)
                df = pd.read_csv(
                    uploaded_file,
                    encoding='latin1'
                )

            # Remove fully empty rows/columns
            df.dropna(
                how='all',
                inplace=True
            )

            df.dropna(
                axis=1,
                how='all',
                inplace=True
            )

            st.sidebar.success(
                "Dataset Loaded Successfully!"
            )

            return df

        except Exception as e:

            st.sidebar.error(
                f"CSV Error: {e}"
            )

            return None

    return None