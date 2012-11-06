from datetime import date,timedelta

def isweekend(fd, td):
		
	fds = fd.split("-")
	tds = td.split("-")
	
	fromdate = date(int(fds[0]),int(fds[1]),int(fds[2]))
	todate = date(int(tds[0]), int(tds[1]), int(tds[2]))
	
	daygenerator = (fromdate + timedelta(x + 1) for x in xrange((todate - fromdate).days))	
	weekend = []
	for day in daygenerator:
		 if day.weekday() < 5:
			thedate = date(day.year, day.month, day.day)
			#print thedate
			weekend.append(thedate)
			
	return weekend



f = file("ctr.csv")
startdate = "2012-10-1"
todate = "2012-10-31"
#weekend = [] 
weekend = isweekend(startdate, todate)
#print weekend
date_ctr = {}
for line in f:
	lines = line.strip().split(",")
	
	idate = lines[0].replace("\"", "")
	ctr = lines[3].replace("\"", "").replace("%", "")
	hour = lines[1].replace("\"", "")
	
	idates = idate.strip().split("-")
	thedate = date(int(idates[0]), int(idates[1]), int(idates[2]))
	#print date, ctr, hour
	if thedate in weekend:
		continue
	
	if idate not in date_ctr:
		date_ctr[idate] =[(hour,ctr)]
	elif idate in date_ctr:
		date_ctr[idate].append((hour, ctr))	
	

for key, value in date_ctr.items():
	#print key
	for i in xrange(len(value)):
		print value[i][1],
	print "\n"	
