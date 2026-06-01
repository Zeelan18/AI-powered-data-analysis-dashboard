import streamlit as st
import pandas as pd

def upload_dataset():

    st.sidebar.markdown("""
    # 🚀 AI Analytics Dashboard

    ### Features
    - 📊 Visual Analytics
    - 🤖 AI Insights
    - 🧠 Machine Learning
    - 📑 PDF Reports
    - 🔥 Correlation Analysis
    """)

    st.sidebar.divider()

    uploaded_file = st.sidebar.file_uploader(
        "📂 Upload CSV Dataset",
        type=["csv"]
    )

    st.sidebar.divider()

    st.sidebar.info(
        "Built using Python, Streamlit, AI, and Machine Learning."
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.sidebar.success(
            "Dataset Loaded Successfully!"
        )

        return df

    return None