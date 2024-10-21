# Pulsar Star Classification using SVM

This project applies Support Vector Machine (SVM) classifiers to classify pulsar stars based on their physical characteristics. The dataset used for this classification is the `pulsar_data.csv`, containing 17898 instances and 9 features, including the target variable `target_class`.

## Dataset Overview
The dataset contains the following columns:
- **IP Mean**: Mean of the integrated profile
- **IP Sd**: Standard deviation of the integrated profile
- **IP Kurtosis**: Excess kurtosis of the integrated profile
- **IP Skewness**: Skewness of the integrated profile
- **DM-SNR Mean**: Mean of the DM-SNR curve
- **DM-SNR Sd**: Standard deviation of the DM-SNR curve
- **DM-SNR Kurtosis**: Excess kurtosis of the DM-SNR curve
- **DM-SNR Skewness**: Skewness of the DM-SNR curve
- **target_class**: The target class, where 0 indicates non-pulsar and 1 indicates pulsar

The dataset is class-imbalanced, with approximately 90.8% of the data belonging to class 0.

## Exploratory Data Analysis
The dataset does not contain any missing values. Some column names had leading spaces, which were cleaned up, and the columns were renamed for easier manipulation. The dataset has only numerical features.

## Data Preprocessing
- **Feature Scaling**: Standard scaling was applied to all feature columns using `StandardScaler`.
- **Train-Test Split**: The dataset was split into a training set (80%) and a test set (20%).

## SVM Classifier
Support Vector Machine (SVM) was used as the classifier for this project. Several experiments were run with different hyperparameters:

1. **Default Hyperparameters**:
   - Accuracy: `98.27%`

2. **SVM with RBF kernel and C=100**:
   - Accuracy: `98.32%`

3. **SVM with RBF kernel and C=1000**:
   - Accuracy: `98.16%`

4. **SVM with Linear kernel and C=1**:
   - Accuracy: `98.30%`

5. **SVM with Linear kernel and C=100**:
   - Accuracy: `98.32%`

6. **SVM with Linear kernel and C=1000**:
   - Accuracy: `98.32%`

## Model Evaluation
The accuracy of the SVM model with various hyperparameters was compared with the null accuracy of `92.35%`. The model's accuracy of `98.32%` significantly outperforms the null accuracy, indicating the model performs well on this dataset.

### Train-Test Accuracy Comparison
The training accuracy was `97.83%`, and the test accuracy was `98.30%`, indicating no overfitting.

## Conclusion
SVM models perform well on the pulsar dataset, with the best accuracy achieved using a linear kernel and C=100 or C=1000. The accuracy was comparable across different configurations, and there was no indication of overfitting.

## How to Run the Code
1. Clone the repository.
2. Install required libraries:
    ```bash
    pip install numpy pandas scikit-learn matplotlib seaborn
    ```
3. Run the Jupyter notebook or Python script to train the SVM models and evaluate their performance.

## License
This project is licensed under the MIT License.
