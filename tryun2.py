import csv
import random 
import sys
min = 10
max = 10
level = 1
away_rate = 0.75
map = []     
new = [] 
for j in range (0, 2):
	foo = random.uniform(min, max)
	new.append(foo)
map.append(new)
for i in range (0, 16):
	new = []
	min_range = min
	max_range = max
	pos = i % 8
	if(i > 0):
		if(pos == 0):
			level += 4
	for j in range (0, 2):
		if (j == 0):
			if(pos == 0 or pos == 1 or pos == 2):
				min_range = min - (level * away_rate)
				max_range = max - (level * away_rate)
			elif(pos == 5 or pos == 6 or pos == 7):
				min_range = min + (level * away_rate)
				max_range = max + (level * away_rate)
			else:
				min_range = min
				max_range = max
		elif(j == 1):
			if(pos == 0 or pos == 3 or pos == 5):
				min_range = min + (level * away_rate)
				max_range = max + (level * away_rate)
			elif(pos == 2 or pos == 4 or pos == 7):
				min_range = min - (level * away_rate)
				max_range = max - (level * away_rate)
			else:
				min_range = min
				max_range = max
		foo = random.uniform(min_range, max_range)
		new.append(foo)
	map.append(new)
kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('squary.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(map)