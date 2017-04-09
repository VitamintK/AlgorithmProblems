n = int(input())
companies = []
for i in range(n):
	asdf = input().split()
	for i in range(1,len(asdf)):
		asdf[i] = int(asdf[i])
	companies.append(asdf)
import math
while(True):
	try:
		inps = [int(x) for x in input().split()]
		weight = inps[0] * inps[1] * inps[2]
		mincost = 1000000000000
		for c in companies:
			if weight >= c[1]:
				nmincost = math.ceil(weight/c[2])
			else:
				nmincost = inps[3]
			nmincost = max(nmincost, inps[3])
			if nmincost < mincost:
				mincost = nmincost
				ans = c[0]
		print(ans, mincost)
	except Exception as e:

		break
