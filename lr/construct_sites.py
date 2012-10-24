import cPickle as p

f = file("../week5/grouplarge1000")


site_id_name = []
	
for line in f:
	site_id = line.strip()
	ff = file("/data/tmp/site_name")
	for l in ff:
		lines = l.strip().split()
		if lines[0] == site_id:
			site_id_name.append((site_id, lines[1]))

	
for i in xrange(len(site_id_name)):
	print site_id_name[i][0] + " " + site_id_name[i][1]


print '-' * 20
print len(site_id_name)
out = file("site_id_name.data", 'w')
p.dump(site_id_name, out)
out.close()

data = p.load(open("site_id_name.data", 'rb'))

print len(data)

