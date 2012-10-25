import os
import shutil

def divide_dir():
	subdir = [1, 3, 5, 7]
	root = "data/2012-10-"
	for i in xrange(1, 16):
		if i < 10:
			fn = "0" + str(i)
		else:
			fn = str(i)
			
		if not os.path.exists(root + fn):
			os.makedirs(root + fn)
			for j in subdir:
				os.makedirs(root + fn + "/" + str(j))

	datapath = "/data/ereborlog/"
	for filename in os.listdir(datapath):
		if len(filename) == 10:
		
			for f in os.listdir(datapath + filename):

				if int(f[0:4]) <= 1:
					print f
					shutil.copy(datapath + filename + "/" + f, "data/" + filename + "/1/" + f)
					continue
				
				if int(f[0:4]) <= 3:
					shutil.copy(datapath + filename + "/" + f, "data/" + filename + "/3/" + f)
					continue

				if int(f[0:4]) <= 5:
					shutil.copy(datapath + filename + "/" + f, "data/" + filename + "/5/" + f)
					continue

				if int(f[0:4]) <= 7:
					shutil.copy(datapath + filename + "/" + f, "data/" + filename + "/7/" + f)
					continue

if __name__ == "__main__":
	divide_dir()
