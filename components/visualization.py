import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def show_visualizations(df):

    st.subheader("📊 Visual Analytics")

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=['object']
    ).columns.tolist()

    # NO NUMERIC DATA
    if len(numeric_cols) == 0:

        st.warning(
            "No numeric columns available."
        )

    else:

        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Histogram",
                "Box Plot",
                "Scatter Plot",
                "Line Chart"
            ]
        )

        if chart_type == "Histogram":

            col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.histogram(
                df,
                x=col,
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif chart_type == "Box Plot":

            col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.box(
                df,
                y=col,
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif chart_type == "Scatter Plot":

            if len(numeric_cols) >= 2:

                x_col = st.selectbox(
                    "X Axis",
                    numeric_cols
                )

                y_col = st.selectbox(
                    "Y Axis",
                    numeric_cols
                )

                fig = px.scatter(
                    df,
                    x=x_col,
                    y=y_col,
                    template="plotly_dark"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Need at least 2 numeric columns."
                )

        elif chart_type == "Line Chart":

            col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.line(
                df,
                y=col,
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # CATEGORICAL ANALYSIS
    if len(categorical_cols) > 0:

        st.subheader("📌 Categorical Analysis")

        cat_col = st.selectbox(
            "Select Category Column",
            categorical_cols
        )

        cat_counts = (
            df[cat_col]
            .value_counts()
            .reset_index()
        )

        cat_counts.columns = [
            "Category",
            "Count"
        ]

        fig = px.bar(
            cat_counts,
            x="Category",
            y="Count",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # CORRELATION
    if len(numeric_cols) >= 2:

        st.subheader("🔥 Correlation Heatmap")

        corr = df[numeric_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )