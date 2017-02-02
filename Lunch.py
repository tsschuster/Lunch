import numpy as np
import random

data_file = open('database.txt', 'r')
previous_file = open('previous.txt', 'r+')

data = []
previous = []
for line in data_file:
    if line[0] == '#':
        continue
    data.append(line.split(','))

for line in previous_file:
    previous.append(line.split(',')[0][:-1])


found = False
while not found:
    pick = random.randint(0, len(data)-1)
    found = True
    for prev in previous[-3:]:
        #print data[pick][0]
        #print prev
        #print 
        if data[pick][0] == prev:
            found = False
            
print "GO TO %s" % data[pick][0]
previous_file.write("%s\n"%data[pick][0])
previous_file.close()
data_file.close()
