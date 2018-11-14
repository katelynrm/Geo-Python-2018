# -*- coding: utf-8 -*-
###########
#Problem 1#
###########
import pandas as pd
fp = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\6153237444115dat.csv'

dataFrame = pd.read_csv(fp, sep=',', na_values=['*', '**', '***', '****', '*****', '******'])


print("There are", len(dataFrame), "rows")
print("The columns are \n", dataFrame.columns)
print("The column's datatypes are \n", dataFrame.dtypes)


temp_mean = dataFrame['TEMP'].mean()
temp_max_std = dataFrame['MAX'].std()
station_count = len(dataFrame['USAF'].unique())

print("Mean temperature in Fahrenheit is ", round(temp_mean,1))
print("Standard deviation of maximum temperature is ", round(temp_max_std, 1))
print("The number of unique stations is ", station_count)


#############
#Problem 2a##
#############

selected = dataFrame[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']].dropna(subset=['TEMP'])

selected['Celsius'] = round(((selected['TEMP']-32)/1.8), 1).astype(int)

############
#Problem 2b#
############

kumpula = selected.loc[selected['USAF']==29980]
rovaniemi = selected.loc[selected['USAF']==28450]

print("Kumpula: \n", kumpula.head(), "\n")
print("Rovaniemi: \n", rovaniemi.head(), "\n")


fp_k = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\Kumpula_temps_May_Aug_2017.csv'
fp_r = r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\Rovaniemi_temps_May_Aug_2017.csv'

#kumpula.to_csv(fp_k, sep=',', index=False, float_format='%.2f')
#rovaniemi.to_csv(fp_r, sep=',', index=False, float_format='%.2f')
 
############
#Problem 3#
############

kumpula_median = kumpula['TEMP'].median()
rovaniemi_median = rovaniemi['TEMP'].median()


print("Kumpula median: ", kumpula_median)
print("Rovaniemi median: ", rovaniemi_median)


kumpula_may = kumpula.loc[(kumpula['YR--MODAHRMN']>= 201705010000) & (kumpula['YR--MODAHRMN']<= 201705309999)]
rovaniemi_may = rovaniemi.loc[(rovaniemi['YR--MODAHRMN']>= 201705010000) & (rovaniemi['YR--MODAHRMN']<= 201705309999)]

kumpula_june = kumpula.loc[(kumpula['YR--MODAHRMN']>= 201706010000) & (kumpula['YR--MODAHRMN']<= 201706299999)]
rovaniemi_june = rovaniemi.loc[(rovaniemi['YR--MODAHRMN']>= 201706010000) & (rovaniemi['YR--MODAHRMN']<= 201706299999)]

print('The mean temp of Kumpula in May 2017 was:', kumpula_may['TEMP'].mean())
print('The min temp of Kumpula in May 2017 was:', kumpula_may['MIN'].min())
print('The max temp of Kumpula in May 2017 was:', kumpula_may['MAX'].max())
print('The mean temp of Rovaniemi in May 2017 was:', rovaniemi_may['TEMP'].mean())
print('The mean temp of Rovaniemi in May 2017 was:', rovaniemi_may['MIN'].min())
print('The mean temp of Rovaniemi in May 2017 was:', rovaniemi_may['TEMP'].max())

print('The mean temp of Kumpula in June 2017 was:', kumpula_june['TEMP'].mean())
print('The min temp of Kumpula in June 2017 was:', kumpula_june['MIN'].min())
print('The max temp of Kumpula in June 2017 was:', kumpula_june['MAX'].max())
print('The mean temp of Rovaniemi in June 2017 was:', rovaniemi_june['TEMP'].mean())
print('The min temp of Rovaniemi in June 2017 was:', rovaniemi_june['MIN'].min())
print('The max temp of Rovaniemi in June 2017 was:', rovaniemi_june['TEMP'].max())








