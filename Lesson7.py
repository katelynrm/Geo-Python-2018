# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:52:48 2018

@author: katel
"""
import matplotlib.pyplot as plt

import pandas as pd

dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)

date = dataFrame['YEARMODA'].values
temp = dataFrame['TEMP'].values
temp_max = dataFrame['MAX'].values
temp_min = dataFrame['MIN'].values

x = date
y = temp
plt.plot(x, y)

plt.plot(x, y, 'ro--')
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')

plt.text(20160604.0, 68.0, 'High temperature in early June')

plt.axis([20160601, 20160615, 55.0, 70.0])


plt.bar(x, y)
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')
plt.text(20160604.0, 68.0, 'High temperature in early June')
plt.axis([20160601, 20160615, 55.0, 70.0])
plt.savefig('bar-plot.png')
plt.savefig('bar-plot-hi-res.pdf', dpi=600)