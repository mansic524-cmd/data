import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def basic_info(df):

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.write("### Column Types")
    st.dataframe(df.dtypes.astype(str))


def numerical_analysis(df):

    numeric_cols = df.select_dtypes(include=["number"])

    if len(numeric_cols.columns) > 0:
        st.dataframe(numeric_cols.describe())
    else:
        st.warning("No numerical columns found.")


def categorical_analysis(df):

    categorical_cols = df.select_dtypes(include=["object"])

    if len(categorical_cols.columns) == 0:
        st.warning("No categorical columns found.")
        return

    selected_col = st.selectbox(
        "Select Categorical Column",
        categorical_cols.columns
    )

    st.write(df[selected_col].value_counts())


def create_charts(df):

    numeric_cols = df.select_dtypes(include=["number"]).columns

    if len(numeric_cols) == 0:
        st.warning("No numerical columns available.")
        return

    selected_col = st.selectbox(
        "Select Numerical Column",
        numeric_cols
    )

    fig, ax = plt.subplots()

    ax.hist(df[selected_col].dropna(), bins=10)

    ax.set_title(selected_col)

    st.pyplot(fig)

    st.write("### Correlation Heatmap")

    corr = df[numeric_cols].corr()

    fig2, ax2 = plt.subplots()

    cax = ax2.imshow(corr)

    plt.colorbar(cax)

    ax2.set_xticks(range(len(corr.columns)))
    ax2.set_yticks(range(len(corr.columns)))

    ax2.set_xticklabels(corr.columns, rotation=90)
    ax2.set_yticklabels(corr.columns)

    st.pyplot(fig2)
