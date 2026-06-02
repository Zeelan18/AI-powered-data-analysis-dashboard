import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def train_ml_model(df):

    st.subheader("🧠 Machine Learning")

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    # VALIDATION
    if len(numeric_cols) < 2:

        st.warning(
            """
            ML requires at least
            2 numeric columns.
            """
        )

        return

    target = st.selectbox(
        "Select Target",
        numeric_cols
    )

    features = [
        col for col in numeric_cols
        if col != target
    ]

    if len(features) == 0:

        st.warning(
            "No feature columns available."
        )

        return

    try:

        X = df[features].fillna(0)
        y = df[target].fillna(0)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = LinearRegression()

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(X_test)

        error = mean_absolute_error(
            y_test,
            predictions
        )

        st.success(
            "ML Model Trained Successfully!"
        )

        st.metric(
            "Mean Absolute Error",
            round(error, 2)
        )

        prediction_df = pd.DataFrame({
            "Actual": y_test.values,
            "Predicted": predictions
        })

        st.dataframe(
            prediction_df,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"ML Error: {e}")