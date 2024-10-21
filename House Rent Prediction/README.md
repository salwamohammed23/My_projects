# House Rent Prediction 

## Overview
This project focuses on predicting house rents using two machine learning models: **Linear Regression** and **Support Vector Regression (SVR)**. The dataset used is a CSV file containing various features related to house rentals.

## Key Steps

1. **Import Libraries**: Essential libraries for data manipulation, model training, and evaluation were imported, including `pandas`, `sklearn`, and `numpy`.

2. **Data Loading**: The dataset was loaded using `pandas`, allowing for easy manipulation and analysis.

3. **Data Preprocessing**:
   - Checked for missing values.
   - Encoded categorical variables using `LabelEncoder`.
   - Scaled features using `StandardScaler`.

4. **Data Splitting**: The dataset was split into training and test sets (80-20 split).

5. **Model Training**:
   - **Linear Regression**:
     - Model trained on the scaled data.
     - Evaluated with metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Median Absolute Error (MdSE).
   - **Support Vector Regression**:
     - Model trained using SVR with a radial basis function kernel.

6. **Model Evaluation**:
   - Both models' performance was assessed based on training and testing scores.
   - Predictions were made on the test set, and evaluation metrics were computed.

## Results

- **Linear Regression**:
  - Train Score: 0.719
  - Test Score: 0.692
  - MAE: 22.3685
  - MSE: 858.2936
  - MdSE: 17.1649

- **Support Vector Regression**:
  - Train Score: 0.8704
  - Test Score: 0.7613

## Conclusion
The project demonstrates effective approaches to predicting house rents using machine learning techniques. Both Linear Regression and SVR models showed promising results, with SVR achieving a higher training score.

