from dpark import DparkContext
import re
from time import time 
import sys
import os


def divide_csv(line):
	
	lines = line.strip().split("\t")
	result = "\t".join([lines[3], lines[4], lines[8], lines[9], lines[10], lines[11], lines[12]])
	results = [lines[3], lines[4], lines[8], lines[9], lines[10], lines[11], lines[12]]
	return lines[8], results

def remove_some_bid_unitid(line):

	lines = line.strip().split("\t")
	try:
		if not (lines[4] == '0' or lines[9] == '128' or int(lines[12]) > 4):
			return True
		
		return False
	except:
		print "exception"
		print len(lines)	

def divide_txt(line):
	
	lines = line.strip().split("\t")
	result = "\t".join([lines[0], lines[1], lines[2]])

	return lines[0], lines[1:]

def join_element(line):

	result = []
	[result.extend(el) for el in line]
	
	return result

def map_unit_type(line):

	result = []
	result.extend(re.findall(r'(\w+)',line[0]))
	for i in xrange(len(line[1])):
		tmp = []
		tmp.extend(re.findall(r'(\w+)',line[1][i][1][0]))
		tmp.extend(re.findall(r'(\w+)',line[1][i][1][4]))
		tmp.extend(re.findall(r'(\w+)',line[1][i][1][6]))
		tmp.extend(re.findall(r'(\w+)',line[1][i][1][7]))
		tmp.extend(re.findall(r'(\w+)',line[1][i][1][8]))

		result.append(tmp)

	return result

def flat_map_unit_type_priority(line):
	#print "i" * 50
	#print line
	#print "2" * 50
	#print [(line[0],line[1],line[2][0]),line[2][1:]]

	for i in xrange(2, len(line)):
		yield [(line[0],line[1],line[i][0]),line[i][1:]]

def map_value_unit_type_priority(line):
	#print "+" * 50
	#print line[0]
	#['1', '1', '0'] 
	#[8, 2, 8, 0, 0.0]
	cluster = 0
	imp = 0
	click = 0
	ads = []
	for i in xrange(len(line)):
		ads.append(line[i][0])
		cluster = int(line[i][1])
		imp += int(line[i][2])
		click += int(line[i][3])

	if imp == 0:
		imp = 1
	return [len(set(ads)), cluster, imp, click, float(click) / imp]


def map_unit_type_priority(line):
	#(('77', 'COMPLEMENT', '2'), [8, 2, 8, 0, 0.0])
	#77\tCOMPLEMENT\t2\t8\t2\t8\t0\t0.0
	return "\t".join([line[0][0], line[0][1], line[0][2], str(line[1][0]), str(line[1][1]), str(line[1][2]), str(line[1][3]), str(line[1][4])])



def main(txt, infile, outfile):
	
	ctx = DparkContext()
	csvfilename = infile
	txtfilename = txt 

	txt_rdd = ctx.textFile(txtfilename)

	txt_rdd = txt_rdd.map(divide_txt)
	#('5988', ['2', 'CPM']) 
	csv_rdd = ctx.textFile(csvfilename, splitSize=64<<20) 
	#print csv_rdd.take(100)
	csv_rdd = csv_rdd.filter(remove_some_bid_unitid)

	csv_rdd = csv_rdd.map(divide_csv)	
	#('6379', ['-1', '1236054964187470000', '6379', '77', '1', '1', '0'])
	record_rdd = txt_rdd.join(csv_rdd)
	#('6370', (['2', 'COMPLEMENT'], ['-1', '8183016859528920000', '6370', '86', '3', '1', '0']))
	record_rdd = record_rdd.mapValue(join_element)
	#('6370', ['2', 'COMPLEMENT', '-1', '8183016859528920000', '6370', '86', '3', '1', '0']) 
	record_rdd = record_rdd.groupBy(lambda line : str(line[1]).split()[5] + str(line[1]).split()[1])

	#print record_rdd.take(1)
	record_rdd = record_rdd.map(map_unit_type)
	#print record_rdd.take(1)
	record_rdd = record_rdd.flatMap(flat_map_unit_type_priority)
	#print record_rdd.take(5)
	record_rdd = record_rdd.groupByKey()
	#print "*" * 50
	#print record_rdd.take(5)

	record_rdd = record_rdd.mapValue(map_value_unit_type_priority)
	#print "#" * 50
	#print record_rdd.take(5)
	record_rdd = record_rdd.map(map_unit_type_priority)
	#print "$" * 50
	#print record_rdd.take(5)

	# unit	type	prioritt	cluster	n_ad	n_imp	n_click	ctr
	record_rdd.saveAsTextFile(outfile)

	
if __name__ == "__main__":

	if len(sys.argv) < 2:   
		print "infile and outfile"
		sys.exit()
	
	datadir = sys.argv[5]
	outfile = sys.argv[6]
	print datadir
	print outfile

	#sys.exit()

	txt = "/home/cwq_intern/Otc/code/bi/a"
	#datadir = "/home/cwq_intern/Otc/code/bi/tools/data"
	#datadir = "/data/ereborlog/2012-10-01/"
	#datadir = "/home/cwq_intern/Otc/code/bi/data/4"
	#outfile = "t"
	#print filename
	main(txt, datadir, outfile)
	

