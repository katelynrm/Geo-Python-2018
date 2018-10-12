# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:03:00 2018

@author: katel
"""
###########
#PROBLEM 1#
###########

# First edit is removing ', ' between Kumpula and lighthouse
stationNames = ['Harmaja', 'Kaisaniemi', 'Kaivopuisto', 'Kumpula lighthouse', \
                'Malmi airfield', 'Suomenlinna aaltopoiju', 'Vuosaari harbour']


stationStartYears = [1989, 1844, 1904, 2005, 2003, 1937, 2016, 2012]

#Second edit, need to input name not number
selectedStation = 'Harmaja'

stationIndex = stationNames.index(selectedStation)

#Third edit, changed selectedStation to stationIndex
stationYears = 2018 - stationStartYears[stationIndex]

#Fourth edit, add quote after years.
print("The Helsinki", selectedStation, "station has been operational for", \
      stationYears, "years.")

###########
#PROBLEM 2#
###########

monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', \
             'August', 'September', 'October', 'November', 'December']

monthTemps = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]

selectedMonth = 'May'

monthIndex = monthName.index(selectedMonth)

selectedMonthTemp = monthTemps[monthIndex]

print("The average temperature in Helsinki in", selectedMonth, "is", selectedMonthTemp)





