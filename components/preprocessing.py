import streamlit as st
import numpy as np

def preprocess_data(df):

    st.subheader("🛠 Data Preprocessing")

    missing = df.isnull().sum()

    st.write("Missing Values:")
    st.write(missing)

    numeric_cols = df.select_dtypes(include=np.number).columns

    if st.button("Handle Missing Values"):

        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)

        st.success("Missing values handled successfully!")

    return df