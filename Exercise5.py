# -*- coding: utf-8 -*-
###########
#Problem 1#
###########
import pandas as pd
fp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\6153237444115dat.csv'

dataFrame = pd.read_csv(fp, sep=',', na_values=['*', '**', '***', '****', '*****', '******'])


print("There are", len(dataFrame), "rows")
print("The columns are \n", dataFrame.columns)
print("The column's datatypes are \n", dataFrame.dtypes)


temp_mean = dataFrame['TEMP'].mean()
temp_max_std = dataFrame['MAX'].std()
station_count = len(dataFrame['USAF'].unique())

print("Mean temperature in Fahrenheit is ", round(temp_mean,1))
print("Standard deviation of maximum temperature is ", round(temp_max_std, 1))
print("The number of unique stations is ", station_count)