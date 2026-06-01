import streamlit as st
import pandas as pd
import numpy as np

def analyze_data_quality(df):

    st.subheader("🛡 Data Quality Analysis")

    # Missing Values
    missing_values = df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing_values.index,
        "Missing Values": missing_values.values,
        "Missing Percentage":
            (missing_values.values / len(df)) * 100
    })

    st.write("### Missing Value Analysis")
    st.dataframe(missing_df)

    # Duplicate Rows
    duplicates = df.duplicated().sum()

    st.warning(f"Duplicate Rows Detected: {duplicates}")

    # Outlier Detection
    st.write("### Outlier Detection")

    numeric_cols = df.select_dtypes(include=np.number).columns

    outlier_summary = []

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[col] < lower_bound) |
            (df[col] > upper_bound)
        ]

        outlier_summary.append({
            "Column": col,
            "Outliers": len(outliers)
        })

    outlier_df = pd.DataFrame(outlier_summary)

    st.dataframe(outlier_df)

    # Skewness
    st.write("### Feature Skewness")

    skewness = df[numeric_cols].skew()

    skew_df = pd.DataFrame({
        "Feature": skewness.index,
        "Skewness": skewness.values
    })

    st.dataframe(skew_df)