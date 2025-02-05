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
    """
    Reads and preprocesses the dataset from the given CSV file.
    """
    df = pd.read_csv(filepath)

    # Select relevant columns
    df = df[['Booking_ID', 'number of adults', 'number of children',
             'number of weekend nights', 'number of week nights', 'type of meal',
             'car parking space', 'room type', 'lead time', 'market segment type',
             'repeated', 'P-C', 'P-not-C', 'average price ', 'special requests',
             'date of reservation', 'booking status']]

    # Convert 'date of reservation' to datetime format
    df['date of reservation'] = pd.to_datetime(df['date of reservation'], errors='coerce')

    # Extract day, month, and year into separate columns
    df['reservation_day'] = df['date of reservation'].dt.day
    df['reservation_month'] = df['date of reservation'].dt.month
    df['reservation_year'] = df['date of reservation'].dt.year

    # Drop the original 'date of reservation' column
    df.drop(columns=['date of reservation'], inplace=True)

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

    # Remove duplicate values
    df.drop_duplicates(inplace=True)

    # Encode categorical features
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object'):
        df[col] = encoder.fit_transform(df[col].astype(str))

    return df



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
        "Choose:",
        options=["Dataset framwork",
            "Dataset Summary",
            "Scatterplot",
            "Boxplots for Outlier Detection",
            "subplot",
            "Feature Correlation Heatmap"
        ]
    )
     # Main content
    if visualization_option == "Dataset framwork":
        st.write("### 📌 Dataset framwork")
        st.write(df.head())

   
    if visualization_option == "Dataset Summary":
        st.write("### 📌 Dataset Info")
        st.write(df.columns)

        st.write("### 📌 Summary Statistics")
        st.write(df.describe())

    elif visualization_option == "Scatterplot":
        tab1, tab2, tab3, tab4 = st.tabs([
            "Adults vs. Price", "children vs. Price",
            "Lead Time vs. Price",
            "Special Requests vs. Price"
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
            st.subheader("🔍 Analysis Insights")
    
            st.markdown("✅ **Distribution of Data:**\n"
                        "   - Most bookings are for families with 0 to 3 children.\n "
                        "There are very few bookings for families with more than 3 children, with an outlier at 10 children.\n")
            
            st.markdown("✅ **Relationship Between Number of Children and Average Price:**\n"
                        "   - There is no clear increasing or decreasing trend between the number of children and the average price.\n")
            
            st.markdown("✅ **Booking Status :**\n"
                        "   - Blue dots (0 - Canceled) are present across all categories, meaning that cancellations occur regardless of the number of children.\n")
            
            st.markdown("✅ **Limited Range of Adult Counts:**\n"
                        "   - However, at higher numbers of children (especially 3+), there are more orange dots (1 - Not Canceled), suggesting that families with more children might be less likely to cancel compared to those with no children.\n")
            

    
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

            - **Difference in Booking Status (0 vs. 1)**:

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
            st.subheader("🔍 Analysis Insights")
    
            st.markdown("✅ **Distribution of Special Requests::**\n" 
                        "Most data points are clustered at lower numbers of special requests (0, 1, 2), indicating that most customers make few or no special requests.\n")
            
            st.markdown("✅ **Relationship Between Special Requests and Average Price:**\n"
                        "   - There is no clear linear relationship between special requests and average price. Customers with both low and high prices make special requests.\n")
            
            st.markdown("✅ **Special Requests vs. Cancellation:**\n"
                        "   - Customers with 0 special requests show a higher concentration of cancellations (blue dots) compared to those with more special requests.\n"
                        "   - As the number of special requests increases, there appears to be a higher proportion of orange dots (Not Canceled bookings).\n")
    
        # Tab 5: 3D Scatter Plot
       
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

    elif visualization_option == "subplot":
        tab1, tab2 = st.tabs([
            "Distribution", "cancellations_by_month"
        ])
                # Tab 1: Number of Adults vs. Average Price
        with tab1:
            st.write("### Distributions of Numerical Columns")
            num_cols = df.select_dtypes(include=['number']).columns
            plt.figure(figsize=(12, 8))
            for i, col in enumerate(num_cols[:6]):  # Limit to first 6 numerical columns
                plt.subplot(2, 3, i+1)
                sns.histplot(df[col], kde=True, bins=30)
                plt.title(f'Distribution of {col}')
            plt.tight_layout()
            st.pyplot(plt)
            st.subheader("🔍 Analysis Insights")
    
            st.markdown("✅ **  Distribution of Booking_ID::**\n"
                            "   - The distribution is uniform, indicating that the booking IDs are assigned sequentially without any missing data patterns.\n")
                
            st.markdown("✅ **Distribution of Number of Adults:**\n"
                "- A large peak at 2 adults, confirming that most bookings are for couples or pairs.\n"
                "- Smaller counts for 1 and 3 adults.\n"
                "- Few bookings with 4 adults, suggesting rare group bookings.\n"
                "- Presence of bookings with 0 adults, which may indicate data entry errors or test records.\n")
    
            st.markdown("✅ **Distribution of Number of Children:**\n"
                "- Most bookings have 0 children, as shown by the sharp peak.\n"
                "- Very few bookings with 1 or more children.\n"
                "- Some outliers with up to 10 children, likely to be data anomalies.\n"
                "- .\n")
    
                
            st.markdown("✅ **Distribution of Number of Weekend Nights:**\n"
                 "- The distribution is right-skewed, with most bookings having 0 to 2 weekend nights.\n"
                 "- Fewer bookings extend to 5 or more weekend nights, indicating shorter weekend stays are common.\n")
    
            st.markdown("✅ **Distribution of Number of Week Nights:**\n"
                         "- Similar right-skewed pattern but extends further compared to weekend nights.\n"
                        "- Many bookings are for 1 to 4 weeknights, with fewer extending up to 17 nights.\n")
            
            st.markdown("✅ **Distribution of Type of Meal:**\n"
                        "- A sharp peak at one category, suggesting a dominant meal type preferred by most customers.\n"
                        "- A few other categories with lower counts indicate less popular meal options.\n")
                        # Tab 1: Number of Adults vs. Average Price
        with tab1:
            def plot_cancellations_by_month(df):
                """
                Plots the number of canceled bookings per month in a Streamlit app.
                """
                # تصفية الحجوزات الملغاة (نفترض أن 0 تعني الإلغاء)
                canceled_df = df[df['booking status'] == 0]
            
                # حساب عدد الإلغاءات لكل شهر
                cancellations_by_month = canceled_df.groupby('reservation_month').size().reset_index(name='Cancellations')
            
                # رسم المخطط باستخدام Plotly
                fig = px.bar(cancellations_by_month, x='reservation_month', y='Cancellations', 
                             labels={'reservation_month': 'Month', 'Cancellations': 'Number of Cancellations'},
                             title='Number of Canceled Bookings per Month',
                             color='Cancellations', color_continuous_scale='reds')
            
                # عرض المخطط في Streamlit
                st.plotly_chart(fig)
                # عرض المخطط
        st.subheader("📉 Cancellation Analysis")
        plot_cancellations_by_month(df)



    elif visualization_option == "Feature Correlation Heatmap":
        st.write("### Feature Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Feature Correlation Heatmap")
        st.pyplot(plt)
        
        
        # Strong Positive Correlations
        st.markdown("### ✅ **Strong Positive Correlations:**")
        st.markdown("- **P-C and P-not-C (~1.0):** These features are almost perfectly correlated, which may indicate they represent similar or dependent variables. Consider checking for redundancy.")
        st.markdown("- **repeated and P-C (~0.97):** A very strong correlation suggests repeated bookings are strongly linked with the P-C variable.")
        st.markdown("- **number of adults and room type (~0.57):** Indicates that the number of adults influences the type of room booked.")
        
        # Moderate Correlations
        st.markdown("### ⚡ **Moderate Correlations:**")
        st.markdown("- **lead time and market segment type (~0.31):** Suggests that different market segments have varying booking lead times.")
        st.markdown("- **average price with room type and special requests:** Indicates pricing varies based on room type and customer requests.")
        
        # Weak or No Correlation
        st.markdown("### 🚫 **Weak or No Correlation:**")
        st.markdown("- **Booking_ID with other features (~0):** As expected, since IDs are unique identifiers.")
        st.markdown("- **number of children shows weak correlation with most features.**")
        
        # Potential Data Insights
        st.markdown("### 💡 **Potential Data Insights:**")
        st.markdown("- **special requests have a slight correlation with booking status,** indicating that special requests might influence cancellations or confirmations.")
        st.markdown("- **date of reservation has minimal correlation,** suggesting booking patterns are not heavily time-dependent.")

else:
    st.error("Failed to load the dataset. Please check the file path and try again.")
