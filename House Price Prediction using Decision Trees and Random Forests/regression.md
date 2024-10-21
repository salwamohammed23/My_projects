
# House Price Prediction

## Overview
This project aims to predict house prices based on various features using machine learning techniques. It implements three regression models: Linear Regression, Logistic Regression, and Support Vector Regression (SVR). The dataset used is `House_Price.csv`, which contains features such as crime rate, residential area, air quality, number of rooms, age, and various distances to amenities.

## Features
- **Data Preprocessing**: Handling missing values and encoding categorical variables.
- **Model Implementation**:
  - Linear Regression
  - Logistic Regression
  - Support Vector Regression (SVR)
- **Performance Evaluation**: Using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and confusion matrix for classification models.

## Installation
To run this project, you'll need to have Python and the necessary libraries installed. You can install the required libraries using the following command:

```bash
pip install pandas scikit-learn numpy
```

## Usage
1. **Download the Dataset**: Ensure you have the `House_Price.csv` file in the same directory as your script.
2. **Run the Script**: Execute the Python script using your preferred Python environment. You can use Jupyter Notebook, Google Colab, or any Python IDE.

```python
python house_price_prediction.py
```

3. **View Results**: The script will output the predictions and performance metrics for each model used.

## Model Descriptions

### 1. Linear Regression
- A simple model used to predict a continuous target variable. The implementation includes normalization of features and evaluation of the model's performance on training and testing datasets.

### 2. Logistic Regression
- Used here for classification purposes. This model predicts the probability of classes based on input features. The confusion matrix and classification performance metrics are provided for evaluation.

### 3. Support Vector Regression (SVR)
- A regression algorithm that uses the concept of support vectors to predict the continuous target variable.

## Performance Metrics
- **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in predictions, without considering their direction.
- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors, giving more weight to larger errors.
- **Median Absolute Error**: The median of all absolute errors, providing a robust measure against outliers.

