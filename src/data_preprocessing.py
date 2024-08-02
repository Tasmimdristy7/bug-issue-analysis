import pandas as pd

def load_data(filepath):
    """
    Load data from a CSV file.
    
    :param filepath: Path to the CSV file
    :return: Pandas DataFrame
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error
def clean_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing target values (if applicable)
    if 'target_column' in df.columns:
        df = df.dropna(subset=['target_column'])

    # Handle missing values for numerical columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # Handle missing values for categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Convert date columns to datetime format and handle errors
    date_cols = ['resolved', 'created']  # Replace with actual date columns
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Remove rows with NaT (Not a Time) values in date columns
    df = df.dropna(subset=date_cols)

    # Remove outliers or apply any other custom data cleaning steps
    # For example, you might want to remove rows with unrealistic values

    return df
