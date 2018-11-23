# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from shapely.geometry import Point, LineString, Polygon 

#create a function that will create a shapely point
def create_point_geom(x_cord, y_cord):
    return Point(x_cord, y_cord)


#create a function that will create a shapely linestring
def create_line_geom(points):
    assert type(points) is list, "Input should be a list!"
    assert len(points) >= 2, "LineString object requires at least two Points!" 
    for i in points:
        assert type(i) is list, "All list values should be Shapely Point objects!"