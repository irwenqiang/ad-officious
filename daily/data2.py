f = file("item_time_relationship")
threadshold = [i for i in xrange(5,65, 5)]

items = []
for line in f:
	items.append(line.strip().split()[1])

print len(items)

f = file("month10ctr.csv")

for line in f:
	lines = line.strip().split(",")
	print lines[0], lines[1], lines[2],lines[4], lines[5]
	item = lines[0].replace("\"", "")
	if item in items:	
		pass
	#print item
	break
	
