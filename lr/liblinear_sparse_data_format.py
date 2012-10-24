# construct the site_id and its corresponding index(begin from 1)
import multiprocessing  
import sys
class DataFormater(object):

	'''
	construct the liblinear traindata format
	'''

	def __init__(self, files, site_indexf):

		self.files = files
		self.site_indexf = site_indexf
		self.site_index = {}

	def load_site_index(self):
		
		f = file(self.site_indexf)
		
		cnt = 1
		for line in f:
			self.site_index[line.strip()] = str(cnt)
			cnt += 1
	
	def run(self):

		jobs = []

		for f in self.files:
			process = multiprocessing.Process(target=self.worker, args=(f,))
			jobs.append(process)
			process.start()

		for job in jobs:
			job.join()

	def worker(self, f):
		
		fname = file(f)

		msg = "Starting construct liblinear traindata format from %s" % fname
		print msg, multiprocessing.current_process().name
		#print "fname: " + f[21:]
		
		out = file("../data/linearformat/" + f[21:], 'w')
		
		cnt = 0
		for line in fname:
			cnt += 1
			if cnt % 1000000 == 0:
				print cnt
			lines = line.strip().split()
			lines = sorted(lines)

			#print lines
			#input()
			if lines[0] == '0':
				out.write("-1 ")
			elif lines[0] == '1':
				out.write("+1 ")
			for i in xrange(1, len(lines)):
				if not lines[i] in self.site_index:
					continue
				try:
					out.write(self.site_index[lines[i]])
					out.write(":")
					out.write("1")
					out.write(" ")
				except KeyError:
					print "the error is KeyError:"
					print lines[i]
					#sys.exit()
				
			out.write("\n")
		
		out.close()
		

if __name__ == "__main__":

	files = ["../data/site_isclick/201208" + str(i) + "_tag_7" for i in xrange(26, 32)]
	
	df = DataFormater(files, "../data/sites_1000")

	df.load_site_index()

	df.run()

