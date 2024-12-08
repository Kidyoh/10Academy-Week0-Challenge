import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def time_series_analysis(df, column, title, output_dir):
    """Create time series plot for specified column."""
    plt.figure(figsize=(15, 5))
    plt.plot(df['Timestamp'], df[column])
    plt.title(f'{title} Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{column}_time_series.png')
    plt.close()

def create_correlation_heatmap(correlation_matrix, output_dir):
    """Create and save correlation heatmap."""
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlation_matrix.png')
    plt.close()

def wind_analysis(df, output_dir):
    """Create wind rose plot."""
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, projection='polar')
    wind_direction_rad = df['WD'] * np.pi / 180
    ax.scatter(wind_direction_rad, df['WS'], alpha=0.5)
    plt.title('Wind Rose - Speed and Direction')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/wind_rose.png')
    plt.close()

def temperature_humidity_analysis(df, output_dir):
    """Create temperature vs humidity scatter plot."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Tamb', y='RH', data=df, hue='GHI', palette='viridis')
    plt.title('Temperature vs Relative Humidity (color: GHI)')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Relative Humidity (%)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/temp_humidity_ghi.png')
    plt.close()

def create_histograms(df, columns, output_dir):
    """Create histograms for specified columns."""
    for column in columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{column}_histogram.png')
        plt.close()

def bubble_chart(df, output_dir):
    """Create bubble chart for multiple variables."""
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['Tamb'], df['GHI'], s=df['RH'], c=df['WS'], 
                         cmap='viridis', alpha=0.6)
    plt.colorbar(scatter, label='Wind Speed (m/s)')
    plt.title('GHI vs Temperature vs Humidity vs Wind Speed')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Global Horizontal Irradiance (W/m²)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/bubble_chart.png')
    plt.close()