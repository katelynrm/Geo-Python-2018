# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:42:31 2018

@author: katel
"""
import pandas as pd


#Problem 1

fp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\1091402.txt'

data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values='-9999')

#how many no data values are in TAVG?
tavg_nodata_count = data['TAVG'].isna().sum()
print("There are", tavg_nodata_count, "Nan values in TAVG")

#how many no data valuers are in TMIN?
tmin_nodata_count = data['TMIN'].isna().sum()
print("There are", tmin_nodata_count, "Nan values in TMIN")


#how many days are covered in the dataset?
day_count = data['DATE'].count()
print("There are", day_count, "days in the data.")

#When was the first observation?
first_obs = data.sort_values(by='DATE')
first_obs = first_obs.reset_index()

print("The first observation was made in", first_obs.loc[0, 'DATE'])

#When was the last observation?
last_obs = data.sort_values(by='DATE', ascending=False)
last_obs = last_obs.reset_index()
#alternate without having to sort: last_obs_c = len(data)-1
print("The last observation was made in", last_obs.loc[0, 'DATE'])


#avg temp of all the data
avg_temp = data["TAVG"].mean()
print("The average temp of the dataframe is:", avg_temp)

#What was the avg max temp of the summer of 69?
temps69 = data.loc[(data['DATE']>= 19690501) & (data['DATE']<= 19690831)]
temps69 = temps69.reset_index()
avg_temp_69 = temps69['TMAX'].mean()
print("The avg max temp of the summer of 69 was:", avg_temp_69)
#What was the max temp of the summer of 69?
max_temp_69 = temps69['TMAX'].max()
print("The max temp of the summer of 69 was:", max_temp_69)

'''
Problem 2
Calculate the monthly average temperatures for the entire data 
(i.e. for each year separately) file using the approach taught in the lecture.
You should store the average temperatures into a new Pandas DataFrame called monthly_data.
Create a new column called temp_celsius into the monthly_data DataFrame 
that has the monthly temperatures in Celsius.
'''
#Make monthly values for DATE
data['DATE'] = data['DATE'].astype(str)
data['DATE'] = data['DATE'].str.slice(start=0, stop=6)
data['DATE'] = data['DATE'].astype(int)
#make a celsius column
data['temp_celsius'] = (data['TAVG']-32)/1.8

#create an empty dataframe that will be filled
monthly_data = pd.DataFrame()

#group by the date value
grouped = data.groupby('DATE')

#column to aggregate
mean_col = ['temp_celsius']


for key, group in grouped:
    #the value we want to have the mean of is temp_celsius
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['DATE'] = key
    #filling the empty data frame with agg temps by date
    monthly_data = monthly_data.append(mean_vals, ignore_index=True)
    
monthly_data['DATE'] = monthly_data['DATE'].astype(int)


'''
Problem 3 - aggregate the data by month, then find temp anomalies
'''
#Make date value for each month
monthly_data['DATE_m'] = monthly_data['DATE'].astype(str)
monthly_data['DATE_m'] = monthly_data['DATE_m'].str.slice(start=4, stop=6)
monthly_data['DATE_m'] = monthly_data['DATE_m'].astype(int)

#empty dataframe
reference_temps = pd.DataFrame()

#group by the date value
grouped_m = monthly_data.groupby('DATE_m')

#column to aggregate
mean_col = ['temp_celsius']


for key, group in grouped_m:
    #the value we want to have the mean of is temp_celsius
    mean_vals = group[mean_col].mean()
    #the key for aggregating the data is Date
    mean_vals['DATE_m'] = key
    #filling the empty data frame with agg temps by date
    reference_temps = reference_temps.append(mean_vals, ignore_index=True)

reference_temps['DATE_m'] = reference_temps['DATE_m'].astype(int)

#rename the columns
reference_temps = reference_temps.rename(columns={"DATE_m":"Month", "temp_celsius": "ref_temp"})


#Join the data frame to find anomalies
join = monthly_data.merge(reference_temps, left_on='DATE_m', right_on='Month')

join['diff'] = join['temp_celsius']-join['ref_temp']

print(join['diff'].max())













