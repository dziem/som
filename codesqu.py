import csv
import sys
import math
import numpy as np
import random 
import copy

#const
tmax = 1200
epsilon0 = 0.0004
unit = 17
sigma0 = unit - 1
min_random_range = 9.5
max_random_range = 10.5

#functions
def fixText(text):
    row = []
    z = text.find(',')
    if z == 0:  row.append('')
    else:   row.append(text[:z])
    for x in range(len(text)):
        if text[x] != ',':  pass
        else:
            if x == (len(text)-1):  row.append('')
            else:
                if ',' in text[(x+1):]:
                    y = text.find(',', (x+1))
                    c = text[(x+1):y]
                else:   c = text[(x+1):]
                row.append(c)
    return row

def createTuple(oldFile):
    ## oldFile is filename (e.g. 'sheet.csv')
    f1 = open(oldFile, "r")
    tup = []
    while 1:
        text = f1.readline()
        if text == "":  break
        else:   pass
        if text[-1] == '\n':
            text = text[:-1]
        else:   pass
        row = fixText(text)
        tup.append(row)
    return tup

def sigma(t):
	return sigma0 * math.exp( -1 * (t / tmax) )

def epsilon(t):
	return epsilon0 * math.exp( -1 * (t / tmax) )
	
def euclid(x, y):
	return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

def neighbourhood(t, j, jbintang):
	return math.exp( -1 * ((euclid(j, jbintang) ** 2) / (2 * (sigma(t) ** 2))) )	

#get dataset from csv file
data = np.array(createTuple('datasetcsv.csv'))
datas = data.astype(np.float)
#create map
min = min_random_range
max = max_random_range
level = 1
away_rate = 2
map = []     
new = [] 
for j in range (0, 2):
	foo = random.uniform(min, max)
	new.append(foo)
map.append(new)
for i in range (0, (unit -1 )):
	new = []
	min_range = min
	max_range = max
	pos = i % 8
	if(i > 0):
		if(pos == 0):
			level += 2
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
t = 0
rows_num = len(datas) - 1
while t < tmax:
	random_index = random.randint(0,rows_num)
	min_distance = euclid(map[0], datas[random_index])
	min_index = 0
	j = 0
	while j < len(map):
		distance = euclid(map[j], datas[random_index])
		if(min_distance > distance):
			min_distance = distance
			min_index = j
		j += 1
	#update winner
	map[min_index][0] = map[min_index][0] + epsilon(t) * neighbourhood(t, map[min_index], map[min_index]) * (datas[random_index][0] - map[min_index][0])
	map[min_index][1] = map[min_index][1] + epsilon(t) * neighbourhood(t, map[min_index], map[min_index]) * (datas[random_index][1] - map[min_index][1])
	#update all
	for r in range (len(map)):
		for c in range (len(map[r])):
			if(r != min_index):
				map[r][c] = map[r][c] + epsilon(t) * neighbourhood(t, map[min_index], map[r]) * (datas[random_index][c] - map[r][c])
	t += 1
# Write CSV file

kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('resultsqu.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(map)