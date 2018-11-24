# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:48:19 2018

@author: katel
"""
from shapely.geometry import Point, LineString, Polygon 
import pandas as pd

fp =r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\travelTimes_2015_Helsinki.txt'
data = pd.read_table(fp, sep=';', usecols=['from_x','from_y','to_x','to_y'])

#empty lists that will be filled with shapely points next
orig_points = []
dest_points = []

#create shapely points out of the from and to columns, add these
#to the above lists
for idx, row in data.iterrows():
   point_orig = Point(row['from_x'],row['from_y'])
   point_dest = Point(row['to_x'],row['to_y'])
   orig_points.append(point_orig)
   dest_points.append(point_dest)