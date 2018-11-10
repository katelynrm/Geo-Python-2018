import re
import os
import csv

os.path.join('Users', 'katel', 'Documents', 'AutoGIS', '2018', 'Geo-Python-2018')

print(os.path.getsize('C:\\Users\\katel\\Documents\\AutoGIS\\2018\\Geo-Python-2018\\Exercise3.py'))
print(len(os.listdir(r'C:\Users\katel\Documents\AutoGIS')))

f = open(r'C:\Users\katel\Documents\AutoGIS\2018\Geo-Python-2018\untitled3.txt')
csv_f = csv.reader(f)

f_1 = []

for row in csv_f:
    f_1.append(row[1])
    
f.close()    
    