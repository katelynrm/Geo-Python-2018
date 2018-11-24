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
        assert i.geom_type is 'Point', "All list values should be Shapely Point objects!"
    return LineString(points) 


#create a function that will create a shapely polygon
def create_poly_geom_tuple(coords):
    assert type(coords) is list, "Input should be a list!"
    assert len(coords) >= 3, "LineString object requires at least two Points!"
    for i in coords:
        assert type(i) is tuple, "All list values should be Shapely Point objects!"
            
            
    return Polygon(coords)


        
def create_poly_geom_point(coords):
    assert type(coords) is list, "Input should be a list!"
    assert len(coords) >= 3, "LineString object requires at least two Points!"
    for i in coords:
        return Polygon([[i.x, i.y] for i in coords])


'''
Problem 2
'''
#create a function that will find a centroid of a shapely object
def get_centroid(geom):
    assert geom.geom_type in ['Point', 'LineString', 'Polygon'], "Input should be a Shapely object"
    return geom.centroid

#create a function that will find the area of a shapely polygon
def get_area(polygon):
    assert polygon.geom_type is 'Polygon', "Input must be Shapely polygon"
    return polygon.area


# Demonstrate the usage of the function 

# Create a Polygon with three points: Point(45.2, 22.34) & Point(100.22, -3.20) & Point(70.0, 10.20)
# You can take advantage of the 'create_poly_geom' -function:


# What is the area of this Polygon? Print the answer below by using the 'get_area' -function:
test_point_list = [(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)]
test_poly = create_poly_geom_tuple(test_point_list)
test_poly_area = get_area(test_poly)
print(test_poly_area)


def get_length(geom):
    assert geom.geom_type in ['LineString', 'Polygon'], "Input must be a Shapely line or polygon"
    return geom.length


print(get_length(test_poly))



