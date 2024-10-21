### Project Overview

This project provides a streamlined process for **Data Cleaning**, **Visualization**, and **Statistical Analysis** of a dataset, with a focus on improving data quality and extracting valuable insights through geographic and exploratory visualizations, as well as statistical summaries.

### Key Steps

1. **Data Cleaning (wrangle function)**:
   - Load and clean the data by handling missing values and removing duplicates.
   - Focuses on the following columns: `['name', 'latitude', 'neighbourhood', 'longitude', 'price', 'availability_365', 'room_type', 'minimum_nights', 'calculated_host_listings_count']`.
   - Ensures data reliability and accuracy for further analysis.

2. **Visualization (Visualization function)**:
   - **Geographical Distribution**: Scatter plots and maps to visualize data based on latitude and longitude.
   - **Neighborhood Analysis**: Insights into the relationship between neighborhoods and various listing characteristics such as price, availability, room type, and minimum nights.
   - **Room Type and Availability Analysis**: Bar plots to show the distribution of room types and the relationship between price, room type, and availability.
   - **3D Scatter Plot**: Interactive 3D visualization for room types, price, and availability.

3. **Statistical Analysis (Statistical function)**:
   - **Correlation Analysis**: Heatmap showing the correlation between price, availability, minimum nights, room type, neighborhood, and calculated host listings.
   - **Central Tendency Measures**:
     - **Mean**: Calculates the average values of price and availability.
     - **Median**: Determines the middle values of price and availability.
     - **Mode**: Identifies the most frequently occurring values for price, availability, and room type.
   - **Summary Statistics**: Detailed numerical summaries, including count, mean, standard deviation, minimum, quartiles, and maximum values for selected columns.

### Requirements

Before running the project, ensure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn
```

### How to Use

1. **Data Cleaning**:
   The `wrangle()` function takes the file path of your CSV file and processes the data by:
   - Handling missing values (using the mean strategy for numeric columns).
   - Removing duplicate rows.
   
   Example:
   ```python
   df = wrangle('listings.csv')
   ```

2. **Data Visualization**:
   The `Visualization()` function generates various visualizations including scatter plots, bar plots, and a 3D scatter plot to analyze price, availability, neighborhood, and room type distributions.
   
   Example:
   ```python
   Visualization(df)
   ```

3. **Statistical Analysis**:
   The `Statistical()` function performs correlation analysis, calculates central tendency measures (mean, median, mode), and provides a heatmap to visualize relationships between different features.
   
   Example:
   ```python
   Statistical(df)
   ```

4. **Summary Statistics**:
   Generates summary statistics for `price`, `availability_365`, `room_type`, `minimum_nights`, and `neighbourhood` columns.
   
   Example:
   ```python
   summary_stats = df[['price', 'availability_365', 'room_type', 'minimum_nights', 'neighbourhood']].describe()
   print(summary_stats)
   ```

### Visualizations Overview

- **Scatter Maps**: Visualize the geographical distribution of listings.
- **Neighborhood Scatter Plots**: Reveal relationships between neighborhood, price, availability, and room types.
- **Bar Plots**: Display the distribution of room types and availability in the dataset.
- **3D Scatter Plot**: Interactive plot showing relationships between room type, price, and availability.

### Statistical Insights

- **Mean, Median, Mode**: Gain a deeper understanding of central tendencies in the dataset, including insights into typical listing prices and availability.
- **Correlation Heatmap**: Helps in identifying features that have strong relationships, useful for feature selection and model building.

### Conclusion

This project helps to preprocess, visualize, and statistically analyze a dataset of listings, providing valuable insights for further exploration or modeling.
