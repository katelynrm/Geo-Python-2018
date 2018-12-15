# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:53:57 2018

@author: katel
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString, MultiLineString, MultiPoint
from shapely.ops import nearest_points
from geopandas.tools import geocode

#Created a text file with the address for a rink about halfway between Jumbo and Itis
fp_rink = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\activity_locations.txt'

rink = pd.read_csv(fp_rink, sep=';')

geocoded_rink = geocode(rink['addr'], provider = 'nominatim', user_agent = 'autogis_student_78')

geocoded_rink = geocoded_rink.to_crs({'init': 'epsg:3879'})

#read in the shp of shopping center points created in the previous E
fp_sc = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\AutoGIS\shopping_centers.shp'

shop_centers = gpd.read_file(fp_sc)

shop_centers = shop_centers.to_crs({'init': 'epsg:3879'})



unary_union = shop_centers.unary_union

nearest_geoms = nearest_points(geocoded_rink['geometry'][0], unary_union)
near_idx0 = nearest_geoms[0]
near_idx1 = nearest_geoms[1]