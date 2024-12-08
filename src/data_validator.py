import pandas as pd
import numpy as np

def validate_data_ranges(df):
    """Validate data ranges and return validation results."""
    validations = {
        'GHI': (-10, 1500),  # Allow slight negative for sensor error
        'DNI': (0, 1500),
        'DHI': (0, 1500),
        'Tamb': (-20, 60),
        'RH': (0, 100),
        'WS': (0, 50),
        'WD': (0, 360)
    }
    
    results = {}
    for column, (min_val, max_val) in validations.items():
        if column in df.columns:
            out_of_range = ~df[column].between(min_val, max_val)
            results[column] = {
                'out_of_range_count': out_of_range.sum(),
                'percentage': (out_of_range.sum() / len(df)) * 100
            }
    
    return results

def check_data_consistency(df):
    """Check data consistency and relationships."""
    checks = {
        'GHI_vs_components': (df['GHI'] >= (df['DNI'] + df['DHI'])).sum(),
        'temp_vs_humidity': ((df['Tamb'] > 40) & (df['RH'] > 90)).sum(),
        'wind_direction': (df['WD'] < 0).sum() + (df['WD'] > 360).sum()
    }
    return checks

def generate_validation_report(df):
    """Generate a comprehensive validation report."""
    report = {
        'missing_values': df.isnull().sum().to_dict(),
        'range_validations': validate_data_ranges(df),
        'consistency_checks': check_data_consistency(df),
        'total_rows': len(df),
        'valid_rows': len(df.dropna())
    }
    return report