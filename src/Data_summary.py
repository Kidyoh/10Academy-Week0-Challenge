import pandas as pd
import numpy as np
import os

def analyze_country_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate key metrics
    summary = {
        'avg_ghi': df['GHI'].mean(),
        'max_ghi': df['GHI'].max(),
        'avg_temp': df['Tamb'].mean(),
        'avg_humidity': df['RH'].mean(),
        'avg_wind_speed': df['WS'].mean(),
        'data_points': len(df)
    }
    
    # Calculate correlation between GHI and temperature
    summary['ghi_temp_corr'] = df['GHI'].corr(df['Tamb'])
    
    # Calculate percentage of time with high GHI (above 500 W/m²)
    summary['high_ghi_percentage'] = (df['GHI'] > 500).mean() * 100
    
    return summary

# Analyze data for each country
countries = ['Benin', 'Sierra Leone', 'Togo']
results = {}

for country in countries:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, f'../outputs/{country}/{country}_cleaned_data.csv')
    results[country] = analyze_country_data(file_path)

# Print results
for country, data in results.items():
    print(f"\nSummary for {country}:")
    for key, value in data.items():
        print(f"{key}: {value:.2f}")

