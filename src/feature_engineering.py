import pandas as pd

def create_features(df):
    # Convert 'resolved' and 'created' columns to datetime
    df['resolved'] = pd.to_datetime(df['resolved'], errors='coerce')
    df['created'] = pd.to_datetime(df['created'], errors='coerce')

    # Calculate issue duration in days
    df['issue_duration'] = (df['resolved'] - df['created']).dt.days

    # Fill NaN in 'issue_duration' with a specific value, e.g., -1
    df['issue_duration'] = df['issue_duration'].fillna(-1)

    # Fill missing values in numeric columns with the median
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # Fill missing values in non-numeric columns with a placeholder value or mode
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
