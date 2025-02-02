import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Function to load data
@st.cache_data


df = df = pd.read_csv("first inten project.csv")

if df is not None:
    # Function to preprocess data
    @st.cache_data(hash_funcs={pd.DataFrame: lambda _: None})
    def preprocess_data(df):
        # Handle missing numerical values
        imputer = SimpleImputer(strategy='mean')
        numeric_columns = df.select_dtypes(include='number').columns
        df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
        
        # Handle missing categorical values
        df.fillna("Unknown", inplace=True)
        
        # Remove duplicates
        df.drop_duplicates(inplace=True)
        
        # Encode categorical variables
        encoders = {}
        for col in df.select_dtypes(include='object'):
            encoders[col] = LabelEncoder()
            df[col] = encoders[col].fit_transform(df[col].astype(str))
        
        return df, encoders

    df, encoders = preprocess_data(df)

    # Sidebar navigation
    st.sidebar.title("🔍 Data Exploration")
    if st.sidebar.button("🗂️ Show Raw Data"):
        st.write(df.head())
    
    if st.sidebar.button("📊 Statistical Analysis"):
        st.write(df.describe())
    
    # Visualization options
    st.sidebar.title("Choose Analysis Type")
    option = st.sidebar.selectbox(
        "Select chart type", 
        ["Adults vs. Average Price", "Lead Time vs. Average Price", "Special Requests vs. Average Price", "3D Visualization"]
    )
    
    color = st.sidebar.color_picker("Pick a color for visualization", "#3498db")
    
    # Display selected visualization
    st.title("📊 Hotel Booking Data Analysis")
    
    if option == "Adults vs. Average Price":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['number of adults'], y=df['average price'], hue=df['booking status'], ax=ax, color=color)
        ax.set_title("Adults vs. Average Price")
        ax.set_xlabel("Number of Adults")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)
    
    elif option == "Lead Time vs. Average Price":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['lead time'], y=df['average price'], hue=df['booking status'], ax=ax, color=color)
        ax.set_title("Lead Time vs. Average Price")
        ax.set_xlabel("Lead Time (Days)")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)
    
    elif option == "Special Requests vs. Average Price":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['special requests'], y=df['average price'], hue=df['booking status'], ax=ax, color=color)
        ax.set_title("Special Requests vs. Average Price")
        ax.set_xlabel("Number of Special Requests")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)
    
    elif option == "3D Visualization":
        fig = px.scatter_3d(
            df, x='lead time', y='number of adults', z='average price', 
            color='booking status', hover_data=['number of children', 'room type', 'market segment type'],
            title="📌 3D Visualization of Hotel Bookings"
        )
        st.plotly_chart(fig)
    
    if st.sidebar.button("📈 Interactive Charts"):
        fig = px.scatter_3d(df, x='lead time', y='number of adults', z='average price', color='booking status')
        st.plotly_chart(fig)
    
    if st.sidebar.button("🔗 Correlation Analysis"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
        st.pyplot(fig)
    
    if st.sidebar.button("📊 Data Distribution Analysis"):
        numeric_columns = df.select_dtypes(include='number').columns
        for col in numeric_columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(df[col], bins=30, kde=True, color=color, ax=ax)
            ax.set_title(f"Distribution of {col}")
            st.pyplot(fig)
else:
    st.warning("Please upload a CSV file to proceed.")
