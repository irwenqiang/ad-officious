import cPickle as p
from time import time
filename = "/data/tmp/user_to_site"
out_user_to_sites = "data/user_to_sites.data"

f = file(filename)
#lst = []
user_to_sites = {}

print 'doing '
t = time()
for line in f:
	#print line
	#input()
	lines = line.strip().split()
	#lst.append(line)
	if lines[0] in user_to_sites:
		user_to_sites[lines[0]].append(lines[1]+":" +lines[2])
	else:
		user_to_sites[lines[0]] = [lines[1] + ":" + lines[2]]
	#del lines	
	#print user_to_sites

print time() - t
#input()
f.close()
del line
#print '--'
print len(user_to_sites.keys())
#input()
f = file(out_user_to_sites, 'w')
p.dump(user_to_sites, f)
f.close()


