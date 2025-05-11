# GradePredictionML
This repository contains code and models for predicting student grades based on exam answers. It includes data preprocessing scripts, machine learning models (such as regression and classification algorithms), and evaluation metrics to assess model performance.
## Project Structure

```
GradePredictionML/
│
├── data/                       # Raw and processed data
│   ├── raw/                    # Original datasets
│   ├── processed/              # Cleaned/feature-engineered datasets
│   └── README.md               # Description of the data
│
├── notebooks/                  # Jupyter notebooks for data exploration, model development, etc.
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── src/                        # Source code
│   ├── __init__.py
│   ├── data_preprocessing.py   # Code for data cleaning and preprocessing
│   ├── feature_engineering.py  # Code for feature engineering
│   ├── model.py                # Model definition and training
│   ├── evaluation.py           # Model evaluation and metrics
│   └── utils.py                # Helper functions and utilities
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview and setup instructions
├── thesis_report.md            # Thesis document
├── config/                     # Configuration files (hyperparameters, etc.)
│   └── model_config.json       # Model hyperparameters, etc.
└── .gitignore                  # Git ignore file
```