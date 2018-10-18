# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:04:25 2018

@author: katel
"""
###########
#PROBLEM 1#
###########
basename = "Station"

#create an empty list
filenames = []

for i in range(21):
    filenames.append(basename+"_"+str(i)+".txt")
    
    
print(filenames)