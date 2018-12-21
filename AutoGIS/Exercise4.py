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


breaks=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

#classify the data
n_classes = 13

m_array = myyrmanni_geo['pt_r_t'].values

# Create a Natural Breaks classifier
classifier = ps.User_Defined(m_array, breaks)

m_classifications = myyrmanni_geo[['pt_r_t']].apply(classifier)




n_classes = 9

# Create a Natural Breaks classifier
classifier = ps.Natural_Breaks.make(k=n_classes)

# Classify the data
classifications = acc[['pt_r_tt']].apply(classifier)





