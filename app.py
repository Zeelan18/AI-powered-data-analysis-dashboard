import streamlit as st
import pandas as pd

from components.uploader import upload_dataset
from components.statistics import show_statistics
from components.preprocessing import preprocess_data
from components.visualization import show_visualizations
from components.insights import generate_ai_insights
from components.data_quality import analyze_data_quality
from components.profiler import show_profile
from components.exporter import export_dataset
from components.ml_model import train_ml_model
from components.gemini_ai import generate_gemini_insights
from components.report_generator import generate_pdf_report

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Page Configuration
st.set_page_config(
    page_title="AI Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Main Title
st.markdown("""
# 📊 AI-Powered Data Analysis Dashboard

### Intelligent Analytics Platform for Real-World Data Insights

Transform raw datasets into:
- 📈 Advanced visual analytics
- 🤖 AI-powered recommendations
- 🔥 Correlation intelligence
- 🧠 Machine learning predictions
- 📑 Automated reporting
""")

st.markdown("""
Welcome to the intelligent analytics dashboard.

Upload a CSV dataset to:
- Analyze statistics
- Handle missing values
- Generate visualizations
- Detect correlations
- Produce AI-generated insights
""")

# Upload Dataset
df = upload_dataset()

if df is not None:

    with st.spinner("Processing dataset..."):

      st.success("Dataset uploaded successfully!")

    # Dashboard Tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📁 Overview",
    "📊 Visualizations",
    "🛡 Data Quality",
    "🤖 AI Insights",
    "🧠 Machine Learning",
    "⬇ Export",
    "✨ AI Assistant"
])

    # TAB 1
    with tab1:

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        show_statistics(df)

        show_profile(df)

    # TAB 2
    with tab2:

        show_visualizations(df)

    # TAB 3
    with tab3:

        analyze_data_quality(df)

    # TAB 4
    with tab4:

        generate_ai_insights(df)

    # TAB 5
    with tab5:

        train_ml_model(df)

    # TAB 6
    with tab6:

        export_dataset(df)
        generate_pdf_report(df)
    with tab7:

        generate_gemini_insights(df)

else:

    st.info("Upload a CSV dataset to begin analysis.")
st.markdown("---")

st.markdown(
    """
    <center>
    Built with ❤️ using Streamlit, AI, Machine Learning, and Data Analytics
    </center>
    """,
    unsafe_allow_html=True
)