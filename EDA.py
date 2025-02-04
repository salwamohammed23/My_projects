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

# Streamlit app
st.title("Hotel Booking Data Analysis")

# Load and preprocess data
filepath = 'first inten project.csv'
df = wrangle(filepath)

if df is not None:
    # Sidebar for user inputs
    st.sidebar.title("📊 EDA")

    # Add a radio button to select one visualization
    visualization_option = st.sidebar.radio(
        "Choose a Visualization:",
        options=[
            "Dataset Summary",
            "Scatterplot",
            "Boxplots for Outlier Detection",
            "Distributions of Numerical Columns",
            "Feature Correlation Heatmap"
        ]
    )

    # Main content
    if visualization_option == "Dataset Summary":
        st.write("### 📌 Dataset Info")
        st.write(df.columns)

        st.write("### 📌 Summary Statistics")
        st.write(df.describe())

    elif visualization_option == "Scatterplot":
        tab1, tab2, tab3, tab4 = st.tabs([
            "Number of Adults vs. Average Price",
            "Lead Time vs. Average Price",
            "Special Requests vs. Average Price",
            "3D Scatter Plot"
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
            st.subheader("🔍 Analysis Insights")
    
            st.markdown("✅ **Increasing Cost with More Adults:**\n"
                        "   - Generally, as the number of adults increases, the average price also rises. "
                        "This is expected since larger accommodations or extra services are required.\n")
            
            st.markdown("✅ **Outliers in Pricing:**\n"
                        "   - Some points show exceptionally high prices, possibly due to luxury bookings or premium services.\n")
            
            st.markdown("✅ **Variation in Booking Status:**\n"
                        "   - Different booking statuses (0 and 1) suggest pricing variations based on confirmation or cancellation.\n")
            
            st.markdown("✅ **Limited Range of Adult Counts:**\n"
                        "   - The number of adults is capped at 4, indicating a focus on small group or family reservations.\n")
            
            st.markdown("✅ **Potential Impact of External Factors:**\n"
                        "   - Seasonal changes, promotions, and events might influence price variations.\n")
         with tab2:
            st.write("### Number of children vs. Average Price")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x=df['number of children'], y=df['average price '], hue=df['booking status'], ax=ax)
            ax.set_title("Number of children vs. Average Price")
            ax.set_xlabel("Number of children")
            ax.set_ylabel("Average Price")
            st.pyplot(fig)    
    
        # Tab 3: Lead Time vs. Average Price
        with tab3:
            st.write("### Lead Time vs. Average Price")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x=df['lead time'], y=df['average price '], hue=df['booking status'], ax=ax)
            ax.set_title("Lead Time vs. Average Price")
            ax.set_xlabel("Lead Time (Days)")
            ax.set_ylabel("Average Price")
            st.pyplot(fig)
            st.header("Analysis Insights")
            st.markdown("""
            - **Inverse Relationship Between Lead Time and Price**:  
              As Lead Time increases, the Average Price tends to decrease. Early bookings (higher lead time) often secure lower prices, while last-minute bookings (low lead time) may be more expensive.
            
            - **High Density of Bookings at Lower Lead Times**:  
              The majority of bookings occur at a lead time of less than 100 days, indicating that most customers book within this period. A significant number of bookings also exist close to zero lead time, suggesting frequent last-minute reservations.
            
            - **Outliers in Price**:  
              There are a few points where prices are exceptionally high, particularly for low lead times (last-minute bookings). This could be due to premium rooms, peak season pricing, or high-demand periods.
            
            - **Few Bookings Beyond 300 Days**:  
              Very few bookings extend beyond 300-400 days, indicating that most people don’t plan trips that far in advance.

            - ** Difference in Booking Status (0 vs. 1)**:

               it appears that bookings with lower lead times may have a higher probability of cancellations.
            """)
                
        # Tab 4: Special Requests vs. Average Price
        with tab4:
            st.write("### Special Requests vs. Average Price")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x=df['special requests'], y=df['average price '], hue=df['booking status'], ax=ax)
            ax.set_title("Special Requests vs. Average Price")
            ax.set_xlabel("Number of Special Requests")
            ax.set_ylabel("Average Price")
            st.pyplot(fig)
    
        # Tab 5: 3D Scatter Plot
        with tab5:
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
        
    elif visualization_option == "Boxplots for Outlier Detection":
        st.write("### Boxplots for Outlier Detection")
        num_cols = df.select_dtypes(include=['number']).columns
        plt.figure(figsize=(12, 6))
        for i, col in enumerate(num_cols[:6]):  # Limit to first 6 numerical columns
            plt.subplot(2, 3, i+1)
            sns.boxplot(y=df[col])
            plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
In this dataset, boxplots are generated for multiple features:

- **Booking ID**: The range of values is wide, but no extreme outliers are evident.  
- **Number of adults**: A few outliers exist, indicating unusually high numbers of adults in some bookings.  
- **Number of children**: Outliers suggest that some bookings have an exceptionally high number of children.  
- **Number of weekend nights**: Some bookings have significantly more weekend nights than others.  
- **Number of week nights**: Many outliers indicate that a few bookings have significantly longer stays during the week.  
- **Type of meal**: Outliers appear, suggesting some unusual meal-type entries.  
""")

    elif visualization_option == "Distributions of Numerical Columns":
        st.write("### Distributions of Numerical Columns")
        num_cols = df.select_dtypes(include=['number']).columns
        plt.figure(figsize=(12, 8))
        for i, col in enumerate(num_cols[:6]):  # Limit to first 6 numerical columns
            plt.subplot(2, 3, i+1)
            sns.histplot(df[col], kde=True, bins=30)
            plt.title(f'Distribution of {col}')
        plt.tight_layout()
        st.pyplot(plt)

    elif visualization_option == "Feature Correlation Heatmap":
        st.write("### Feature Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Feature Correlation Heatmap")
        st.pyplot(plt)
else:
    st.error("Failed to load the dataset. Please check the file path and try again.")
