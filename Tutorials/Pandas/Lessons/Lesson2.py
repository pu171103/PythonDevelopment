###############################################################################
###  Pandas Tutorials - Lesson 2                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

# Create Data #################################################################

# Generate a list of 1000 randomly sampled baby names and birth counts
names = ["Bob", "Jessica", "Mary", "John", "Mel"]
random.seed(500)

random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]
births = [random.randint(low=0, high=1000) for i in range(1000)]

BabyDataSet = list(zip(random_names, births))

df = pd.DataFrame(data=BabyDataSet, columns=["Names", "Births"])

# Assorted summary methods
df.info()
df.head()
df.tail()
df.head(15)

# Prepare Data ################################################################

# Finding unique values
# Method 1
df['Names'].unique()
[x for x in df['Names'].unique()]
for x in df['Names'].unique():
    print(x)

# Method 2
df['Names'].describe()

# Sum over names
# We can create a 'groupby' object to do convenient aggregation
name = df.groupby('Names')
df = name.sum()

# Present Data ################################################################

# Create bar chart
df['Births'].plot.bar()
plt.show()
df.sort_values(by='Births', ascending=False)
