
sites = {}

filename = "../data/grouplarge1000"

f = file(filename)

for line in f:
	sites[line.strip()] = 0


print sites

print len(sites)

site = "103723"
if site in sites:
	sites[site] = 1

input()

print sites


