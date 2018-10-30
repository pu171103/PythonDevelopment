###############################################################################
###  Pandas Tutorials - Lesson 1                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb

# Import all libraries needed for tutorial
import sys
import matplotlib
import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv

# Enable inline plotting for notebooks
# %matplotlib inline

print("Python version " + sys.version)
print("Pandas version" + pd.__version__)
print("Matplotlib version " + matplotlib.__version__)

# Create Some Data ############################################################


names = ["Bob", "Jessica", "Mary", "John", "Mel"]
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births))

df = pd.DataFrame(data=BabyDataSet, columns=["Names", "Births"])

# CSV Import / Export
Location = r'C:\Users\pu171\PythonDevelopment\Tutorials\Pandas\Lessons\births1880.csv'
df.to_csv(Location, index=False, header=False)
df = pd.read_csv(Location)

# Need to specify no header and provide column names
df = pd.read_csv(Location, header=None)
df = pd.read_csv(Location, names=["Names", "Births"])
os.remove(Location)  # Script-Shell interface

# Prepare Data ################################################################

# Check data type of columns
df.dtypes
df.Births.dtype

# Analyze Data ################################################################

# Method 1
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)

# Method 2
df['Births'].max()

# Present Data ################################################################

# Create graph object and then display it
df['Births'].plot()
plt.show()  # Shows last created graph w/no arg

# Annotate the max value
df['Births'].plot()
MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
Text = str(MaxValue) + " - " + MaxName
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
             xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.show()
