# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 09:35:22 2018

@author: katel
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups
import pandas as pd
import pysal as ps
import glob
import numpy as np

filepaths = glob.glob(r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\E4_data\tfiles\*')
fp_shp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\E4_data\MetropAccess_YKR_grid_EurefFIN.shp'

grid = gpd.read_file(fp_shp)

for idx, fp in enumerate(filepaths):
    data = pd.read_csv(fp, sep=';', usecols=['from_id','pt_r_t'])
    data = data.rename(columns={"pt_r_t": "pt_r_t_"+ (str(idx))})
    grid = grid.merge(data, left_on='YKR_ID', right_on='from_id')



grid_keep = ['x', 'y', 'YKR_ID', 'geometry', 'pt_r_t_0',
       'pt_r_t_1', 'pt_r_t_2', 'pt_r_t_3', 'pt_r_t_4', 'pt_r_t_5', 'from_id',
       'pt_r_t_6']

grid = grid[grid_keep]

grid = grid.replace(-1, np.nan)

grid = grid.dropna()

grid['min_t'] = grid[['pt_r_t_0',
       'pt_r_t_1', 'pt_r_t_2', 'pt_r_t_3', 'pt_r_t_4', 'pt_r_t_5', 'pt_r_t_6']].min(axis=1)

grid['min_idx'] = grid[['pt_r_t_0',
       'pt_r_t_1', 'pt_r_t_2', 'pt_r_t_3', 'pt_r_t_4', 'pt_r_t_5', 'pt_r_t_6']].idxmin(axis=1)



grid.plot(column='min_idx', scheme="Fisher_Jenks", k=7, cmap="RdYlBu", linewidth=0)
plt.title('dominance areas of shopping centers')

grid.plot(column='min_t', scheme="Fisher_Jenks", k=9, cmap="RdYlBu", linewidth=0)
plt.title('travel times closest to shopping centers')








#df = pd.concat([pd.read_csv(f, sep=';') for f in files], ignore_index = True)
    
#df_list = [pd.read_csv(file, sep=';') for file in files]
#
#shopping_centers = []
#
#for f in files:
#    shopping_centers.append(((f.split('_')[-1]).split('.')[-2]).lower())
#    
#jumbo = df_list[0].rename(columns=lambda x: x + "_0")
#dixi = df_list[1].rename(columns=lambda x: x + "_1")
#myyrmanni = df_list[2].rename(columns=lambda x: x + "_2")
#itis = df_list[3].rename(columns=lambda x: x + "_3")
#forum = df_list[4].rename(columns=lambda x: x + "_4")
#omena = df_list[5].rename(columns=lambda x: x + "_5")
#ruoholahti = df_list[6].rename(columns=lambda x: x + "_6")
#    
#shopdict = {'jumbo':0, 
#            'dixi':1, 
#            'myyrmanni':2, 
#            'itis':3, 
#            'forum':4, 
#            'omena':5, 
#            'ruoholahti':6}
#
#test = [jumbo, dixi, myyrmanni, itis, forum, omena, ruoholahti]