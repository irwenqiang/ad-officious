from time import time
tag_ads = {}
f = file("../tag_ads")

cnt = 0
for line in f:
	if len(line) < 3:
		continue
	cnt += 1
	if cnt < 2:
		continue
	#print line
	lines = line.strip().split()
	
	print lines[0]
	#print len(lines)
	for i in xrange(1, len(lines)):
		tag_ads[lines[i]] = None
	break
print len(tag_ads.keys())
print tag_ads

f = file("../week4/code/data/test_f/f/f_20120816")
out = file("data/ta_20120816", 'w')
t = time()
for line in f:
	#print line
	lines = line.strip().split()
	if lines[3] in tag_ads:
		out.write(line)
	#break
out.close()

print time() - t

