
# Diabetes Prediction Model

This project involves building a deep learning model to predict diabetes using a dataset containing various health metrics. The model is designed to help in early diagnosis and treatment planning for diabetes.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Results](#results)
- [Model Prediction](#model-prediction)


## Overview

The aim of this project is to create a neural network model that accurately predicts whether a person has diabetes based on several health metrics. The model is built using Keras and trained on a dataset that includes features like glucose levels, body mass index (BMI), age, and more.

## Dataset

The dataset used in this project is the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database). The dataset contains the following columns:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function
- **Age**: Age (years)
- **Outcome**: Class variable (0 or 1) indicating whether a patient has diabetes

## Installation

To run this project, ensure you have Python and the following packages installed:

```bash
pip install numpy pandas matplotlib keras scikit-learn
```

## Usage

1. Load the dataset:

   ```python
   import pandas as pd
   data = pd.read_csv("diabetes.csv")
   ```

2. Preprocess the data by normalizing and splitting it into training and testing sets.

3. Build and compile the model:

   ```python
   from keras.models import Sequential
   from keras.layers import Dense

   model = Sequential()
   model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
   model.add(Dense(100, activation='relu'))
   model.add(Dense(2, activation='softmax'))
   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
   ```

4. Train the model:

   ```python
   model.fit(X_train, Y_train, validation_split=0.3, epochs=100, callbacks=[early_stopping_monitor])
   ```

5. Save the trained model:

   ```python
   model.save('Diabetes_model.h5')
   ```

## Model Architecture

The neural network consists of multiple layers:

- Input Layer: 100 neurons (ReLU activation)
- Hidden Layers: 3 layers with 100, 200, and 50 neurons respectively (ReLU activation)
- Output Layer: 2 neurons (Softmax activation for binary classification)

## Training

The model is trained using the categorical cross-entropy loss function and the Adam optimizer. Early stopping is implemented to prevent overfitting.

## Results

During training, the model achieved the following metrics:

- Accuracy: [Insert final accuracy]
- Validation Loss: [Insert final validation loss]

## Model Prediction

To make predictions with the trained model, load it and pass test data:

```python
from keras.models import load_model

model = load_model('Diabetes_model.h5')
predictions = model.predict(X_test)
```

The output will provide the probabilities for each class (diabetes or not).

