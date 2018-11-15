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
#create random numbers for x,y points and colors, then save
x = np.random.rand(1000)
y = np.random.rand(1000)

colors = np.random.rand(1000)

plt.scatter(x,y, s=50, c=colors)
plt.title('My random candy points')
plt.xlabel('X-label')
plt.ylabel('Y-label')
#plt.savefig('my_first_plot.png')

'''
#Problem 2 - make a plot with Helsinki temp data
'''
fp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\helsinki.csv'
df = pd.read_csv(fp, sep=',')
selected = df.loc[(df['DATE']>= 201001) & (df['DATE']<= 201612)]

y = selected['temp_celsius']
x = selected['DATE']
plt.plot(x,y, color='black', marker='o', linestyle='dashed')
plt.title('Temperatures in Celsius: 2010-2016')
plt.xlabel('Time')
plt.ylabel('Temp (C)')

#plt.savefig('temp_line_plot.png')
'''
#Problem 3
#Problem 4
#Problem 5
'''