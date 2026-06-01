import streamlit as st
import pandas as pd
import os

from dotenv import load_dotenv
from openai import OpenAI

# Load Environment Variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_gemini_insights(df):

    st.subheader("✨ AI Analytics Assistant")

    # Dataset Summary
    summary = df.describe().to_string()

    prompt = f"""
    You are an expert AI Data Analyst.

    Analyze this dataset summary and provide:

    1. Key trends
    2. Business insights
    3. Data quality observations
    4. Recommendations
    5. Important feature relationships

    Dataset Summary:
    {summary}
    """

    if st.button("Generate AI Analysis"):

        with st.spinner("AI is analyzing dataset..."):

            try:

                completion = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                result = completion.choices[0].message.content

                st.success(
                    "AI Analysis Generated Successfully!"
                )

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")