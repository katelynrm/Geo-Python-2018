# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:05:27 2018

@author: katel
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups
import pandas as pd
import pysal as ps
import os
import glob
import seaborn as sns

files = glob.glob(r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\E4_data\tfiles\*')
fp_shp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\E4_data\MetropAccess_YKR_grid_EurefFIN.shp'

col_list = ['pt_r_t', 'car_r_t', 'from_id', 'to_id']

#concatenated df
df = pd.concat([pd.read_csv(f, sep=';', usecols=col_list) for f in files], ignore_index = True)

MYYRMANNI = pd.read_csv(files[2], sep=';', usecols=col_list)
ITIS = pd.read_csv(files[3], sep=';', usecols=col_list)

grid = gpd.read_file(fp_shp)

myyrmanni_geo = grid.merge(MYYRMANNI, left_on='YKR_ID', right_on='from_id')
itis_geo = grid.merge(ITIS, left_on='YKR_ID', right_on='from_id')

myyrmanni_geo = myyrmanni_geo.replace(to_replace={-1: 999})
itis_geo = itis_geo.replace(to_replace={-1: 999})

#classify the data
#userdefined breaks
breaks=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


#Create arrays
m_array_pt = myyrmanni_geo['pt_r_t'].values
m_array_car = myyrmanni_geo['car_r_t'].values

i_array_pt = itis_geo['pt_r_t'].values
i_array_car = itis_geo['car_r_t'].values

# Create a Natural Breaks classifier
classifier_m_pt = ps.User_Defined(m_array_pt, breaks)
classifier_m_car = ps.User_Defined(m_array_car, breaks)

classifier_i_pt = ps.User_Defined(i_array_pt, breaks)
classifier_i_car = ps.User_Defined(i_array_car, breaks)


m_classifications_pt = myyrmanni_geo[['pt_r_t']].apply(classifier_m_pt)
m_classifications_pt.columns = ['ud_pt_r_t']

m_classifications_car = myyrmanni_geo[['car_r_t']].apply(classifier_m_car)
m_classifications_car.columns = ['ud_car_r_t']

i_classifications_pt = itis_geo[['pt_r_t']].apply(classifier_i_pt)
i_classifications_pt.columns = ['ud_pt_r_t']

i_classifications_car = itis_geo[['car_r_t']].apply(classifier_i_car)
i_classifications_car.columns = ['ud_car_r_t']


m_pt_join = myyrmanni_geo.join(m_classifications_pt)
m_car_join = myyrmanni_geo.join(m_classifications_car)

i_pt_join = itis_geo.join(i_classifications_pt)
i_car_join = itis_geo.join(i_classifications_car)


m_pt_join.plot(column="ud_pt_r_t", linewidth=0, legend=True)
m_car_join.plot(column="ud_car_r_t", linewidth=0, legend=True)

i_pt_join.plot(column="ud_pt_r_t", linewidth=0, legend=True)
i_car_join.plot(column="ud_car_r_t", linewidth=0, legend=True)



fig, axes = plt.subplots(1, 2, figsize=(10,10))

# 1st subplot
ax = m_pt_join.plot(column='ud_pt_r_t', axes=axes.flat[0])

# 2nd subplot
ax = m_car_join.plot(column='ud_car_r_t', axes=axes.flat[1])
