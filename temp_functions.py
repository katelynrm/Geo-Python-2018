# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:03:57 2018

@author: katel
"""

###########
#PROBLEM 1#  Creat a temp coverter. Fahrensheit to Celsius
###########
def fahrToC(tempF):
    return (tempF-32)*(5/9)


###########
#PROBLEM 2# Creat if else statement
###########
def temp_classifier(tempC):
    if tempC <-2:
        return 0
    elif tempC >= -2 and tempC <2:
        return 1
    elif tempC >=2 and tempC <15:
        return 2
    else:
        return 3
