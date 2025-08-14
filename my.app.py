
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Hospital_infections App", layout="wide")

st.title("Hospital_infections Analysis Project 🏥")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your Hospital_infections CSV file", type="csv")

if uploaded_file is not None:
    st.success("Your CSV file has been uploaded successfully! ✅")
    
    # Read first 5000 rows for speed
    df = pd.read_csv(uploaded_file, nrows=5000)
    
    # Create 3 tabs
    tabs = st.tabs(["📄 Data", "📊 General Statistics", "📈 Visualizations"])
    
    # Tab 1: Data
    with tabs[0]:
        st.subheader("First 5 Rows of the Data")
        st.dataframe(df.head())
    
    # Tab 2: General Statistics
    with tabs[1]:
        st.subheader("General Statistics")
        st.write(df.describe())
    
    # Tab 3: Visualizations
    with tabs[2]:
        st.subheader("Visualizations")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        selected_column = st.selectbox("Choose a numeric column to visualize", numeric_cols)
        
        # Histogram
        st.write(f"Histogram for {selected_column}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Boxplot
        st.write(f"Boxplot for {selected_column}")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[selected_column], ax=ax2)
        st.pyplot(fig2)
