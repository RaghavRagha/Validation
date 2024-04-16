'''Commanads to install required modules
pip install pandas openpyxl'''

import pandas as pd 

'''Reading the json file (Assuming that the json file has only one array/ root). If we have 
nested arrays then we have to loop those arrays to get the data out of json'''
data = pd.read_json("Data.json")

'''The below is the simple logic to split the passed and failed test cases. If there are complicated
conditions then we can go with the normal if else, which will require traditional loop method to achieve that.'''

# Getting the test cases which were successful
passed = data[
            (data['status'] == 'pass') &
            (data['bug_count'] == 0) 
            # & (data['response_time'] <= 100)  # more conditions
            # & (data['valid_credentials'] == True) # more conditions
            ]

# Getting the test cases which are not present in passed dataframe which is basically failed test cases.
failed = data[~data.index.isin(passed.index)]

# After spliting the passed and failed test case, loading both the dataframe into diffeent excel files.
passed.to_excel("Passed.xlsx",sheet_name="Passed",engine="openpyxl",index=False)
failed.to_excel("Failed.xlsx",sheet_name="Failed",engine="openpyxl",index=False)