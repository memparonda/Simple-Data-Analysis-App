import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Simple Data Analysis App", layout="wide")

# Title
st.title("📊 Simple Data Analysis App")
st.write("Upload a CSV file to begin analyzing your data.")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Dataset information
    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Column selection
    st.subheader("Select Columns")
    selected_columns = st.multiselect(
        "Choose columns to display",
        df.columns,
        default=df.columns.tolist()
    )

    filtered_df = df[selected_columns]
    st.dataframe(filtered_df)

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Statistics
    st.subheader("Statistical Summary")
    st.write(df.describe())

    # Chart section
    st.subheader("Data Visualization")

    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_columns) > 0:
        x_axis = st.selectbox("Select X-axis", numeric_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns)

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line Chart", "Bar Chart", "Scatter Plot"]
        )

        fig, ax = plt.subplots()

        if chart_type == "Line Chart":
            ax.plot(df[x_axis], df[y_axis])

        elif chart_type == "Bar Chart":
            ax.bar(df[x_axis], df[y_axis])

        st.pyplot(fig)
    else:
        st.info("Please upload a CSV file to continue.")