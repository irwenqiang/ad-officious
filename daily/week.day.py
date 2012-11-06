f = file("week.day.csv")
cnt = 0
out = file("week.day", "w")

for line in f:
	if cnt % 7 == 0:
		cnt = 0
		out.write("\n")
	lines = line.strip().split(",")
	ctr = lines[3].replace("\"","").replace("%", "")
	cnt += 1
	out.write(ctr)
	out.write(" ")

out.close()
