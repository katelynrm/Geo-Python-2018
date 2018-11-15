# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:18:25 2018

@author: katel
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Problem 1 - Create a scatter plot 
'''
#create random numbers for x,y points and colors
x = np.random.rand(1000)
y = np.random.rand(1000)

colors = np.random.rand(1000)

plt.scatter(x,y, s=50, c=colors)
plt.title('My random candy points')
plt.xlabel('X-label')
plt.ylabel('Y-label')
#plt.savefig('my_first_plot.png')
'''
#Problem 2
#Problem 3
#Problem 4
#Problem 5
'''