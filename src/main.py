import os
from data_loader import load_data, data_quality_check
from data_cleaner import clean_data
from data_validator import generate_validation_report
from analysis import summary_statistics, cleaning_impact_analysis, correlation_analysis
from visualization import (
    time_series_analysis, create_correlation_heatmap, wind_analysis,
    temperature_humidity_analysis, create_histograms, bubble_chart
)

def process_dataset(country, file_path, output_dir):
    """Process a single dataset with validation and cleaning."""
    print(f"\nProcessing data for {country}")
    
    # Load data
    df = load_data(file_path)
    
    # Validate data
    validation_report = generate_validation_report(df)
    print("\nValidation Report:")
    print(validation_report)
    
    # Clean data
    df_cleaned = clean_data(df)
    
    # Generate analysis and visualizations
    print("\nGenerating analysis and visualizations...")
    
    # Create visualizations
    for column in ['GHI', 'DNI', 'DHI', 'Tamb']:
        time_series_analysis(df_cleaned, column, f'{column} in {country}', output_dir)
    
    correlation_matrix = correlation_analysis(
        df_cleaned, 
        ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    )
    create_correlation_heatmap(correlation_matrix, output_dir)
    
    wind_analysis(df_cleaned, output_dir)
    temperature_humidity_analysis(df_cleaned, output_dir)
    create_histograms(df_cleaned, ['GHI', 'DNI', 'DHI', 'WS', 'Tamb'], output_dir)
    bubble_chart(df_cleaned, output_dir)
    
    # Save cleaned data
    cleaned_file_path = os.path.join(output_dir, f'{country}_cleaned_data.csv')
    df_cleaned.to_csv(cleaned_file_path, index=False)
    
    print(f"\nResults for {country}:")
    print(f"Original data shape: {df.shape}")
    print(f"Cleaned data shape: {df_cleaned.shape}")
    print(f"Cleaned data saved to: {cleaned_file_path}")

def main():
    datasets = {
        'Benin': './data/benin-malanville.csv',
        'Sierra Leone': './data/sierraleone-bumbuna.csv',
        'Togo': './data/togo-dapaong_qc.csv'
    }

    output_base_dir = './outputs'
    os.makedirs(output_base_dir, exist_ok=True)

    for country, file_path in datasets.items():
        country_output_dir = os.path.join(output_base_dir, country)
        os.makedirs(country_output_dir, exist_ok=True)
        process_dataset(country, file_path, country_output_dir)

if __name__ == "__main__":
    main()