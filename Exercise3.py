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
    

###########
#PROBLEM 2#
###########

#categorize temps into cold, slippery, comfortable and warm by looping with nested conditionals then print number of
#days in each category
#here is the list of temps
temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]
#create empty cat lists
cold = []
slippery = []
comfortable = []
warm = []


#now iterate and catergorize!!!!

for i in range(len(temperatures)):
    if temperatures[i] < -2:
        cold.append(i)
    elif temperatures[i] >= -2 and temperatures[i]<2:
        slippery.append(i)
    elif temperatures[i] >= 2 and temperatures[i] <15:
        comfortable.append(i)
    else:
        warm.append(i)
    

#Print the number of days the temps occurred in each category
        
cold_times = len(cold)
slippery_times = len(slippery)
comfortable_times = len(comfortable)
warm_times = len(warm)

print("In April 2013 it was cold", cold_times, "times.")
print("In April 2013 it was slippery", slippery_times, "times.")
print("In April 2013 it was comfortable", comfortable_times, "times.")
print("In April 2013 it was warm", warm_times, "times.")

    
###########
#PROBLEM 3#
###########








