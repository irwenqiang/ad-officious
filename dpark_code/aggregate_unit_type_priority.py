from dpark import DparkContext

def map_unit_type_priority(line):
	
	#76      COMPLEMENT      2       3       15715   60      0.00381800827235 
	line = line.strip().split()
	return (line[0], line[1], line[2]), [int(line[4]), int(line[5]), float(line[6])]

def reduce_by_key(x, y):
	
	for i in xrange(len(x)):
		x[i] += y[i]
	return x


def map_to_string(line):

	#(('76', 'COMPLEMENT', '2'), [15715, 60, 0.00381800827235])
	imp = float(line[1][0])
	click = float(line[1][1])
	if imp < 1.0:
		imp = 1.0
	
	ctr = click / imp
	return "\t".join([line[0][0], line[0][1], line[0][2], str(line[1][0]), str(line[1][1]), str(ctr)])

def main(infile, outfile):

	ctx = DparkContext()

	rdd = ctx.textFile(infile)

	rdd = rdd.map(map_unit_type_priority)

	rdd = rdd.reduceByKey(reduce_by_key)

	rdd = rdd.map(map_to_string)

	rdd.saveAsTextFile(outfile)	


if __name__ == "__main__":

	infile = "/home/cwq_intern/Otc/code/bi/results/"
	outfile = "aggregate_results"
	main(infile, outfile)


