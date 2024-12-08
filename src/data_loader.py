import numpy as np
import pandas as pd

def load_data(file_path):
    """Load and parse CSV data with timestamp conversion."""
    return pd.read_csv(file_path, parse_dates=['Timestamp'])

def data_quality_check(df):
    """Check for missing and negative values in the dataset."""
    missing_values = df.isnull().sum()
    negative_values = df.select_dtypes(include=[np.number]).lt(0).sum()
    return missing_values, negative_values