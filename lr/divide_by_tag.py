'''
total runs
548.778880119
'''
from time import time
import sys
if len(sys.argv) < 2:
	print "usage:"
	print "python divide_by_tag.py filename"
	print "python divide_by_tag.py 20120826 e.g."
	sys.exit()


filesub = sys.argv[1]
print "the filename is :" + filesub
print "please enter num to confirm or letter to cancel"
input()

t = time()
tag_ads = {}
f = file("../data/tag_ads")
cnt = 0
for line in f:
	if len(line) < 3:
		continue
	
	lines = line.strip().split()
	tag_ads[lines[0]] = []
	for i in xrange(1, len(lines)):
		tag_ads[lines[0]].append(lines[i])

print len(tag_ads['7'])


#f = file("../data/"+filesub+"/"+filesub)
f = file("../data/tttttttt" + filesub)
cnt = 0

for line in f:
	cnt += 1
	if cnt % 100000 == 0:
		print time() - t
	lines = line.strip().split()
	for tag, ads in tag_ads.items():
		#print lines[3]
		#print tag
		#input()
		#print ads
		#input()
		if not tag == '7':
			continue
		if lines[3] in ads:
			#print "%s is in ads " % lines[3]
			out = file("../data/"+filesub+"/"+filesub+"_tagtttttt" + tag, 'a')
			out.write(line)
			out.close()

print time() - t

print len(tag_ads)
