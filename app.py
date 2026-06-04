import streamlit as st
import pandas as pd
from analysis import (
    basic_info,
    numerical_analysis,
    categorical_analysis,
    create_charts
)

st.set_page_config(
    page_title="Finance Data Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Finance Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Basic Information")
    basic_info(df)

    st.subheader("Numerical Analysis")
    numerical_analysis(df)

    st.subheader("Categorical Analysis")
    categorical_analysis(df)

    st.subheader("Visualizations")
    create_charts(df)

else:
    st.info("Upload a CSV file to begin analysis.")
