###############################################################################
###  Pandas Tutorials - Lesson 6 & 7                                        ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/06%20-%20Lesson.ipynb
# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/06%20-%20Lesson.ipynb

# The groupby() function ######################################################

import pandas as pd

d = {'one': [1, 1, 1, 1, 1],
     'two': [2, 2, 2, 2, 2],
     'letter': ['a', 'a', 'b', 'b', 'c']}
df = pd.DataFrame(d)

# One level of aggregation
one = df.groupby('letter')
one.sum()

# Multiple levels of aggregation
letterone = df.groupby(['letter', 'one']).sum()
letterone.index

# Using groupby() without moving cols to index
# NOTE: This will overwrite columns in place
letterone = df.groupby(['letter', 'one'], as_index=False).sum()

# Calculating outliers ########################################################

States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States

data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States

df = pd.concat([df1, df2])

# Method 1
# newdf = df would assign newdf and df to the same object on the heap
newdf = df.copy()

newdf['x-Mean'] = abs(newdf['Revenue'] - newdf['Revenue'].mean())
newdf['1.96*std'] = 1.96 * newdf['Revenue'].std()
newdf['Outlier'] = abs(
    newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()

# Method 2 : Group by item
newdf = df.copy()
State = newdf.groupby('State')

newdf['Outlier'] = State.transform(
    lambda x: abs(x - x.mean()) > 1.96 * x.std())
newdf['x-Mean'] = State.transform(lambda x: abs(x - x.mean()))
newdf['1.96*std'] = State.transform(lambda x: 1.96 * x.std())

# Method 2: Group by multiple items
newdf = df.copy()
StateMonth = newdf.groupby(['State', lambda x: x.month])

newdf['Outlier'] = StateMonth.transform(
    lambda x: abs(x - x.mean()) > 1.96 * x.std())
newdf['x-Mean'] = StateMonth.transform(lambda x: abs(x-x.mean()))
newdf['1.96*std'] = StateMonth.transform(lambda x: 1.96 * x.std())

# Method 3: Group by item
State = df.copy().groupby('State')


def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96 * group['Revenue'].std()
    group['Outlier'] = abs(
        group['Revenue'] - group['Revenue'].mean()) > 1.96 * group['Revenue'].std()

    return group

Newdf2 = State.apply(s)