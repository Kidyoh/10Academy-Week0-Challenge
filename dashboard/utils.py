import pandas as pd
import plotly.express as px
from datetime import timedelta

def load_data(country):
    """Load cleaned data for a specific country."""
    try:
        file_path = f'../outputs/{country}/{country}_cleaned_data.csv'
        df = pd.read_csv(file_path, parse_dates=['Timestamp'])
        return df
    except Exception as e:
        raise Exception(f"Error loading data for {country}: {str(e)}")

def create_solar_radiation_plot(df):
    """Create solar radiation components plot."""
    return px.line(df, x='Timestamp', 
                  y=['GHI', 'DNI', 'DHI'],
                  title="Solar Radiation Components")

def create_temp_humidity_plot(df):
    """Create temperature vs humidity scatter plot."""
    return px.scatter(df, x='Tamb', y='RH',
                     color='GHI',
                     title="Temperature vs Humidity (colored by GHI)")

def create_wind_rose(df):
    """Create wind rose plot."""
    return px.scatter_polar(df, r='WS', theta='WD',
                          color='WS',
                          title="Wind Speed and Direction")

def create_daily_pattern_plot(df):
    """Create daily pattern analysis plot."""
    df = df.copy()
    df['Hour'] = df['Timestamp'].dt.hour
    hourly_avg = df.groupby('Hour')['GHI'].mean().reset_index()
    return px.line(hourly_avg, x='Hour', y='GHI',
                  title="Average Daily Solar Radiation Pattern")

def calculate_metrics(df):
    """Calculate key metrics from the data."""
    return {
        "avg_ghi": f"{df['GHI'].mean():.2f}",
        "max_temp": f"{df['Tamb'].max():.2f}",
        "avg_wind": f"{df['WS'].mean():.2f}",
        "avg_humidity": f"{df['RH'].mean():.2f}"
    }