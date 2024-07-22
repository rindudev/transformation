import pandas as pd
import numpy as np
path = "C:\\Users\\rindu\\workingspace\\transformation\\machine-readable-business-employment-data-mar-2024-quarter.csv"
work = pd.read_csv(path, delimiter=",")
print(work.head()) 
del_work = work.drop(['Series_title_4', 'Series_title_5', 'Suppressed'], axis=1)
print(del_work.head())

# we need to convert float to a string 
del_work['Period'] = del_work['Period'].astype(str) 
#  you need split column name period
del_work['Period_year'] = del_work['Period'].str.split('.').str[0]

print(del_work[['Period', 'Period_year', 'Series_reference', 'Data_value']])

