#good problem! stars and bars
T = int(input())
from collections import Counter
for t in range(T):
	inp = [int(x) for x in input().split()]
	n, k = inp[0], inp[1]
	rest = inp[2:]
	#stars and bars-ish.  
	#imagine each segment of black stones as a bar
	#and the white stones are stars.
	#also, we can't have adjacent bars.
	#so we need to give ourself less freedom with the pieces
	#by removing the mandatory "spacer" stars that must exist between each set of neighboring bars
	#from the set of pieces that can be adjusted.

	N = n-(k-1) - sum(rest) + len(rest)#total free "units" - each of which can be populated by a white square or a segment of black squares.
	K = k

	if N < K:
		print(0)
		continue
	num = 1
	for i in range(K+1, N+1):
		num*=i
	for i in range(1, N-K+1):
		num//=i
	print(num)
