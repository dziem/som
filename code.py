import csv
import sys
import math
import numpy as np
import random 

#const
tmax = 100
epsilon0 = 0.01
unit = 8
sigma0 = unit - 1

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
map = []             
for i in range (0, unit):
	new = []
	for j in range (0, 2):
		foo = random.uniform(3, 18)
		new.append(foo)
	map.append(new)
rows_num = len(datas) - 1
map_def = map #try bits
print(map_def) #try bits
print('----------') #try bits
t = 0
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
	#update all
	for r in range (len(map)):
		for c in range (len(map[r])):
			map[r][c] = map[r][c] + epsilon(t) * neighbourhood(t, map[min_index], map[r]) * (map[r][c] - datas[random_index][c])
	t += 1
print(map)
# Write CSV file

kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('result.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(map)
	