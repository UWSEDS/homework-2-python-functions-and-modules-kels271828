# CSE 583 Homework 2

import pandas as pd
import numpy as np

# Write a python script that creates a dataframe form a URL that points to a CSV file such as 
# the pronto data or CSVs in data.gov.

url = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

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
        return False

    # Check types
    for col in df.columns:
        type_set = set([type(entry) for entry in df[col].to_list()])
        if len(type_set) > 1:
            return False

    # Check length
    if len(df) < 10:
        return False

    return True
