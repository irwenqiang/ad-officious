import csv
from time import time 
t = time() 

def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line

for data in import_text('data_format', ' '):
    print (data)

print "total run time:"
print time()-t 
