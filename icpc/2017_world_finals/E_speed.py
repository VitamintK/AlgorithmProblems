#read in inputs
n, T = map(int, input().split())
ss = [] #contains all "s_i" values, in order of input
ds = [] #contains all "d_i" values, in the same order^
for i in range(n):
	d, s = map(int, input().split())
	ss.append(s)
	ds.append(d)

def calc(ds, ss, c):
	"""Given a guess for the value of c, return what the time of the whole trip would have been"""
	if min(ss) + c <= 0:
		#If speed at any point would have been 0 or negative, the trip would take infinity time to complete.
		return 100000000000000
	tt = sum(a/b for a,b in zip(ds, [s+c for s in ss]))
	return tt

#Binary search: keep guessing values of C, and check to see if the resulting total trip time would be greater than or less than the actual T.
#Then guess again - lower or higher, accordingly.
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