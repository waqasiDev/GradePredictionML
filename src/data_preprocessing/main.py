import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """
    Load data from an Excel file.
    """
    data = pd.read_excel(file_path)
    print(f"Data loaded: {data.shape} rows, {data.columns}")
    return data

def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values and encoding categorical variables.
    """
    # Clean column names by stripping any leading/trailing spaces
    data.columns = data.columns.str.strip()

    # Handle missing values in 'Points' by filling them with the mean
    points_imputer = SimpleImputer(strategy='mean')
    data['Points'] = points_imputer.fit_transform(data[['Points']])

    # Encode the 'Answer' column (correct answers) using LabelEncoder
    answer_encoder = LabelEncoder()
    data['Answer'] = answer_encoder.fit_transform(data['Answer'])

    # For 'Answer Choices', we'll remove newline characters and unnecessary spaces
    data['Answer Choices'] = data['Answer Choices'].str.replace('\n', ' ', regex=False)
    data['Answer Choices'] = data['Answer Choices'].str.strip()

    # Split the data into features (X) and target (y)
    X = data[['Question', 'Answer Choices']]  # Features (you might want to include more features if available)
    y = data['Answer']  # Target (correct answers)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def main():
    # Path to your Excel file
    file_path = 'data/raw/exam_data.xlsx'  # Adjust this path as needed

    # Load and preprocess the data
    data = load_data(file_path)
    X_train, X_test, y_train, y_test = preprocess_data(data)

    print(f"Training data shape: {X_train.shape}")
    print(f"Test data shape: {X_test.shape}")

if __name__ == "__main__":
    main()
