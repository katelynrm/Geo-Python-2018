# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:42:31 2018

@author: katel
"""
import pandas as pd


#Problem 1

fp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\1091402.txt'

data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values='-9999')

#how many no data values are in TAVG?
tavg_nodata_count = data['TAVG'].isna().sum()
print("There are", tavg_nodata_count, "Nan values in TAVG")

#how many no data valuers are in TMIN?
tmin_nodata_count = data['TMIN'].isna().sum()
print(tmin_nodata_count)


#how many days are covered in the dataset?
day_count = data['DATE'].count()
print("There are", day_count, "days in the data.")

#When was the first observation?
first_obs = data.sort_values(by='DATE')
first_obs = first_obs.reset_index()

print("The first observation was made in", first_obs.loc[0, 'DATE'])