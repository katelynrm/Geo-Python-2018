# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:34:58 2018

@author: katel
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString, MultiLineString, MultiPoint
from shapely.ops import nearest_points
from geopandas.tools import geocode
import matplotlib.pyplot as plt
import shapely.speedups
shapely.speedups.enable()



#Problem 1: Geocode shopping centers





#Problem 2: Create buffers around shopping centers






#Problem 3: How many people live within 5 km from shopping centers?