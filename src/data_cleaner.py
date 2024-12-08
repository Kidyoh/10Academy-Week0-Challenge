import pandas as pd
import numpy as np

def clean_solar_radiation(df):
    """Clean solar radiation components."""
    df_clean = df.copy()
    # Replace negative GHI with 0 (nighttime)
    df_clean.loc[df_clean['GHI'] < 0, 'GHI'] = 0
    # Valid range checks
    mask = (
        (df_clean['GHI'].between(0, 1500)) &
        (df_clean['DNI'].between(0, 1500)) &
        (df_clean['DHI'].between(0, 1500))
    )
    return df_clean[mask]

def clean_weather_data(df):
    """Clean weather-related measurements."""
    mask = (
        (df['Tamb'].between(-20, 60)) &  # Temperature range
        (df['RH'].between(0, 100)) &     # Relative humidity range
        (df['WS'].between(0, 50)) &      # Wind speed range
        (df['WD'].between(0, 360))       # Wind direction range
    )
    return df[mask]

def clean_module_data(df):
    """Clean module temperature and performance data."""
    if 'ModA' in df.columns and 'ModB' in df.columns:
        mask = (
            (df['ModA'].between(-20, 90)) &  # Module temperature range
            (df['ModB'].between(-20, 90))    # Module temperature range
        )
        return df[mask]
    return df

def remove_statistical_outliers(df, columns, n_std=3):
    """Remove statistical outliers using standard deviation method."""
    df_clean = df.copy()
    for col in columns:
        mean = df_clean[col].mean()
        std = df_clean[col].std()
        df_clean = df_clean[
            (df_clean[col] >= mean - n_std * std) &
            (df_clean[col] <= mean + n_std * std)
        ]
    return df_clean

def clean_data(df):
    """Main cleaning function applying all cleaning steps."""
    # Drop rows with missing values in critical columns
    critical_columns = ['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'WD', 'RH']
    df_cleaned = df.dropna(subset=critical_columns)
    
    # Apply specific cleaning steps
    df_cleaned = clean_solar_radiation(df_cleaned)
    df_cleaned = clean_weather_data(df_cleaned)
    df_cleaned = clean_module_data(df_cleaned)
    
    # Remove statistical outliers for key measurements
    key_columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    df_cleaned = remove_statistical_outliers(df_cleaned, key_columns)
    
    # If cleaning removed all data, return original with basic cleaning
    if len(df_cleaned) == 0:
        print("Warning: Strict cleaning removed all data. Applying basic cleaning only.")
        df_cleaned = df.copy()
        df_cleaned.loc[df_cleaned['GHI'] < 0, 'GHI'] = 0
        df_cleaned = df_cleaned.dropna(subset=['GHI', 'DNI', 'DHI'])
    
    return df_cleaned