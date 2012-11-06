def read_csv(unit, filename, infile):

	out = file(infile, "w")
	f = file(filename)
	for line in f:
		if unit in line:
			out.write(line.strip())
			out.write("\n")
	out.close()

def divide_into_weeks(infile, outfile):

	out = file(outfile, "w")
	f = file(infile)
	cnt = 0
	for line in f:
		
		cnt += 1			
		lines = line.strip().split(",")
		#print lines[3], lines[4]
		imp = int(lines[3].replace("\"", "") + lines[4].replace("\"", ""))
		ctr = lines[len(lines)-1]
		
		if len(ctr) <= 0:
			ctr = "0.01%"
		ctr = ctr.replace("%", "").replace("\"", "")	
		if ctr == "":
			ctr = "0.01"
		ctr = float(ctr)

		out.write(str(ctr))
		out.write("\t")
		
		if cnt == 7:
			cnt = 0
			out.write("\n")
	
	out.close()

if __name__ == "__main__":

	#infile = "dale_fm_channel"
	#outfile = "dale_fm_channel_week_ctr"
	infile = "dale_newgroup_home_my_topics"
	outfile = infile + "_ctr"
	outfile2 = ""
	unit = infile
	read_csv(unit, "unit_date_ctr.csv", infile)

	divide_into_weeks(infile, outfile)	

