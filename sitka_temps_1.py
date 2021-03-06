import csv

open_file = open('sitka_weather_07-2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)


highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c='red')

plt.title("Daily High Temp, July 2018", fontsize= 16)
plt.xlabel('')
plt.ylabel('Temperature (F)', fontsize= 16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()