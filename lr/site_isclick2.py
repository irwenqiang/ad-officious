import cPickle as p
import os
from time import time

t = time()

f = file("../data/user_to_site_1000.data")

data = p.load(f)

print time() - t

t = time()
filesub = "20120816"
idir = "../data/" + filesub + "/"
#filesub = "20120815"
for filename in os.listdir(idir):
	tt = time()
	if filesub in filename:
		print filename[9:]

	f = file(idir + filename)

	out = file("../data/"+filesub+"/sites_ctr/" + filename[9:], 'w')
	for line in f:

		lines = line.strip().split()
		if not lines[1] in data:
			continue

		#print str(data[lines[1]])
		#print "*" * 20
		#for i in xrange(len(data[lines[1]])):
		#	out.write(data[lines[1]][i])
		#	out.write(" ")

		out.write(data[lines[1]])
		out.write(" ")
		out.write(lines[0])
		out.write("\n")

	out.close()
	
	print time() - tt

print time() - t
