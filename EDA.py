import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Function to load and preprocess data
def wrangle(filepath):
    try:
        # Read CSV file
        df = pd.read_csv(filepath)

        # Select relevant columns
        columns = ['Booking_ID', 'number of adults', 'number of children',
                   'number of weekend nights', 'number of week nights', 'type of meal',
                   'car parking space', 'room type', 'lead time', 'market segment type',
                   'repeated', 'P-C', 'P-not-C', 'average price ', 'special requests',
                   'date of reservation', 'booking status']
        
        # Check if all columns exist in the dataframe
        missing_cols = set(columns) - set(df.columns)
        if missing_cols:
            st.warning(f"Missing columns: {missing_cols}")
            return None

        df = df[columns]

        # Handle missing values
        if df.isnull().sum().sum() > 0:
            imputer = SimpleImputer(strategy='mean')  # Replace missing values with column mean
            numeric_columns = df.select_dtypes(include='number').columns
            df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

        # Remove duplicate values
        if df.duplicated().sum() > 0:
            df.drop_duplicates(inplace=True)

        # Encode categorical features
        encoder = LabelEncoder()
        for col in df.select_dtypes(include='object'):
            df[col] = encoder.fit_transform(df[col].astype(str))

        return df

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load and preprocess data
filepath = 'first inten project.csv'
df = wrangle(filepath)

if df is not None:
    # Main page
    st.title("Hotel Booking Data Analysis")
    st.write("### Dataset Head")
    st.write(df.head())

    # Create tabs for scatter plots
    tab1, tab2, tab3 = st.tabs([
        "Number of Adults vs. Average Price",
        "Lead Time vs. Average Price",
        "Special Requests vs. Average Price"
    ])

    # Tab 1: Number of Adults vs. Average Price
    with tab1:
        st.write("### Number of Adults vs. Average Price")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['number of adults'], y=df['average price '], hue=df['booking status'], ax=ax)
        ax.set_title("Number of Adults vs. Average Price")
        ax.set_xlabel("Number of Adults")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)

    # Tab 2: Lead Time vs. Average Price
    with tab2:
        st.write("### Lead Time vs. Average Price")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['lead time'], y=df['average price '], hue=df['booking status'], ax=ax)
        ax.set_title("Lead Time vs. Average Price")
        ax.set_xlabel("Lead Time (Days)")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)

    # Tab 3: Special Requests vs. Average Price
    with tab3:
        st.write("### Special Requests vs. Average Price")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df['special requests'], y=df['average price '], hue=df['booking status'], ax=ax)
        ax.set_title("Special Requests vs. Average Price")
        ax.set_xlabel("Number of Special Requests")
        ax.set_ylabel("Average Price")
        st.pyplot(fig)

    # Additional visualizations in separate sections
    st.write("### 3D Scatter Plot of Hotel Bookings")
    fig = px.scatter_3d(
        df,  # Our DataFrame
        x='lead time',  # X-axis: How far in advance the booking was made
        y='number of adults',  # Y-axis: Number of adults in the booking
        z='average price ',  # Z-axis: Price of the booking
        color='booking status',  # Color the points based on booking status
        hover_data=['number of children', 'room type', 'market segment type'],  # Extra details on hover
        title="3D Scatter Plot of Hotel Bookings"
    )
    fig.update_layout(
        width=800,  # Set figure width
        height=600,  # Set figure height
        scene=dict(
            xaxis_title='Lead Time (Days)',
            yaxis_title='Number of Adults',
            zaxis_title='Average Price ($)'
        )
    )
    st.plotly_chart(fig)

    st.write("### Boxplots for Outlier Detection")
    num_cols = df.select_dtypes(include=['number']).columns
    plt.figure(figsize=(12, 6))
    for i, col in enumerate(num_cols[:6]):  # Limit to first 6 numerical columns
        plt.subplot(2, 3, i+1)
        sns.boxplot(y=df[col])
        plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    st.pyplot(plt)

    st.write("### Distributions of Numerical Columns")
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(num_cols[:6]):  # Limit to first 6 numerical columns
        plt.subplot(2, 3, i+1)
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f'Distribution of {col}')
    plt.tight_layout()
    st.pyplot(plt)

    st.write("### Feature Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    st.pyplot(plt)
