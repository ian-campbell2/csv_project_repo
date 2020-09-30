#https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file_s = open('sitka_weather_2018_simple.csv', 'r')

csv_file_s = csv.reader(open_file_s, delimiter=',')



open_file_d = open('death_valley_2018_simple.csv', 'r')

csv_file_d = csv.reader(open_file_d, delimiter=',')

file_dict = {'sitka':csv_file_s,'death':csv_file_d}


for x in file_dict:

    header_row = next(file_dict[x])
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            max_col = index
        if column_header == 'TMIN':
            min_col = index
        if column_header == 'DATE':
            time_col = index

    
    if file_dict[x] == csv_file_s:
        highs_s = []
        lows_s = []
        dates_s = [] 

        for row in file_dict[x]:
            try:
                highs_s.append(int(row[max_col]))
                lows_s.append(int(row[min_col]))
                the_date = datetime.strptime(row[time_col],'%Y-%m-%d')
                dates_s.append(the_date)
            except:
                print('A value was missing in the data')
                pass

    if file_dict[x] == csv_file_d:
        highs_d = []
        lows_d = []
        dates_d = [] 

        for row in file_dict[x]:
            try:
                highs_d.append(int(row[max_col]))
                lows_d.append(int(row[min_col]))
                the_date = datetime.strptime(row[time_col],'%Y-%m-%d')
                dates_d.append(the_date)
            except:
                print('A value was missing in the data')
                pass
'''
for x in file_dict:
    title_s_d = []
    header_row = next(file_dict[x])
    for index, column_header in enumerate(header_row):
        if column_header == 'NAME':
            if file_dict[x] == csv_file_s:
                s_title.append()
            if file_dict[x] == csv_file_d:
'''
fig, ax = plt.subplots(2)
fig.suptitle('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US')

ax[0].plot(dates_s, highs_s, c='red')
ax[0].plot(dates_s, lows_s, c="blue", alpha=0.5)
ax[0].fill_between(dates_s, highs_s, lows_s, facecolor='blue', alpha=0.1)

ax[0].set_title('SITKA AIRPORT, AK US', fontsize= 16)
ax[0].set(xlabel='',ylabel='Temperature (F)')
ax[0].tick_params(axis='both',labelsize=12)



ax[1].plot(dates_d, highs_d, c='red')
ax[1].plot(dates_d, lows_d, c="blue", alpha=0.5)
ax[1].fill_between(dates_d, highs_d, lows_d, facecolor='blue', alpha=0.1)

ax[1].set_title('DEATH VALLEY, CA US', fontsize= 16)
ax[1].set(xlabel='',ylabel='Temperature (F)')
ax[1].tick_params(axis='both',labelsize=12)


fig.autofmt_xdate()


plt.show()
