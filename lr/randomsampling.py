import random

#data = file("../ntag415_31")
#data = file("../data/linearformat/ttt")
data = file("../liblinear-1.91/41531traindata")

ni = []
pi = []

for line in data:

	if line[:2] == '+1':
		pi.append(line)
	elif line[:2] == '-1':
		ni.append(line)

rsnum = len(ni) / 5

rsni = random.sample(ni, rsnum) 

#out = file("../rsntag_41531", "w")
#out = file("../data/linearformat/rsttt", 'w')
out = file("../liblinear-1.91/41531traindatar", 'w')

for i in xrange(len(pi)):
	out.write(pi[i])
for i in xrange(len(rsni)):
	out.write(rsni[i])

out.close()

