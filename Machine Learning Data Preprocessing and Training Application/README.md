
# Machine Learning Data Preprocessing and Training Application

This application provides a user-friendly command-line interface for loading, preprocessing, exploring, and training machine learning models on structured datasets. Users can input a dataset, handle missing values, perform exploratory data analysis (EDA), and train models interactively.

## Features

- **Data Loading**: Load your dataset in CSV format by specifying the file path.
- **Handling Missing Values**:
  - Continuous features can be handled by replacing missing values using the mean, median, or mode.
  - Categorical features can be handled using an ordinal encoder or imputer.
- **Dropping Columns**: Optionally drop specific columns from the dataset.
- **Exploratory Data Analysis (EDA)**:
  - Generate histograms, box plots, and scatter plots to visually explore your data.
  - Display statistical summaries (mean, median, mode, standard deviation).
- **Model Training**: Select a target variable and train machine learning models on your dataset.

## Requirements

Before running the application, ensure you have the following Python packages installed:

```bash
pip install pandas matplotlib scikit-learn
```

## How to Use

1. **Run the Script**:
   - Run the script using Python:

     ```bash
     python main.py
     ```

2. **Follow the Instructions**:
   - After running the script, follow the prompts to:
     - Input the path to your dataset.
     - Specify how you want to handle missing values for continuous and categorical features.
     - Choose whether to drop certain columns.
     - Explore your dataset through various visualizations and summary statistics.
     - Train a machine learning model by selecting a target variable.

## Application Flow

1. **Data Loading**:
   - You will be prompted to provide the file path for the dataset you want to analyze.

2. **Preprocessing**:
   - Choose how to treat missing values for both continuous and categorical features.

3. **EDA**:
   - You can generate various plots (histograms, box plots, scatter plots) to visualize your data.
   - Get a statistical summary of your data, including mode and other summary statistics.

4. **Model Training**:
   - Select the target variable for your model.
   - Train the machine learning model and validate its performance.

## Example

```bash
> Machine Learning Package
> put your pass: path_to_your_file.csv
> choose the way to trate with continuous features choose   'mean()', 'median()', or 'mode()': mean()
> choose the way to trate with categorical features choose   'ordinal_encoder', or 'imputer': imputer
> Do you want to drop column choose 'y' or 'n': y
> Enter the columns you want to drop (separated by commas): column1, column2
> Select the target variable: target_column
> Do you want to Explor your Data  choose 'y' or 'n': y
> Do you want to get summary_statistical for  your Data  choose 'y' or 'n': y
> Do you want to train the  choose 'y' or 'n': y
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

