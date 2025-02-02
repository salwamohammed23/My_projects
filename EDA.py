import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data
def wrangle(filepath):
    df = pd.read_csv(filepath)
    
    # Select relevant columns
    df = df[['Booking_ID', 'number of adults', 'number of children',
             'number of weekend nights', 'number of week nights', 'type of meal',
             'car parking space', 'room type', 'lead time', 'market segment type',
             'repeated', 'P-C', 'P-not-C', 'average price ', 'special requests',
             'date of reservation', 'booking status']]
    
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Encode categorical features
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object'):
        df[col] = encoder.fit_transform(df[col].astype(str))
    
    return df

# Streamlit App
st.title("Hotel Booking Data Analysis")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df = wrangle(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("## Dataset Preview")
        st.write(df.head())
        
        # Summary statistics
        st.write("## Summary Statistics")
        st.write(df.describe())
        
        # Correlation Heatmap
        st.write("## Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
        st.pyplot(fig)
    
    with col2:
        # Scatter plot
        st.write("## Scatter Plots")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='number of adults', y='average price ', hue='booking status', ax=ax)
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='lead time', y='average price ', hue='booking status', ax=ax)
        st.pyplot(fig)
        
        # 3D Scatter Plot
        st.write("## 3D Scatter Plot")
        fig = px.scatter_3d(
            df, x='lead time', y='number of adults', z='average price ', 
            color='booking status', hover_data=['number of children', 'room type', 'market segment type'],
            title="3D Scatter Plot of Hotel Bookings")
        st.plotly_chart(fig)
    
    # Boxplots for Outlier Detection
    st.write("## Boxplots")
    num_cols = df.select_dtypes(include=['number']).columns
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df[num_cols])
    st.pyplot(fig)
