import cPickle as p
from time import time

t = time()
user_to_site = p.load(open("../data/user_to_sites.data", 'rb'))
site_id_name = p.load(open("../data/site_id_name.data", 'rb'))

print 'load finished '
print time() - t

f = file("../data/20120815")
site_ctr = []
t = time()
for line in f:
	lines = line.strip().split()
	uid = lines[1]
	ic = lines[0]

	if uid in user_to_site:
		site_ctr.append((user_to_site[uid], ic))

print 'list finished '
print time() - t

t = time()
out = file("../data/site_ic_20120815", 'w')
for i in xrange(len(site_ctr)):
	out.write(site_ctr[i][0])
	out.write("\n")
	out.write(site_ctr[i][1])

	out.write("\n")

out.close()

print time() - t
