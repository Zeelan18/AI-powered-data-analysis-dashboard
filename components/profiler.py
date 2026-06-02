import streamlit as st

def show_profile(df):

    st.subheader("📑 Dataset Profile")

    st.write("### Data Types")

    st.dataframe(df.dtypes.astype(str))

    st.write("### Unique Values")

    unique_df = df.nunique().reset_index()

    unique_df.columns = ["Column", "Unique Values"]

    st.dataframe(unique_df)

    st.write("### Dataset Shape")

    st.success(
        f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
    )


