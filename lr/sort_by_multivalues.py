'''
20120824
total runs:
802.53946209
'''

from operator import itemgetter, attrgetter  
import os, sys
from time import time


if len(sys.argv) < 2:
	print "usage:"
	print "python sort_by_multivalues.py filename"
	print "e.g. python sort_by_multivalues.py 20120825"
	sys.exit()

filesub = "20120826"

filesub = sys.argv[1]
print "the filename is:" + filesub
print "please enter num to confirm or letter to cancel"
input()

t = time()
print "total runs "
cnt = 0
for filename in os.listdir("/data/" + filesub):
	tt = time()
	cnt += 1
	print str(cnt) + " " + filename + " runs "
	if not filename.isdigit():
		continue
	logs = []	
	f = file("/data/"+filesub+"/" + filename)
	for line in f:
		if len(line) < 3:
			continue
		lines = line.strip().split()
		if lines[1] == '0':
			logs.append([lines[0], int(lines[2]),lines[3], lines[5]])

	logs = sorted(logs, key=itemgetter(1, 2, 3, 1))	

	print "logs length: " + str(len(logs))
	#print len(logs)
	delist = []

	for i in xrange(len(logs)):
		if logs[i][0] == '1':
			if logs[i][1] == logs[i-1][1] and logs[i][3] == logs[i-1][3]:	
				logs[i-1][0] = '1'
			delist.append(logs[i])
		
	for i in delist:
		logs.remove(i)

	out = file("../data/tttttttt" + filesub, 'a')

	for i in xrange(len(logs)):
		out.write(logs[i][0] + " " + str(logs[i][1]) + " " + logs[i][2] + " " + logs[i][3])
		out.write("\n")
	out.close()

	print time() - t
print "total runs "
print time() - t
