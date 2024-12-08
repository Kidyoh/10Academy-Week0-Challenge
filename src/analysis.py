import pandas as pd
import numpy as np

def summary_statistics(df):
    """Calculate summary statistics for the dataset."""
    return df.describe()

def cleaning_impact_analysis(df):
    """Analyze the impact of cleaning on module temperatures."""
    return df.groupby('Cleaning')[['ModA', 'ModB']].mean()

def correlation_analysis(df, columns):
    """Calculate correlation matrix for specified columns."""
    return df[columns].corr()