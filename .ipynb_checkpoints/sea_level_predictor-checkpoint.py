import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    df = pd.DataFrame(data)

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'], label = 'scatter origin')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    years = df['Year'].tolist() + [2050]
    seaLevels = [slope * year + intercept for year in years]
    plt.plot(years, seaLevels, 'r', label = 'Line of Best Fit')
    
    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    mostRecentYear = df_filtered.max()
    slope_filtered, intercept_filtered, rvalue_filtered, pvalue_filtered, stderr_filtered = linregress(x=df_filtered['Year'], y=df_filtered['CSIRO Adjusted Sea Level'])
    years_filtered = df_filtered['Year'].tolist() + [2050]
    sea_levels_filtered = [slope_filtered * year + intercept_filtered for year in years_filtered]
    plt.plot(years_filtered, sea_levels_filtered, 'g', label='Line of Best Fit (2000-Present)')

    # Add labels and title
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()