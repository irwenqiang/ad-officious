user_ctr = {}

f = file("data/t2a_20120816")

for line in f:
	lines = line.strip().split()
	if lines[1] in user_ctr:
		if lines[0] == '0':
			user_ctr[lines[1]][0] += 1
		if lines[0] == '1':
			user_ctr[lines[1]][1] += 1
	
	if not lines[1] in user_ctr:
		user_ctr[lines[1]] = [0, 0]
	

out = file("data/t2a_ctr_20120816", 'w')
for user, ctr in user_ctr.items():
	out.write(user)
	out.write(" ")
	out.write(str(ctr[0]))
	out.write(" ")
	out.write(str(ctr[1]))
	out.write(" ")
	clicks = ctr[1]
	imps = ctr[0]
	
	if imps ==0 :
		imps = 1
	out.write(str( float(clicks) / float(imps)))
	out.write("\n")
	
			
