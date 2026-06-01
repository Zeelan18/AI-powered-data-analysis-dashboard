import streamlit as st

def show_statistics(df):

    st.subheader("📈 Dataset Overview")

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    missing_values = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        label="📄 Rows",
        value=total_rows
    )

    col2.metric(
        label="📊 Columns",
        value=total_columns
    )

    col3.metric(
        label="⚠ Missing Values",
        value=missing_values
    )

    col4.metric(
        label="🧬 Duplicate Rows",
        value=duplicates
    )

    st.subheader("📋 Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )