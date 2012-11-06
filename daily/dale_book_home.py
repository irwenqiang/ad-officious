f = file("dale_book_home914.csv")
for line in f:
	lines = line.strip().split(",")
	
	#print line
	for i in xrange(len(lines)):
		if "%" in lines[i]:
			print lines[i].replace("\"", "").replace("%", "")+" ", 
