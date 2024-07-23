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


del_work1 = del_work.groupby(['Series_reference', 'Period_year'])['Data_value'].max()
print(del_work1)

mapping_dict = {}
for i , v in del_work1.items():
    
    if i[0] in mapping_dict.keys():
        if v > mapping_dict[i[0]]['Data_value'] :
            mapping_dict[i[0]]['Period'] = i[1]
            mapping_dict[i[0]]['Data_value'] = v
    else :
        mapping_dict[i[0]] = {}
        mapping_dict[i[0]]['Period'] =  i[1] 
        mapping_dict[i[0]]['Data_value'] = v
        
# convert dictionary in to data frame
max_sale_year = pd.DataFrame.from_dict(mapping_dict, orient='index', columns=['Period', 'Data_value'])

print(max_sale_year.describe)
    
