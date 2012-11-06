# -*- coding=utf-8 -*-
import xlrd
import csv
from datetime import date,timedelta
from recsys.evaluation.ranking import SpearmanRho

date_record = {}


def write_to_file(lst, out, isscale=False):
	
	imax = max(lst)
		
	for i in xrange(len(lst)):
		
		if isscale:
			out.write(str(lst[i] / imax))
		elif not isscale:
			out.write(str(lst[i]))
	
		out.write(" ")
	out.write("\n")

def day_ctr(infile, outfile):

	filename = infile
	out = file(outfile, "w")

	book = xlrd.open_workbook(filename)
	sh = book.sheet_by_index(0)
	
	for i in xrange(sh.nrows):

		row = sh.row_values(i)
		
		if row[6] == u'0.00%':
			print row	
		
		if row[1] in date_record:
			date_record[row[1]].append([row[0], row[2], row[4], row[5], row[6]])
		elif row[1] not in date_record:
			date_record[row[1]] = [[row[0], row[2], row[4], row[5], row[6]]]
	
	cpm = []
	cpm_ctr = []
	com = []
	com_ctr = []
	total_imp = []
	total_ctr = []
	logged_on_user_ctr = []
	anonymous_user_ctr = []
	user_ctr = []
	dates = []
	
	for key, value in date_record.items():

		dates.append(key)

		cpm_imp = 0.0
		cpm_click = 0.0
		com_imp = 0.0
		com_click = 0.0
		total_i = 0.0	
		total_c = 0.0
		
		logged_on_user_imp = 0.0
		logged_on_user_click = 0.0
		anonymous_user_imp = 0.0
		anonymous_user_click = 0.0
		user_imp = 0.0
		user_click = 0.0
				
		for i in xrange(len(value)):
			
			'''	
			upctr =  float(value[i][4].encode("ascii").replace("%", ""))
			
			if upctr > 0.55:
				cnt += 1
				continue
			'''
			
			# no info user
			if value[i][1] == u'\u65e0\u8eab\u4efd\u4fe1\u606f\u7528\u6237':
				continue	
			# normal market
			if value[i][0] == u'\u6b63\u5e38\u6295\u653e':
				cpm_imp += value[i][2]
				total_i += value[i][2]
				cpm_click += value[i][3]
				total_c += value[i][3]
			# complement market
			if value[i][0] == u'\u8865\u4f59\u6295\u653e':
				com_imp += value[i][2]
				total_i += value[i][2]
				com_click += value[i][3]
				total_c += value[i][3]
			# logged on user
			if value[i][1] == u'\u767b\u5f55\u7528\u6237':
				user_imp += value[i][2]
				user_click += value[i][3]
				logged_on_user_imp += value[i][2]
				logged_on_user_click += value[i][3]
			# anonymous user
			if value[i][1] == u'\u533f\u540d\u7528\u6237':
				user_imp += value[i][2]
				user_click += value[i][3]
				anonymous_user_imp += value[i][2]
				anonymous_user_click += value[i][3]
			
		total_imp.append(total_i)
		total_ctr.append(total_c / total_i)
			
		cpm.append(cpm_imp)	
		cpm_ctr.append(cpm_click / cpm_imp)
		
		com.append(com_imp)
		com_ctr.append(com_click / com_imp)

		user_ctr.append(user_click / user_imp)
		logged_on_user_ctr.append(logged_on_user_click / logged_on_user_imp)	
		anonymous_user_ctr.append(anonymous_user_click / anonymous_user_imp)
					
	write_to_file(total_imp, out)
	#write_to_file(total_ctr, out)
	#write_to_file(cpm, out)
	#write_to_file(cpm_ctr, out, True)
	#write_to_file(com, out)
	#write_to_file(com_ctr, out, True)
	

	write_to_file(user_ctr, out)
	#write_to_file(logged_on_user_ctr, out)
	#write_to_file(anonymous_user_ctr, out)
	#zero = [0.0 for i in xrange(len(user_ctr))]
	#write_to_file(zero, out, False)
	out.close()
	
	#print sorted(dates)					
if __name__ == "__main__":
	infile = "ctrwavedata2.xls"
	outfile = "multivariablectr"
	day_ctr(infile, outfile)
