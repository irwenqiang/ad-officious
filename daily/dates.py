import datetime

dt = datetime.datetime(2012, 7, 01)
end = datetime.datetime(2012, 11, 4)
step = datetime.timedelta(days=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d'))
    dt += step

for i in xrange(len(result)):
	print "\"" + result[i] + "\"," , 
