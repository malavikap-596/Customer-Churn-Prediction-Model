import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Drop missing values
    df.dropna(inplace=True)
    
    # Drop customerID (not useful)
    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)

    return df


def feature_engineering(df):
    # Create tenure groups
    def tenure_group(x):
        if x <= 12:
            return '0-12'
        elif x <= 36:
            return '12-36'
        else:
            return '36+'

    df['tenure_group'] = df['tenure'].apply(tenure_group)
    return df