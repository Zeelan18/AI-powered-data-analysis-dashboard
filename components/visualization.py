import streamlit as st
import plotly.express as px
import numpy as np

def show_visualizations(df):

    st.subheader("📊 Advanced Visualizations")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) > 0:

        chart_type = st.selectbox(
            "Select Visualization Type",
            [
                "Histogram",
                "Box Plot",
                "Scatter Plot",
                "Line Chart",
                "Bar Chart",
                "Pie Chart"
            ]
        )

        # Histogram
        if chart_type == "Histogram":

            selected_col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.histogram(
                df,
                x=selected_col,
                template="plotly_dark",
                title=f"{selected_col} Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Box Plot
        elif chart_type == "Box Plot":

            selected_col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.box(
                df,
                y=selected_col,
                template="plotly_dark",
                title=f"{selected_col} Box Plot"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Scatter Plot
        elif chart_type == "Scatter Plot":

            x_axis = st.selectbox("X Axis", numeric_cols)
            y_axis = st.selectbox("Y Axis", numeric_cols)

            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                template="plotly_dark",
                title=f"{x_axis} vs {y_axis}"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Line Chart
        elif chart_type == "Line Chart":

            selected_col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.line(
                df,
                y=selected_col,
                template="plotly_dark",
                title=f"{selected_col} Trend"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Bar Chart
        elif chart_type == "Bar Chart":

            selected_col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            fig = px.bar(
                df,
                y=selected_col,
                template="plotly_dark",
                title=f"{selected_col} Bar Analysis"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Pie Chart
        elif chart_type == "Pie Chart":

            selected_col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            pie_df = df[selected_col].value_counts().reset_index()

            pie_df.columns = ["Category", "Count"]

            fig = px.pie(
                pie_df,
                names="Category",
                values="Count",
                template="plotly_dark",
                title=f"{selected_col} Pie Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

    # Correlation Heatmap
    if len(numeric_cols) > 1:

        st.subheader("🔥 Correlation Heatmap")

        corr = df[numeric_cols].corr()

        heatmap = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Feature Correlation Matrix"
        )

        st.plotly_chart(heatmap, use_container_width=True)