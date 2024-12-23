import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', marker='o') 
    # Add titles and labels 
    plt.title('Sample Scatter Plot') 
    plt.xlabel('Year') 
    plt.ylabel('CSIRO Adjusted Sea Level') 
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    # Extend the line to the year 2050 
    years_extended = pd.Series(range(1880, 2051)) 
    sea_levels_predicted = slope * years_extended + intercept 
    # Plot the line of best fit 
    plt.plot(years_extended, sea_levels_predicted, color='red', label='Best Fit Line') 
    plt.legend() 

    # Create second line of best fit
    # Filter data from 2000 onwards 
    data_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    # Extend the line to the year 2050 
    years_extended_2000 = pd.Series(range(2000, 2051)) 
    sea_levels_predicted_2000 = slope_2000 * years_extended_2000 + intercept_2000 
    # Plot the line of best fit 
    plt.plot(years_extended_2000, sea_levels_predicted_2000, color='green', label='second best Fit Line') 
    plt.legend() 

    # Add labels and title
    plt.xlabel('Year') 
    plt.ylabel('Sea Level (inches)') 
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
