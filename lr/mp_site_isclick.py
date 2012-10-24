import cPickle as p
import multiprocessing

class SiteIsClick(object):
	
	'''
	transform the ctr log to site v.s. ctr log
	'''
	
	def __init__(self, files, user_sitesf):

		self.files = files
		self.user_sitesf = user_sitesf
		self.user_sites = {}

	def load_user_sites(self):

		f = file(self.user_sitesf)

		self.user_sites = p.load(f)
		print len(self.user_sites)
	
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
		
		msg = "Starting transform the ctr logs into site vs ctr logs of %s" % fname		
		print msg, multiprocessing.current_process().name
		#print f[16:25] + f[-5:]
		#../data/tttttttt20120823_divide_tag_7
		out = file("../data/site_isclick/" + f[16:25]+f[-5:], 'w')
		#return
		for line in fname:

			lines = line.strip().split()
			#print lines
			
			if not lines[1] in self.user_sites:
				continue

			for i in xrange(len(self.user_sites[lines[1]])):
				out.write(self.user_sites[lines[1]][i])
				out.write(" ")

			
			out.write(lines[0])
			out.write("\n")
			
		out.close()


if __name__ == "__main__":

	files = ["../data/tttttttt201208"+str(i)+"_divide_tag_7" for i in xrange(26, 32)]
	sic = SiteIsClick(files, "../data/user_to_site_1000.data")
	sic.load_user_sites()
	sic.run()

