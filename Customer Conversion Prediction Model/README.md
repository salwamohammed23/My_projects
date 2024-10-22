

# Customer Conversion Prediction Model

This project builds a neural network model to predict customer conversion based on a dataset from a bank marketing campaign. The dataset contains various features such as customer demographics, past interactions with the bank, and economic indicators. The target variable is whether or not the customer subscribed to a term deposit (`y`), which is binary-encoded for training purposes.

## Features

The project performs the following steps:

1. **Data Preprocessing**:
    - **Data Cleaning**: Missing values and duplicate rows are handled.
    - **Encoding**: Categorical variables are converted to numerical representations using `OneHotEncoder`.
    - **Feature Selection**: Key features with a significant correlation to the target variable are selected for modeling.

2. **Model Training**:
    - **Data Splitting**: The data is split into training and testing sets using `train_test_split`.
    - **Feature Scaling**: Features are standardized using `StandardScaler`.
    - **Neural Network**: A neural network model is built using `TensorFlow` and `Keras` with multiple dense layers and dropout for regularization.

3. **Model Evaluation**:
    - The model is trained and validated for 10 epochs, with metrics such as loss and accuracy being tracked for both training and validation sets.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `tensorflow`
- `scikit-learn`
- `category_encoders`

## Dataset

The dataset used in this project is the Bank Marketing dataset (`bank-additional-full.csv`), which can be found [here](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing). The dataset contains 21 columns, including demographic information, past interactions, and economic variables.

## Model Architecture

The neural network model consists of the following layers:

1. Dense layer with 128 units and ReLU activation
2. Dropout layer with a 50% dropout rate
3. Dense layer with 64 units and ReLU activation
4. Dropout layer with a 50% dropout rate
5. Dense layer with 32 units and ReLU activation
6. Dropout layer with a 50% dropout rate
7. Output layer with 1 unit and Sigmoid activation (for binary classification)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-repo/bank-marketing-prediction.git
cd bank-marketing-prediction
```

2. Run the script:

```bash
python main.py
```

3. Modify the `wrangle()` function in the script to point to the correct path of your dataset.

4. The model will output training/validation accuracy and loss for each epoch.

## Results

The model achieves the following results:

- Training Accuracy: 90%
- Validation Accuracy: 91%

