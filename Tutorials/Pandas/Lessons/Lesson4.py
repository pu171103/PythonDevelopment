###############################################################################
###  Pandas Tutorials - Lesson 4                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/04%20-%20Lesson.ipynb
import pandas as pd

# Make some data
d = [0,1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d)
df.columns = ['Rev']

# Passing scalar to new col will fill value
df['NewCol'] = 5

# Can modify columns in place
df['NewCol'] = df['NewCol'] + 1

# Delete columns
del df['NewCol']

df['test'] = 3
df['col'] = df['Rev']

# Modify index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index=i

# Subset by named indices with .loc()
df.loc['a']
df.loc['a':'d']
df.loc['a':'d'][['Rev', 'test']]

# Subset by coordinate position with .iloc()
df.iloc[0:3]

# Can pass values of index positions with named column indices
df.loc[df.index[0:3], 'Rev']
df.loc[df.index[5: ], 'col']
df.loc[df.index[ :3], ['col', 'test']]


