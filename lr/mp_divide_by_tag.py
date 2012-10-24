import multiprocessing
import os

class MultiProcDivideTags(object):

	'''
	divide ctr logs by ad's tag with Python's 
	multiprocessing module
	'''

	def __init__(self, files, tag_adsf):

		self.files = files
		self.tag_adsf = tag_adsf
		self.tag_ads = {}

	def loadtag_ads(self):

		f = file(self.tag_adsf)

		for line in f:
			if len(line) < 3:
				continue
			
			lines = line.strip().split()
			self.tag_ads[lines[0]] = []
			for i in xrange(1, len(lines)):
				self.tag_ads[lines[0]].append(lines[i])
		print len(self.tag_ads['7'])
		
	def run(self):
		'''
		divide logs by tag and waits for the processes to finish
		'''
		jobs = []
		for f in self.files:
			process = multiprocessing.Process(target=self.worker, args=(f,))
			jobs.append(process)
			process.start()

		for job in jobs:
			job.join()
	
	def worker(self, f):
		fname = file(f) #os.path.basename(f)
		msg = "Starting divide the logs by tag of %s" % fname
		print msg, multiprocessing.current_process().name
		
		for line in fname:
			lines = line.strip().split()
			
			for tag, ads in self.tag_ads.items():
			
				if not tag == '7':
					continue
				if lines[3] in ads:
					#print "%s is in ads " % lines[3]
					out = file("../data/"+f+"_divide_tag_" + tag, 'a')
					out.write(line)
					out.close()


if __name__ == "__main__":
	#files = ["../data/tttttttt20120826"]
	files = ["../data/tttttttt" + str(i) for i in xrange(20120815, 20120824)]
	mpdt = MultiProcDivideTags(files, "../data/tag_ads")
	mpdt.loadtag_ads()
	mpdt.run()
