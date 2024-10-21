
# House Price Prediction using Decision Trees and Random Forests

This project demonstrates the use of Decision Trees and Random Forests to predict house sale prices using the Ames housing dataset. The goal is to train a model that accurately predicts house prices based on various features such as lot area, year built, number of rooms, and more.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Modeling Techniques](#modeling-techniques)
  - [Decision Tree Regressor](#decision-tree-regressor)
  - [Optimizing Decision Tree](#optimizing-decision-tree)
  - [Random Forest Regressor](#random-forest-regressor)
- [Results](#results)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [References](#references)

## Overview

The project involves training a machine learning model to predict house prices using features like:
- Lot Area
- Year Built
- 1st and 2nd Floor Square Footage
- Number of Full Bathrooms
- Bedrooms Above Ground
- Total Rooms Above Ground

We use two types of models:
1. **Decision Tree Regressor**
2. **Random Forest Regressor**

The performance of these models is evaluated using the Mean Absolute Error (MAE) metric.

## Dataset

The dataset used is the [Ames Housing Dataset](https://www.kaggle.com/c/home-data-for-ml-course/data), which includes 79 features related to houses in Ames, Iowa.

The main features we focus on in this project are:
- `LotArea`
- `YearBuilt`
- `1stFlrSF`
- `2ndFlrSF`
- `FullBath`
- `BedroomAbvGr`
- `TotRmsAbvGrd`
- Target Variable: `SalePrice`

## Modeling Techniques

### Decision Tree Regressor

We start by training a basic `DecisionTreeRegressor` model on the dataset. The goal is to predict the target variable `SalePrice` based on the selected features.

```python
from sklearn.tree import DecisionTreeRegressor

# Create and train the Decision Tree model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)
```

### Optimizing Decision Tree

To improve the accuracy of the Decision Tree, we experiment with different `max_leaf_nodes` values and select the one that minimizes the Mean Absolute Error (MAE).

```python
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    return mean_absolute_error(val_y, preds_val)

# Loop through candidate values for max_leaf_nodes
best_tree_size = min({leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}, key=my_mae.get)
```

### Random Forest Regressor

To further improve predictions, we use a `RandomForestRegressor`, which generally provides better performance by combining multiple decision trees.

```python
from sklearn.ensemble import RandomForestRegressor

# Create and train the Random Forest model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
```

## Results

The models' performance is evaluated using the Mean Absolute Error (MAE):
- **Decision Tree (without optimization)**: MAE = 29,653
- **Optimized Decision Tree**: MAE = 27,283
- **Random Forest Regressor**: MAE = 21,857

The Random Forest model outperforms the Decision Tree models, showing its ability to generalize better to unseen data.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- numpy

You can install the dependencies using:
```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python house_price_prediction.py
   ```

## References

- Kaggle Ames Housing Dataset: [https://www.kaggle.com/c/home-data-for-ml-course](https://www.kaggle.com/c/home-data-for-ml-course)
- Scikit-learn Documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
