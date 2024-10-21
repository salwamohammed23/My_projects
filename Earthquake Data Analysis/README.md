
# Earthquake Data Analysis

## Overview
This project involves analyzing earthquake data to predict earthquake magnitudes using Support Vector Regression (SVR). The dataset contains historical earthquake records with features such as latitude, longitude, depth, and datetime.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Modeling](#modeling)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/earthquake-data-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd earthquake-data-analysis
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your dataset (`Earthquakes.csv`) in the project directory.
2. Run the analysis script:
   ```bash
   python earthquake_analysis.py
   ```

## Data Description
The dataset contains the following columns:
- **DATETIME**: The date and time of the earthquake.
- **LAT**: Latitude of the earthquake.
- **LONG**: Longitude of the earthquake.
- **DEPTH**: Depth of the earthquake (in km).
- **MAGNITUDE**: Magnitude of the earthquake (Richter scale).

### Example Data
| DATETIME          | LAT    | LONG   | DEPTH | MAGNITUDE |
|-------------------|--------|--------|-------|-----------|
| 1/7/1965 10:22    | 36.50  | 26.50  | 10.0  | 5.3       |
| 1/10/1965 8:02    | 39.25  | 22.25  | 10.0  | 4.9       |

## Modeling
The project implements a Support Vector Regression (SVR) model to predict earthquake magnitudes. Key steps include:
1. **Data Preprocessing**: Handling missing values and scaling features.
2. **Feature Engineering**: Extracting useful features from the `DATETIME` column.
3. **Model Training**: Training the SVR model with hyperparameter tuning.

### Hyperparameters
- `C`: Regularization parameter.
- `epsilon`: Tolerance for the epsilon-insensitive loss function.
- `kernel`: The kernel type used in the algorithm (e.g., 'linear', 'rbf').

## Results
The performance of the SVR model is evaluated using:
- **Training Score**: (e.g., -0.03)
- **Test Score**: (e.g., -0.04)
- Additional metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) can also be included.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

