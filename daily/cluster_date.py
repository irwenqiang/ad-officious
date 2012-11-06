import xlrd
import csv
from datetime import date,timedelta
from recsys.evaluation.ranking import SpearmanRho

day = []


def day_ctr(infile, outfile):

	filename = infile
	out = file(outfile, "a")

	book = xlrd.open_workbook(filename)
	#print "The number of worksheets is", book.nsheets
	#print "Worksheet name(s):", book.sheet_names()

	sh = book.sheet_by_index(0)
	#print sh.name, sh.nrows, sh.ncols

	day_ctr = [[0.0,0.0] for i in xrange(7)]

	cnt = 6

	for i in xrange(sh.nrows):
		
		#if i < 2205:
		#if i < 2205 and i >= 735:
		#if i < 2950 and i >= 2205:
		#if i >= 629:
		if True:
			print "*"
			row = sh.row_values(i)

			'''	
			print row
			print row[4]
			print row[5]
			'''

			day_ctr[cnt][0] += float(row[4])
			day_ctr[cnt][1] += float(row[5])
			
			cnt += 1
			if cnt == 7:
				cnt = 0
		
	ctr = []
	print day_ctr
	for i in xrange(len(day_ctr)):

		ctr.append(float(day_ctr[i][1]) / float(day_ctr[i][0]))
		out.write(str(float(day_ctr[i][1]) / float(day_ctr[i][0])))
		out.write(" ")
	out.write("\n")	
	out.close()
	print ctr


def cpm_imp(infile, outfile):
	book = xlrd.open_workbook(infile)

	out = file(outfile, "w")
	#print "The number of worksheets is", book.nsheets
	#print "Worksheet name(s):", book.sheet_names()

	sh = book.sheet_by_index(0)
	#print sh.name, sh.nrows, sh.ncols

	plot = []
	cnt = 0
	for i in xrange(sh.nrows):
		cpm = sh.row_values(i)
		print cpm
	
		#if cpm[0] == u'\u8865\u4f59\u6295\u653e':
		if cpm[0] == u'\u6b63\u5e38\u6295\u653e':
			cnt += 1
			#print cpm[6]
			plot.append([cpm[4], cpm[6]])
	print cnt
	plot.sort(cmp=lambda x,y:cmp(x[0],y[0]))
	#print plot	
	for i in xrange(len(plot)):
		out.write(plot[i][1])
		out.write(" ")	
	out.close()


	
def user_imp(infile, outfile):
	book = xlrd.open_workbook(infile)

	out = file(outfile, "w")
	#print "The number of worksheets is", book.nsheets
	#print "Worksheet name(s):", book.sheet_names()

	sh = book.sheet_by_index(0)
	#print sh.name, sh.nrows, sh.ncols

	plot = []
	cnt = 0
	for i in xrange(sh.nrows):
		cpm = sh.row_values(i)
		print cpm	
		#if cpm[2] == u'\u767b\u5f55\u7528\u6237':
		if cpm[2] == u'\u533f\u540d\u7528\u6237':
			cnt += 1
			#print cpm[6]
			plot.append([cpm[4], cpm[6]])
	print cnt
	plot.sort(cmp=lambda x,y:cmp(x[0],y[0]))
	#print plot	
	for i in xrange(len(plot)):
		out.write(plot[i][1])
		out.write(" ")	
	out.close()

if __name__ == "__main__":
	infile = "ctrwavedata2.xls"
	#infile = "test/xaa"
	outfile = "user_ctr"

	#day_ctr(infile, outfile)
	#cpm_imp(infile, outfile)
	user_imp(infile, outfile)
	
