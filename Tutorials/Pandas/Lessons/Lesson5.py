###############################################################################
###  Pandas Tutorials - Lesson 5                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/05%20-%20Lesson.ipynb

import pandas as pd

# Working with stack and unstack functions ####################################

d = {'one': [1, 1], 'two': [2, 2]}
i = ['a', 'b']
df=pd.DataFrame(data=d, index=i)

# Add columns as lower level index 
stack = df.stack()
stack.index

# Add columns as higher level index
unstack = df.unstack()
unstack.index

# Inverse operations, but you can't stack a vector
# You can UNstack a vector with an index
stack.unstack()
unstack.stack()

# Transpose function
transpose = df.T

