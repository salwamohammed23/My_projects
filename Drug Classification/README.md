
# Drug Classification Using Decision Trees

This project aims to classify drugs based on patient data using a Decision Tree Classifier. The dataset includes various features such as age, sex, blood pressure, cholesterol levels, and sodium to potassium ratio. The goal is to predict which drug a patient should be prescribed based on these features.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [License](#license)

## Project Overview

The project implements a Decision Tree Classifier to analyze the drug prescription data. It involves data preprocessing, feature encoding, model training, and evaluation.

## Dataset

The dataset used in this project is `drug200.csv`, which contains 200 records and the following features:

- **Age**: Age of the patient
- **Sex**: Gender of the patient (F/M)
- **BP**: Blood pressure level (LOW/NORMAL/HIGH)
- **Cholesterol**: Cholesterol level (NORMAL/HIGH)
- **Na_to_K**: Sodium to potassium ratio
- **Drug**: Drug prescribed (categorical variable)

## Installation

To run this project, you need to have Python and the following libraries installed:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Usage

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Ensure the dataset `drug200.csv` is in the project directory.

3. Run the main script:
    ```bash
    python drug_classification.py
    ```

## Model Evaluation

The Decision Tree Classifier is evaluated using accuracy and confusion matrix metrics. The model was tuned using cross-validation and Randomized Search to find the best hyperparameters.



## Results

The model achieved a training accuracy of **100%** and a testing accuracy of **100%**. The feature importance indicated that the sodium to potassium ratio has the highest impact on drug classification.




