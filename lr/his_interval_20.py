import cPickle as p
from time import time

nums = []

for i in xrange(9):
	nums.append(0)

print nums

f = file("../data/user_to_site_1000.data", 'rb')

t = time()

data = p.load(f)

print time() - t
t = time()

u_160 = []
for key, values in data.items():
	if len(values) < 20:
		nums[0] += 1
	
	if len(values) >= 20 and len(values) < 40:
		nums[1] += 1
	
	if len(values) >= 40 and len(values) < 60:
		nums[2] += 1
	
	if len(values) >= 60 and len(values) < 80:
		nums[3] += 1
	
	if len(values) >= 80 and len(values) < 100:
		nums[4] += 1
	
	if len(values) >= 100 and len(values) < 120:
		nums[5] += 1
	
	if len(values) >= 120 and len(values) < 140:
		nums[6] += 1
	
	if len(values) >= 140 and len(values) < 160:
		nums[7] += 1
	
	if len(values) >= 160:
		nums[8] += 1
		u_160.append(key)


print time() - t

print "*" * 50
print nums
print u_160

out = file("his_user.data", 'w')

p.dump(nums, out)

out.close()
