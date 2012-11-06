#0pen file to read
from time import time
t = time()
f = file('data_format', 'r')

# iterate over the lines in the file
for line in f:
    # split the line into a list of column values
    columns = line.split(',')
    # clean any whitespace off the items
    columns = [col.strip() for col in columns]

    # ensure the column has at least one value before printing
    if columns:
        print "first", columns[0]  # print the first column
        print "last", columns[-1] # print the last column

print 'total comsume time:'
print time() - t
