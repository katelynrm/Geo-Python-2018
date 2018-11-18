# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

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
Problem 2 - make a plot with Helsinki temp data
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
Problem 3 - create graphs for seasons between 1953-2016
'''
#create a dataframe for temps between 1953-2016
df_53_16 = df.loc[(df['DATE']>= 195301) & (df['DATE']<= 201612)]

#create a month column
df_53_16['DATE_m'] = df_53_16['DATE'].astype(str)
df_53_16['DATE_m'] = df_53_16['DATE_m'].str.slice(start= 4,stop=6)
df_53_16['DATE_m'] = df_53_16['DATE_m'].astype(int)

#Create a year column 
df_53_16['year'] = df_53_16['DATE'].astype(str)
df_53_16['year'] = df_53_16['year'].str.slice(start= 0,stop=4)
df_53_16['year'] = df_53_16['year'].astype(int)


#create dataframes for each season
winter = df_53_16.loc[(df_53_16['DATE_m']<=2)|(df_53_16['DATE_m']==12)] 
spring = df_53_16.loc[(df_53_16['DATE_m']>= 3) & (df_53_16['DATE_m']<= 5)]
summer = df_53_16.loc[(df_53_16['DATE_m']>= 6) & (df_53_16['DATE_m']<= 8)]
fall = df_53_16.loc[(df_53_16['DATE_m']>= 9) & (df_53_16['DATE_m']<= 11)]


#calculate the diff
winter['mean_anomaly'] = (winter['temp_celsius'])-(winter['temp_celsius'].mean())
spring['mean_anomaly'] = (spring['temp_celsius'])-(spring['temp_celsius'].mean())
summer['mean_anomaly'] = (summer['temp_celsius'])-(summer['temp_celsius'].mean())
fall['mean_anomaly'] = (fall['temp_celsius'])-(fall['temp_celsius'].mean())

#create empty dataframes
winter_agg = pd.DataFrame()
spring_agg = pd.DataFrame()
summer_agg = pd.DataFrame()
fall_agg = pd.DataFrame()

#group the data
winter_group = winter.groupby('year')
spring_group = spring.groupby('year')
summer_group = summer.groupby('year')
fall_group = fall.groupby('year')


mean_col = ['mean_anomaly']

#loop trhough each to find the anomoly by year

#winter
for key, group in winter_group:
    #the value we want to have the mean of 
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['year'] = key
    #filling the empty data frame with agg temps by date
    winter_agg = winter_agg.append(mean_vals, ignore_index=True)

winter_agg['year'] = winter_agg['year'].astype(int)

#spring

for key, group in spring_group:
    #the value we want to have the mean of 
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['year'] = key
    #filling the empty data frame with agg temps by date
    spring_agg = spring_agg.append(mean_vals, ignore_index=True)

spring_agg['year'] = spring_agg['year'].astype(int)


#summer

for key, group in summer_group:
    #the value we want to have the mean of 
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['year'] = key
    #filling the empty data frame with agg temps by date
    summer_agg = summer_agg.append(mean_vals, ignore_index=True)

summer_agg['year'] = summer_agg['year'].astype(int)
#fall


for key, group in fall_group:
    #the value we want to have the mean of 
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['year'] = key
    #filling the empty data frame with agg temps by date
    fall_agg = fall_agg.append(mean_vals, ignore_index=True)

fall_agg['year'] = fall_agg['year'].astype(int)



#Create figure
fig, axes = plt.subplots(nrows=2, ncols=2)
ax11 = axes[0][0]
ax12 = axes[0][1]
ax21 = axes[1][0]
ax22 = axes[1][1]

min_temp = -5
max_temp = 5


ax11.grid()
ax12.grid()
ax21.grid()
ax22.grid()


# Set plot line width
line_width = 1.5

# Plot data
ax11.plot(winter_agg, c='blue', lw=line_width)
ax12.plot(spring_agg, c='orange', lw=line_width)
ax21.plot(summer_agg, c='green', lw=line_width)
ax22.plot(fall_agg, c='brown', lw=line_width)



ax11.set_ylim(min_temp, max_temp)
ax12.set_ylim(min_temp, max_temp)
ax21.set_ylim(min_temp, max_temp)
ax22.set_ylim(min_temp, max_temp)


ax21.set_xlabel('Date')
ax22.set_xlabel('Date')
ax11.set_ylabel('Temperature [deg. C]')
ax21.set_ylabel('Temperature [deg. C]')

plt.savefig('seasonal_temperatures.png')


'''
#Problem 4
'''
'''
#Problem 5
'''