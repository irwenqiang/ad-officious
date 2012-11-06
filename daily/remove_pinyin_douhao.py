from datetime import date,timedelta

def isweekend(fd, td):

        fds = fd.split("-")
        tds = td.split("-")
	
	a = date(2012, 10, 10)
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


f = file("item_ctr_relationship")
threadshold = [i for i in xrange(5,65, 5)]

items = []
for line in f:
        items.append(line.strip().split()[1])


filename = "month10ctr.csv"
#filename = "head.csv"

f = file(filename)

date_record = {}
for line in f:
	lines = line.strip().split(",")
	
	dates = lines[1].replace("\"","")	
	if dates not in date_record:
		if len(lines) == 8:
			date_record[dates] = [[lines[0].replace("\"",""), lines[2].replace("\"",""),(lines[4]+lines[5]).replace("\"",""), lines[6].replace("\"","") ]]
		elif len(lines) == 7:
			date_record[dates] = [[lines[0].replace("\"",""), lines[2].replace("\"",""),(lines[4]).replace("\"",""), lines[5].replace("\"","") ]]
	
	if dates in date_record:
		if len(lines) == 8:
			date_record[dates].append([lines[0].replace("\"",""), lines[2].replace("\"",""),(lines[4]+lines[5]).replace("\"",""), lines[6].replace("\"","") ])
		elif len(lines) == 7:
			date_record[dates].append([lines[0].replace("\"",""), lines[2].replace("\"",""),(lines[4]).replace("\"",""), lines[5].replace("\"","") ])
	
startdate = "2012-10-1"
todate = "2012-10-31"
weekend = isweekend(startdate, todate)

dic_record = {}

#print weekend
for key, value in date_record.items():

	idates = key.strip().split("-")
        thedate = date(int(idates[0]), int(idates[1]), int(idates[2]))
        #print date, ctr, hour
	print "*" * 20
        if thedate in weekend:  
		print key
                continue

	record = []

	for i in xrange(len(value)):
		
		if value[i][0] in items[35:]:
			continue
		
		if int(value[i][2]) < 100:
			continue
		
		record.append([value[i][1],value[i][3], value[i][2]])

	dic_record[key] = record

'''
print "*" * 50
print len(dic_record)
print dic_record["2012-10-20"]
input()
'''

date_hours = []
for key, value in dic_record.items():
	print key
	#for i in xrange(len(value)):
	#	print value[i]
	#break
	
	
	hours = [[0, 0] for i in xrange(24)]
	#print key
	cnt = 0
	for i in xrange(len(value)):
		cnt += 1
		if cnt % 50 == 0:
			pass
			#input()
		hours[int(value[i][0])][0] += int(value[i][1])
		hours[int(value[i][0])][1] += int(value[i][2])
		#print hours

	date_hours.append(hours)
	#print date_hours
out = file("month10.ctr", "w")
for i in xrange(len(date_hours)):	
	#print date_hours[i]
	for j in xrange(len(date_hours[i])):
		out.write(str(float(date_hours[i][j][0]) / float(date_hours[i][j][1])))
		out.write(" ")
	out.write("\n")
out.close()

