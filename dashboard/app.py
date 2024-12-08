import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils import (
    load_data, create_solar_radiation_plot, create_temp_humidity_plot,
    create_wind_rose, create_daily_pattern_plot, calculate_metrics
)

st.set_page_config(
    page_title="Solar Data Analysis Dashboard",
    page_icon="☀️",
    layout="wide"
)

def render_metrics(metrics):
    """Render metrics in columns."""
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Avg GHI (W/m²)", metrics["avg_ghi"])
    with col2:
        st.metric("Max Temperature (°C)", metrics["max_temp"])
    with col3:
        st.metric("Avg Wind Speed (m/s)", metrics["avg_wind"])
    with col4:
        st.metric("Avg Humidity (%)", metrics["avg_humidity"])

def main():
    st.title("☀️ Solar Data Analysis Dashboard")
    
    # Sidebar
    st.sidebar.header("Filters")
    country = st.sidebar.selectbox(
        "Select Country",
        ["Benin", "Sierra Leone", "Togo"]
    )
    
    try:
        df = load_data(country)
        
        # Date range filter
        min_date = df['Timestamp'].min()
        max_date = df['Timestamp'].max()
        date_range = st.sidebar.date_input(
            "Select Date Range",
            value=(min_date, min_date + timedelta(days=7)),
            min_value=min_date.date(),
            max_value=max_date.date()
        )
        
        if len(date_range) == 2:
            start_date, end_date = date_range
            mask = (df['Timestamp'].dt.date >= start_date) & (df['Timestamp'].dt.date <= end_date)
            df_filtered = df[mask]
            
            # Display metrics
            metrics = calculate_metrics(df_filtered)
            render_metrics(metrics)
            
            # Time Series Plot
            st.subheader("Solar Radiation Components Over Time")
            fig_radiation = create_solar_radiation_plot(df_filtered)
            st.plotly_chart(fig_radiation, use_container_width=True)
            
            # Temperature vs Humidity and Wind Rose
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Temperature vs Humidity")
                fig_temp_hum = create_temp_humidity_plot(df_filtered)
                st.plotly_chart(fig_temp_hum, use_container_width=True)
            
            with col2:
                st.subheader("Wind Rose")
                fig_wind = create_wind_rose(df_filtered)
                st.plotly_chart(fig_wind, use_container_width=True)
            
            # Daily Patterns
            st.subheader("Daily Patterns")
            fig_daily = create_daily_pattern_plot(df_filtered)
            st.plotly_chart(fig_daily, use_container_width=True)
            
            # Data Table
            st.subheader("Raw Data Sample")
            st.dataframe(df_filtered.head(100))
            
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please make sure to run the data analysis first to generate the cleaned data files.")

if __name__ == "__main__":
    main()