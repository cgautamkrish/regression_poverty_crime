import csv
import threading
import time 
import datetime
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

x, x1, x2, y, y1, y2 = ([] for i in range(6))

cr = csv.reader(open("data/JOB_UNEMPLOYMENT_RATE.csv","rt"))
toggle = 0
for row in cr:
	if toggle != 0:
		year = row[0].split('-')
		x.append(int(year[0]))
		y.append(float(row[1])*1000000)
	toggle += 1

cr = csv.reader(open("data/LEVELS.csv","rt"))
toggle = 0
for row in cr:
	if toggle != 0:
		year = row[0].split('-')
		x1.append(int(year[0]))
		y1.append(float(row[1]))
	toggle += 1

cr = csv.reader(open("data/POVERTY_B.csv","rt"))
toggle = 0
for row in cr:
	if toggle != 0:
		if row[3] != '':
			year = row[0].split('-')
			x2.append(int(year[0]))
			y2.append(float(row[3])*10000000)
	toggle += 1

s = np.pi * (1 * 2)**2
plt.scatter(x, y, s=s, c='b', alpha=0.5, label='first')
plt.scatter(x1, y1, s=s, c='r', alpha=0.5, label='second')
plt.scatter(x2, y2, s=s, c='g', alpha=0.5, label='third')
plt.show()