import cPickle as p
import os, sys
from time import time

if len(sys.argv) < 2:
	print "usage:"
	print "python site_isclick.py filename"
	print "python site_isclick.py"
	sys.exit()

filesub = sys.argv[1]

print "the filename is:" + filesub
print "please enter num to confirm or letter to cancel"
input()

t = time()

f = file("../data/user_to_site_1000.data")

data = p.load(f)
#data = []
print "data length"
print len(data)

input()
print time() - t

t = time()


idir = "../data/"+filesub+"/"

for filename in os.listdir(idir):
	tt = time()
		
	if not filename == (filesub + '_tagtttttt7'):
		continue

	f = file(idir + filename)

	out = file("../data/"+filesub+"/sites_ctr/" + filename[9:], 'w')
	#input()
	for line in f:

		lines = line.strip().split()
		if not lines[1] in data:
			continue

		#print str(data[lines[1]])
		#print "*" * 20
		for i in xrange(len(data[lines[1]])):
			out.write(data[lines[1]][i])
			out.write(" ")

		
		out.write(lines[0])
		out.write("\n")

	out.close()
	
	print time() - tt

print time() - t
