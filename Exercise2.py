# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:03:00 2018

@author: katel
"""
# First edit is removing ', ' between Kumpula and lighthouse
stationNames = ['Harmaja', 'Kaisaniemi', 'Kaivopuisto', 'Kumpula lighthouse', \
                'Malmi airfield', 'Suomenlinna aaltopoiju', 'Vuosaari harbour']


stationStartYears = [1989, 1844, 1904, 2005, 2003, 1937, 2016, 2012]

#Second error, need to input name not number
selectedStation = 'Harmaja'

# DO NOT EDIT THIS CELL
stationIndex = stationNames.index(selectedStation)

stationYears = 2018 - stationStartYears[selectedStation]

print("The Helsinki", selectedStation, "station has been operational for", \
      stationYears, "years.)