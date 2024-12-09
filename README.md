# Solar Radiation Analysis for MoonLight Energy Solutions

## Project Overview

This project aims to analyze solar radiation data from three countries (Benin, Sierra Leone, and Togo) to support MoonLight Energy Solutions in developing a strategic approach for enhancing operational efficiency and sustainability through targeted solar investments. As an Analytics Engineer, our task was to perform a comprehensive analysis of environmental measurements provided by the engineering team and translate observations into a strategic report.

## Methodology

Our analysis followed these key steps:

1. **Data Loading and Cleaning**: We loaded data from three CSV files, one for each country. We performed initial data cleaning, including handling missing values and removing outliers.

2. **Exploratory Data Analysis (EDA)**: We conducted a thorough EDA to understand the data distribution, identify patterns, and uncover relationships between variables.

3. **Statistical Analysis**: We performed various statistical analyses to derive meaningful insights from the data.

4. **Visualization**: We created multiple visualizations to represent our findings effectively.

5. **Dashboard Creation**: We developed an interactive Streamlit dashboard to present our results in a user-friendly manner.

## Key Findings

### 1. Solar Radiation Patterns

- **Daily Patterns**: All three countries show a clear daily pattern in solar radiation, with peaks around midday and lows during night hours.
- **Seasonal Variations**: We observed seasonal variations in solar radiation, with higher levels during summer months and lower levels during winter months.
- **Country Comparisons**: Togo generally showed higher average solar radiation levels compared to Benin and Sierra Leone.

### 2. Temperature and Humidity Effects

- There's a strong positive correlation between temperature and solar radiation (GHI, DNI, DHI).
- Humidity shows a negative correlation with solar radiation, suggesting that higher humidity levels might reduce solar energy potential.

### 3. Wind Patterns

- Wind speed and direction vary significantly between the three countries.
- Togo shows the most consistent wind patterns, which could be beneficial for potential wind energy projects.

### 4. Cleaning Impact

- Regular cleaning of solar panels (indicated by the 'Cleaning' column) shows a noticeable improvement in module efficiency (ModA and ModB readings).

### 5. Data Quality

- We identified and addressed several data quality issues, including missing values and outliers, particularly in the wind speed and solar radiation measurements.

## Visualizations

1. **Time Series Analysis**: 
   ![Time Series of GHI](GHI_time_series.png)
   This plot shows the Global Horizontal Irradiance (GHI) over time, highlighting daily and seasonal patterns.

2. **Correlation Heatmap**:
   ![Correlation Heatmap](correlation_matrix.png)
   This heatmap visualizes the correlations between key variables, helping identify strong relationships.

3. **Wind Rose**:
   ![Wind Rose](wind_rose.png)
   The wind rose plot shows the distribution of wind speed and direction, crucial for understanding wind patterns.

4. **Bubble Chart**:
   ![Bubble Chart](bubble_chart.png)
   This chart explores the relationship between GHI, temperature, humidity, and wind speed.

## Recommendations

Based on our analysis, we recommend the following strategies for MoonLight Energy Solutions:

1. **Optimal Locations**: Focus solar installations in areas of Togo that showed consistently high GHI levels. These locations are likely to yield the highest solar energy potential.

2. **Seasonal Planning**: Plan for seasonal variations in energy production. Consider complementary energy sources or storage solutions to maintain consistent energy supply during lower solar radiation periods.

3. **Cleaning Schedule**: Implement a regular cleaning schedule for solar panels. Our analysis shows that regular cleaning significantly improves module efficiency.

4. **Wind Energy Potential**: Explore the possibility of wind energy projects in Togo, where wind patterns are most consistent. This could provide a complementary energy source to solar.

5. **Humidity Considerations**: In high humidity areas, consider using solar panel technologies that perform better in humid conditions. Also, factor in the negative impact of humidity on solar radiation when estimating energy production.

6. **Data Collection Improvements**: Enhance data collection processes to reduce missing values and outliers, particularly for wind speed and solar radiation measurements. This will improve the accuracy of future analyses and predictions.

7. **Continuous Monitoring**: Implement a system for continuous monitoring of environmental factors. This will allow for real-time adjustments and long-term strategy refinement.

## Future Work

To further enhance this analysis, we suggest:

1. Incorporating more granular geographical data to pinpoint optimal locations for solar installations.
2. Conducting a detailed economic analysis to assess the return on investment for solar projects in different areas.
3. Exploring machine learning models for predicting solar radiation levels based on other environmental factors.
4. Analyzing the impact of cloud cover and air quality on solar radiation, if such data becomes available.

## Conclusion

This analysis provides MoonLight Energy Solutions with data-driven insights to guide their solar investment strategy. By focusing on high-potential areas, optimizing maintenance schedules, and considering complementary energy sources, the company can significantly enhance its operational efficiency and sustainability. The interactive dashboard we've created will allow for ongoing exploration of the data, supporting adaptive decision-making as new data becomes available.

## Deployed Streamlit dashboard
You can access the deployed Streamlit dashboard at the following URL:

[Streamlit Dashboard(https://solar-10academy.streamlit.app/)

