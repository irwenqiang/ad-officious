from time import time
import cPickle as p
t = time()
site_1000 = {}
f = file("../data/grouplarge1000")
for line in f:
	site_1000[line.strip()] = []

print len(site_1000)

print time() - t

user_to_sites_1000 = {}
f = file("/data/tmp/user_to_site")

t = time()
for line in f:
	lines = line.strip().split()
	if lines[0] in user_to_sites_1000:
		if lines[1] in site_1000:
			user_to_sites_1000[lines[0]].append(lines[1])
	
	else:
		if lines[1] in site_1000:
			user_to_sites_1000[lines[0]] = [lines[1]]

	#print user_to_sites_1000
	
print time() - t

t = time()

f = file("user_to_site_1000.data", 'w')
p.dump(user_to_sites_1000, f)

f.close()

print time() - t
