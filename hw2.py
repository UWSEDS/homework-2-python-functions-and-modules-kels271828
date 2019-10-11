# CSE 583 Homework 2

import pandas as pd
import numpy as np

# Write a python script that creates a dataframe form a URL that points to a CSV file such as 
# the pronto data or CSVs in data.gov.

# The following works in the notebook, but not in a script... 
# Wait for them to talk about this in lecture...
!curl -o pronto.csv https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD
df = pd.read_csv('pronto.csv')
df.head()

# Create the function test_create_dataframe() that takes as input: 
#   (a) a pandas DataFrame
#   (b) a list of column names
#
# The function returns True if the following conditions hold:
#   * The DataFrame contains only the columns that you specified as the second argument
#   * The values in each column have the same python type 
#   * There are at least 10 rows in the DataFrame 
def test_create_dataframe(df,col_names):

    # Check columns
    if set(col_names) != set(df.columns):
        print('Incorrect column names')
        return False

    # Check types
    if len(set(df.dtypes)) > 1:
        print('Incorrect types')
        return False

    # Check length
    if len(df) < 10:
        print('Incorrect length')
        return False

    return True

test_create_dataframe(df,df.columns)

df2 = df[['starttime','stoptime','bikeid','from_station_name']]
test_create_dataframe(df2,df2.columns)

test_create_dataframe(df2,df2.columns.values[0:2])

col_names = df2.columns.to_list()
col_names.append('kelsey')
test_create_dataframe(df2,col_names)

df3 = df2.loc[0:4,:]
test_create_dataframe(df3,df3.columns)
