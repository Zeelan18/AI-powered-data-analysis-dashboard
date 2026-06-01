import streamlit as st
import numpy as np

def generate_ai_insights(df):

    st.subheader("🤖 AI-Powered Insights")

    insights = []

    # Missing Values
    total_missing = df.isnull().sum().sum()

    if total_missing > 0:
        insights.append(
            f"Dataset contains {total_missing} missing values. "
            f"Data cleaning is recommended."
        )
    else:
        insights.append(
            "Dataset quality is excellent with no missing values."
        )

    # Duplicate Rows
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        insights.append(
            f"{duplicates} duplicate rows detected."
        )

    # Numeric Columns
    numeric_cols = df.select_dtypes(include=np.number).columns

    insights.append(
        f"Detected {len(numeric_cols)} numerical features."
    )

    # Correlation Analysis
    if len(numeric_cols) > 1:

        corr_matrix = df[numeric_cols].corr()

        for i in range(len(corr_matrix.columns)):
            for j in range(i):

                corr_value = corr_matrix.iloc[i, j]

                if abs(corr_value) > 0.75:

                    insights.append(
                        f"Strong relationship between "
                        f"{corr_matrix.columns[i]} and "
                        f"{corr_matrix.columns[j]} "
                        f"(Correlation: {corr_value:.2f})"
                    )

    # Trend Analysis
    for col in numeric_cols:

        mean_value = df[col].mean()

        max_value = df[col].max()

        insights.append(
            f"{col} average is {mean_value:.2f} "
            f"with maximum value {max_value:.2f}."
        )

    # Display Insights
    for insight in insights:
        st.info(insight)