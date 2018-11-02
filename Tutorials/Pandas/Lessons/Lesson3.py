###############################################################################
###  Pandas Tutorials - Lesson 3                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/03%20-%20Lesson.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import matplotlib

np.seed(111)

#  Create some data ###########################################################


def CreateDataSet(Number=1):
    """Convenience function for data generation.

    Keyword Arguments:
        Number {int} -- Number of cases. (default: {1})
    """
    Output = []

    for i in range(Number):

        # Create a weekly (Mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1, 2, 3]

        # Make a random list of statuses
        random_status = [
            status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ["GA", "FL", "fl", "NY", "NJ", "TX"]

        # Make a random list of states
        random_states = [
            states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output


dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=[
                  "State", "Status", "CustomerCount", "StatusDate"])
df.info()

# Working with Excel-if you have to ###########################################

df.to_excel('.\\Tutorials\\Pandas\\Lessons\\Lesson3.xlsx', index=False)

# Parse a specific sheet
df = pd.read_excel(
    '.\\Tutorials\\Pandas\\Lessons\\Lesson3.xlsx', 0, index_col='StatusDate')
df.dtypes
df.index
df.head()

# Cleaning data ###############################################################

# Convert all state names to uppercase
df['State'].unique()
df['State'] = df.State.apply(lambda x: x.upper())

# Filter to only where status == 1
mask = df['Status'] == 1
df = df[mask]

# Recode 'NJ' to 'NY'
mask = df.State == 'NJ'
df['State'][mask] = 'NY'

# Lineplot to check data consistency
df['CustomerCount'].plot(figsize=(15, 5))
plt.show()

# Group by State and StatusDate
# Use 'reset.index()' to restore date as a regular column
# Groupby columns will become indices
Daily = df.reset_index().groupby(['State', 'StatusDate']).sum()
Daily.head()

# We know all Status == 1, so drop the column
del Daily['Status']
Daily.index
Daily.index.levels[0]

# Small multiples on State
# plt.show() will show all unprinted plots in memory
Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot()
plt.show()

# Plot subset data
Daily.loc['FL']['2012'].plot()
Daily.loc['GA']['2012'].plot()
Daily.loc['NY']['2012'].plot()
Daily.loc['TX']['2012'].plot()
plt.show()

# Define outliers by percentile deviation from customer count / month
# .groupby() aggregates, .transform() does linear transformations
# .transform() useful for creating derrived variables
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0),
                                Daily.index.get_level_values(1).year,
                                Daily.index.get_level_values(1).month])

# Thresholds: 1.5 IQR above 75th and 1.5 IQR below 25th
# Does pandas have an analog to R's 'with()'?
Daily['Lower'] = StateYearMonth['CustomerCount'].transform(
    lambda x: x.quantile(q=.25) - (1.5 * x.quantile(q=.75) - x.quantile(q=.25)))
Daily['Upper'] = StateYearMonth['CustomerCount'].transform(
    lambda x: x.quantile(q=.75) + (1.5 * x.quantile(q=.75) - x.quantile(q=.25)))
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (
    Daily['CustomerCount'] > Daily['Upper'])

# Drop outliers
Daily = Daily[Daily['Outlier'] == False]

# Max customer count by date, group by year, month
All = pd.DataFrame(Daily['CustomerCount'].groupby(
    Daily.index.get_level_values(1)).sum())
YearMonth = All.groupby([lambda x: x.year, lambda x: x.month])
All['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())

# Compare to some sales goal (BHAG)
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=["BHAG"])

# Combining dataframes, axis=0 for row-wise join
combined = pd.concat([All, BHAG], axis=0)

# Plot multiple series
fig, axes = plt.subplots(figsize=(12,7))  # Define layout
combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best')
plt.show()

# Forecast and visualize ######################################################

