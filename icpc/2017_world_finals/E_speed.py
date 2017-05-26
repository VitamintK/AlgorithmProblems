n, T = map(int, input().split())
ss = []
ds = []
for i in range(n):
	d, s = map(int, input().split())
	ss.append(s)
	ds.append(d)

def calc(ds, ss, c):
	#print(c)
	if min(ss) + c <= 0:
		return 100000000000000
	#for a, b in zip(ds, ss):
	#	print(a, b, c)
	#	print(a/(b+c))
	tt = sum(a/b for a,b in zip(ds, [s+c for s in ss]))
	#print(tt)
	return tt

high = 1e10
low = -1e10
while high - low > 0.000001:
	mid = (high + low)/2
	ttt = calc(ds, ss, mid)
	if ttt > T:
		low = mid
	else:
		high = mid
print(mid)