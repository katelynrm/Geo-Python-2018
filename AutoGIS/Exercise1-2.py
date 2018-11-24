# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:48:19 2018

@author: katel
"""
from shapely.geometry import Point, LineString, Polygon 
import pandas as pd

'''
Prob 3
'''

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
   
   
   
'''
Prob 4
'''
#create an empty list to be filled by the following
lines =[]

#Iterate throught the orig and dest point lists to create a list of linestrings
for o, d in zip(orig_points,dest_points):
    od_line = LineString([o,d])
    lines.append(od_line)
    
#calculate the total distance of the lenth of the LIneStrings in lines list

def get_length(geom):
    assert geom.geom_type in ['LineString', 'Polygon'], "Input must be a Shapely line or polygon"
    return geom.length

total_length = 0

for i in range(len(lines)):
    total_length = total_length + get_length(lines[i])


#testing out the +=
other_length = 0

for i in range(len(lines)):
    other_length += get_length(lines[i])


print("Total length of all lines is", total_length)













