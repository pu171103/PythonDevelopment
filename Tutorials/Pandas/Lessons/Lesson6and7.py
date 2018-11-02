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




