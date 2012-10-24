import cPickle as p
from time import time

t = time()

f = file("data/user_to_sites.data")
data = p.load(f)
print len(data.keys())

print time() - t

t = time()
f = file("data/t2a_20120816")
out = file("data/t2ar_20120816_2", 'w')
for line in f:
	lines = line.strip().split()
	uid = lines[1]
	site = lines[4]
	times = "2012-08-16"
	if uid in data:
		for i in xrange(len(data[uid])):
			if site in data[uid][i]:
				#st = data[uid][i].strip().split(":")
				#if times > st[1]:
				out.write(line)

out.close()
print time() - t
				
			
