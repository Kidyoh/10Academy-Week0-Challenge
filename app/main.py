import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import BytesIO

# Load the data
@st.cache_data
def load_data(country):
    return pd.read_csv(f'outputs/{country}/{country}_cleaned_data.csv', parse_dates=['Timestamp'])

# Create time series plot
def plot_time_series(df, column):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Timestamp'], df[column])
    ax.set_title(f'{column} Over Time')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(column)
    plt.xticks(rotation=45)
    return fig

# Create correlation heatmap
def plot_correlation(df, columns):
    correlation_matrix = df[columns].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix')
    return fig

# Create wind rose
def plot_wind_rose(df):
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    ax.bar(df['WD'] * np.pi / 180, df['WS'], bins=16)
    ax.set_title('Wind Rose - Speed and Direction')
    return fig

# Create bubble chart
def plot_bubble_chart(df):
    fig, ax = plt.subplots(figsize=(12, 8))
    scatter = ax.scatter(df['Tamb'], df['GHI'], s=df['RH'], c=df['WS'], cmap='viridis', alpha=0.6)
    plt.colorbar(scatter, label='Wind Speed (m/s)')
    ax.set_title('GHI vs Temperature vs Humidity vs Wind Speed')
    ax.set_xlabel('Ambient Temperature (°C)')
    ax.set_ylabel('Global Horizontal Irradiance (W/m²)')
    return fig

# Streamlit app
st.title('Solar Radiation Analysis Dashboard')

# Sidebar for country selection
country = st.sidebar.selectbox('Select Country', ['Benin', 'Sierra Leone', 'Togo'])

# Load data for selected country
df = load_data(country)

st.header(f'Solar Radiation Analysis for {country}')

# Display summary statistics
st.subheader('Summary Statistics')
st.write(df.describe())

# Time series analysis
st.subheader('Time Series Analysis')
column = st.selectbox('Select variable for time series', ['GHI', 'DNI', 'DHI', 'Tamb'])
st.pyplot(plot_time_series(df, column))

# Correlation analysis
st.subheader('Correlation Analysis')
correlation_columns = st.multiselect('Select variables for correlation analysis', 
                                     ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD'],
                                     default=['GHI', 'DNI', 'DHI', 'TModA', 'TModB'])
if correlation_columns:
    st.pyplot(plot_correlation(df, correlation_columns))

# Wind analysis
st.subheader('Wind Analysis')
st.pyplot(plot_wind_rose(df))

# Temperature, Humidity, and Solar Radiation Analysis
st.subheader('Temperature, Humidity, and Solar Radiation Analysis')
st.pyplot(plot_bubble_chart(df))

# Data quality information
st.subheader('Data Quality Information')
missing_values = df.isnull().sum()
st.write('Missing Values:')
st.write(missing_values[missing_values > 0])

# Download cleaned data
st.subheader('Download Cleaned Data')
csv = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name=f'{country}_cleaned_data.csv',
    mime='text/csv',
)

