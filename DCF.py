import pandas as pd
import statsmodels.api as sm
import numpy as np


data = {
    # Historical Data
    'Year': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Revenue': [4700000, 8612000, 9081000, 9337000, 10180000, 11081000, 11401000, 12621000, 13600000, 14198000, 14539000, 16205000, 19374000, 17873000, 17859000, 18686000],
    'CapEx': [67000, 131000, 247000, 150000, 94000, 66000, 221000, 119000, 155000, 204000, 254000, 194000, 341000, 533000, 344000, 273000],
    'COGS': [0.1015, 0.4761, 0.4657, 0.4812, 0.4740, 0.4704, 0.4780, 0.5114, 0.5193, 0.4925, 0.5086, 0.5074, 0.5119, 0.5285, 0.5326, 0.5252],
    'Operating_Costs': [0.6219, 0.1758, 0.1730, 0.1414, 0.1350, 0.1214, 0.1129, 0.0930, 0.0935, 0.1189, 0.1039, 0.1031, 0.1016, 0.1084, 0.1128, 0.1078],
    'Tax_Rate': [0.0798, 0.1127, 0.0877, 0.1103, 0.1004, 0.0118, 0.1096, 0.1021, 0.0199, 0.0758, 0.0867, 0.0764, 0.1016, 0.0725, 0.0828, 0.0759],
    'Marketing': [360000, 370000, 375000, 384000, 409000, 413000, 365000, 325000, 333000, 361000, 350000, 229000, 238000, 331000, 344000, 354000],
    'M&A': [22000, 11000, 32000, 16000, 16000, 50000, 50000, 74000, 8000, 60000, 53000, 23000, 34000, 94000, 64000, 57000],
    'Interest': [68000, 150000, 176000, 215000, 211000, 232000, 204000, 205000, 184000, 203000, 205000, 205000, 212000, 292000, 292000, 382000],
   
    # Macroeconomic Indicators
    'GDP': [14.48, 15.05, 15.60, 16.25, 16.88, 17.61, 18.30, 18.80, 19.61, 20.66, 21.52, 21.32, 23.59, 25.74, 27.36, 28.30],
    'Inflation': [-0.4, 1.6, 3.2, 2.1, 1.5, 1.6, 0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8, 4.1, 3.7],
    'Fed_Rate': [0.16, 0.18, 0.1, 0.14, 0.11, 0.09, 0.13, 0.39, 1.00, 1.79, 2.16, 0.36, 0.08, 1.68, 5.03, 5.31],


    #Geopolitical Indicators
    'Geopolitics': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.692, 0.106, 0.732, 0.67, 0.018, 0.5418, 0.17, 0.4],
}


df = pd.DataFrame(data)


# Prepare independent variables (X) and dependent variable (Y)
X = df[['CapEx', 'COGS', 'Operating_Costs', 'Tax_Rate', 'Marketing', 'M&A', 'Interest', 'GDP', 'Inflation', 'Fed_Rate', 'Geopolitics']]
Y = df['Revenue']


# Add a constant for the intercept
X = sm.add_constant(X)


# Perform regression analysis
model = sm.OLS(Y, X).fit()


# Display the summary
print(model.summary())


coefficients = model.params
print(coefficients)


# Future projections for the next 15 years
future_years = 15
num_simulations = 10000  # Number of Monte Carlo Simulations
results = []


# Stochastic simulation for key factors
for i in range(num_simulations):
    future_data = []
    for i in range(1, future_years + 1):
        year = 2023 + i  # Adjust this as needed for the current year
       
        # Simulating future CapEx, COGS, Operating Costs, etc. using random growth rates
        future_capex = df['CapEx'].iloc[-1] * (1 + np.random.normal(0.05, 0.02))  # Mean growth 5%, std dev 2%
        future_cogs = df['COGS'].iloc[-1] * (1 - np.random.normal(0.01, 0.005))  # Mean decrease 1%, std dev 0.5%
        future_operating_costs = df['Operating_Costs'].iloc[-1] * (1 - np.random.normal(0.01, 0.005))  # 1% decrease
        future_tax_rate = df['Tax_Rate'].iloc[-1] * (1 - np.random.normal(0.01, 0.005))  # 1% decrease
        future_marketing = df['Marketing'].iloc[-1] * (1 + np.random.normal(0.05, 0.02))  # 5% increase
        future_ma = df['M&A'].iloc[-1] + np.random.randint(0, 5)  # Randomly adding new M&A deals
        future_interest = df['Interest'].iloc[-1] * (1 - np.random.normal(0.1, 0.05))  # 10% decrease
        future_gdp = df['GDP'].iloc[-1] * (1 + np.random.normal(0.02, 0.01))  # 2% increase
        future_inflation = df['Inflation'].iloc[-1] * (1 + np.random.normal(0.02, 0.01))  # 2% increase
        future_fed_rates = df['Fed_Rate'].iloc[-1] * (1 - np.random.normal(0.05, 0.02))  # 5% decrease
        future_geopolitics = df['Geopolitics'].iloc[-1] * (1 + np.random.normal(0.02, 0.01))  # 2% increase


        future_data.append([
            year,
            future_capex,
            future_cogs,
            future_operating_costs,
            future_tax_rate,
            future_marketing,
            future_ma,
            future_interest,
            future_gdp,
            future_inflation,
            future_fed_rates,
            future_geopolitics
        ])


    future_df = pd.DataFrame(future_data, columns=[
        'Year', 'CapEx', 'COGS', 'Operating_Costs', 'Tax_Rate',
        'Marketing', 'M&A', 'Interest', 'GDP', 'Inflation',
        'Fed_Rate', 'Geopolitics'
    ])


    # Prepare the input for the model
    future_X = sm.add_constant(future_df[['CapEx', 'COGS', 'Operating_Costs', 'Tax_Rate',
                                            'Marketing', 'M&A', 'Interest', 'GDP',
                                            'Inflation', 'Fed_Rate', 'Geopolitics']])
    future_Y = model.predict(future_X)
    results.append(future_Y)


# Convert results to DataFrame for analysis
results_df = pd.DataFrame(results).T
results_df.columns = [f'Simulation_{i + 1}' for i in range(num_simulations)]


# Analyze results
mean_projection = results_df.mean(axis=1)
lower_bound = results_df.quantile(0.05, axis=1)
upper_bound = results_df.quantile(0.95, axis=1)


# Combine results into a summary DataFrame
summary_df = pd.DataFrame({
    'Mean_Projection': mean_projection,
    'Lower_Bound': lower_bound,
    'Upper_Bound': upper_bound
})


# Display summary
print(summary_df)


# Linear OLS Regression Code
'''
for i in range(1, future_years + 1):
    year = 2025 + i  # Projections from this current year
    future_capex = df['CapEx'].iloc[-1] * (1 + 0.05)  # Assuming a 5% increase
    future_cogs = df['COGS'].iloc[-1] * (1 - 0.01)  # Assuming a 1% decrease
    future_operating_costs = df['Operating_Costs'].iloc[-1] * (1 - 0.01)  # 1% decrease
    future_tax_rate = df['Tax_Rate'].iloc[-1] * (1 - 0.01)  # 1% decrease
    future_marketing = df['Marketing'].iloc[-1] * (1 + 0.05)  # 5% increase
    future_ma = df['M&A'].iloc[-1] + 1  # Assuming one new M&A deal each year
    future_interest = df['Interest'].iloc[-1] * (1 - 0.1)  # 10% decrease
    future_gdp = df['GDP'].iloc[-1] * (1 + 0.02)  # 2% increase
    future_inflation = df['Inflation'].iloc[-1] * (1 + 0.02)  # 2% increase
    future_fed_rates = df['Fed_Rate'].iloc[-1] * (1 - .5)  # 50% decrease
    future_geopolitics = df['Geopolitics'].iloc[-1] * (1 + .2)  # 20% increase
   


    future_data.append([
        year,
        future_capex,
        future_cogs,
        future_operating_costs,
        future_tax_rate,
        future_marketing,
        future_ma,
        future_interest,
        future_gdp,
        future_inflation,
        future_fed_rates,
        future_geopolitics,
    ])


# Create a DataFrame for future projections
future_df = pd.DataFrame(future_data, columns=[
    'Year', 'CapEx', 'COGS', 'Operating_Costs',
    'Tax_Rate', 'Marketing', 'M&A', 'Interest',
    'GDP', 'Inflation', 'Fed_Rate', 'Geopolitics'
])


# Function to calculate projected revenue
def calculate_revenue(row):
    return (
        coefficients['const'] +
        coefficients['CapEx'] * row['CapEx'] +
        coefficients['COGS'] * row['COGS'] +
        coefficients['Operating_Costs'] * row['Operating_Costs'] +
        coefficients['Tax_Rate'] * row['Tax_Rate'] +
        coefficients['Marketing'] * row['Marketing'] +
        coefficients['M&A'] * row['M&A'] +
        coefficients['Interest'] * row['Interest'] +
        coefficients['GDP'] * row['GDP'] +
        coefficients['Inflation'] * row['Inflation'] +
        coefficients['Fed_Rate'] * row['Fed_Rate'] +
        coefficients['Geopolitics'] * row['Geopolitics']
    )


# Apply function to future DataFrame to calculate revenue projections
future_df['Projected_Revenue'] = future_df.apply(calculate_revenue, axis=1)


print(future_df[['Year', 'Projected_Revenue']])
'''

