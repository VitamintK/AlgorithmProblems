#also a great problem!
#I shall try a recursive, divide-and-conquer-esque solution

from collections import defaultdict

MEMO = defaultdict(int)

def ans(n):
	#n is the number of pairs (not number of people.  not sure which will make more sense.)
	#divide and conquer based off of who person #1 matches with.
	if n in MEMO:
		return MEMO[n]
	if n == 0:
		return 1
	answer = 0
	for i in range(n): #going around the circle clockwise
		answer += ans(i)*ans(n-i-1)
	MEMO[n] = answer
	return answer

a = int(input())
print(ans(a))

while True:
	try:
		blank = input()
		a = int(input())
		print("")
		print(ans(a))
	except Exception as e:
		#print(e)
		break
