# -*- coding: utf-8 -*-
f = file("position_day_ctr.xls")


days = ["2012-10-29", "2012-10-30", "2012-10-31", "2012-11-1", "2012-11-3","2012-11-4"]
for line in f:
	lines = line.strip().split()
	print lines[0].encode("gbk")
	break
	
