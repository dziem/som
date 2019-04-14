import csv
import random 
import sys
min = 9.5
max = 10.5
level = 1
away_rate = 0.75
map = []     
new = [] 
for j in range (0, 2):
	foo = random.uniform(min, max)
	new.append(foo)
map.append(new)
for i in range (0, 12):
	new = []
	min_range = min
	max_range = max
	pos = i % 6
	if(i > 0):
		if(pos == 0):
			level += 4
	for j in range (0, 2):
		if (j == 0):
			if(pos == 0 or pos == 1):
				min_range = min - (level * away_rate)
				max_range = max - (level * away_rate)
			elif(pos == 4 or pos == 5):
				min_range = min + (level * away_rate)
				max_range = max + (level * away_rate)
			else:
				min_range = min
				max_range = max
		elif(j == 1):
			if(pos == 0 or pos == 4):
				min_range = min + (level * away_rate)
				max_range = max + (level * away_rate)
			elif(pos == 1 or pos == 5):
				min_range = min - (level * away_rate)
				max_range = max - (level * away_rate)
			elif(pos == 2):
				min_range = min + (2 * level * away_rate)
				max_range = max + (2 * level * away_rate)
			elif(pos == 3):
				min_range = min - (2 * level * away_rate)
				max_range = max - (2 * level * away_rate)
		foo = random.uniform(min_range, max_range)
		new.append(foo)
	map.append(new)
kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('hexy.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(map)