import cPickle as p
from time import time

def loaddata():
	t = time()
	f = file("/home/cwq_intern/doing/data/user_to_sites.data")
	data = p.load(f)

	print time() - t
	
	return data
