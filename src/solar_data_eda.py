from scipy.stats import zscore
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Timestamp'])

def summary_statistics(df):
    return df.describe()

def data_quality_check(df):
    missing_values = df.isnull().sum()
    negative_values = df.select_dtypes(include=[np.number]).lt(0).sum()
    return missing_values, negative_values

def time_series_analysis(df, column, title, output_dir):
    plt.figure(figsize=(15, 5))
    plt.plot(df['Timestamp'], df[column])
    plt.title(f'{title} Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{column}_time_series.png')
    plt.close()

def cleaning_impact_analysis(df):
    cleaning_impact = df.groupby('Cleaning')[['ModA', 'ModB']].mean()
    return cleaning_impact

def correlation_analysis(df, columns, output_dir):
    correlation_matrix = df[columns].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlation_matrix.png')
    plt.close()
    return correlation_matrix

def wind_analysis(df, output_dir):
    # Create a polar plot for wind analysis
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, projection='polar')
    
    # Convert wind direction to radians
    wind_direction_rad = df['WD'] * np.pi / 180
    
    # Use a scatter plot to represent wind direction and speed
    scatter = ax.scatter(wind_direction_rad, df['WS'], alpha=0.5)
    
    plt.title('Wind Rose - Speed and Direction')
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(f'{output_dir}/wind_rose.png')
    plt.close()

def temperature_humidity_analysis(df, output_dir):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Tamb', y='RH', data=df, hue='GHI', palette='viridis')
    plt.title('Temperature vs Relative Humidity (color: GHI)')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Relative Humidity (%)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/temp_humidity_ghi.png')
    plt.close()

def create_histograms(df, columns, output_dir):
    for column in columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{column}_histogram.png')
        plt.close()

def z_score_analysis(df, column):
    z_scores = zscore(df[column])
    outliers = np.abs(z_scores) > 3
    return outliers.sum()

def bubble_chart(df, output_dir):
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['Tamb'], df['GHI'], s=df['RH'], c=df['WS'], cmap='viridis', alpha=0.6)
    plt.colorbar(scatter, label='Wind Speed (m/s)')
    plt.title('GHI vs Temperature vs Humidity vs Wind Speed')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Global Horizontal Irradiance (W/m²)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/bubble_chart.png')
    plt.close()

def clean_data(df):
    # Remove rows with missing values
    df_cleaned = df.dropna()
    
    # Remove outliers using IQR method
    Q1 = df_cleaned.quantile(0.25)
    Q3 = df_cleaned.quantile(0.75)
    IQR = Q3 - Q1
    df_cleaned = df_cleaned[~((df_cleaned < (Q1 - 1.5 * IQR)) | (df_cleaned > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    return df_cleaned

def main():
    datasets = {
        'Benin': './data/benin-malanville.csv',
        'Sierra Leone': './data/sierraleone-bumbuna.csv',
        'Togo': './data/togo-dapaong_qc.csv'
    }

    output_base_dir = './outputs'

    for country, file_path in datasets.items():
        print(f"\nAnalyzing data for {country}")
        df = load_data(file_path)
        
        # Create a directory for each country
        output_dir = os.path.join(output_base_dir, country)
        os.makedirs(output_dir, exist_ok=True)
        
        print("Summary Statistics:")
        print(summary_statistics(df))
        
        missing_values, negative_values = data_quality_check(df)
        print("\nMissing Values:")
        print(missing_values)
        print("\nNegative Values:")
        print(negative_values)
        
        for column in ['GHI', 'DNI', 'DHI', 'Tamb']:
            time_series_analysis(df, column, f'{column} in {country}', output_dir)
        
        print("\nCleaning Impact Analysis:")
        print(cleaning_impact_analysis(df))
        
        correlation_matrix = correlation_analysis(df, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD'], output_dir)
        plt.savefig(f'{output_dir}/correlation_matrix.png')
        
        wind_analysis(df, output_dir)
        
        temperature_humidity_analysis(df, output_dir)
        
        create_histograms(df, ['GHI', 'DNI', 'DHI', 'WS', 'Tamb'], output_dir)
        for column in ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']:
            outliers = z_score_analysis(df, column)
            print(f"\nNumber of outliers in {column}: {outliers}")
        
        bubble_chart(df, output_dir)
        
        df_cleaned = clean_data(df)
        print(f"\nOriginal data shape: {df.shape}")
        print(f"Cleaned data shape: {df_cleaned.shape}")
        
        # Save cleaned data
        df_cleaned.to_csv(f'{output_dir}/{country}_cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()

