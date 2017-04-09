## microvave.py
import math

mydict = {1: [1,2,3,4,5,6,7,8,9,0], 2: [2,3,5,6,8,9,0], 3:[3,6,9], 4:[4,5,6,7,8,9,0], 5:[5,6,8,9,0],6:[6,9], 7:[7,8,9,0], 8:[8,9,0], 9:[9], 0:[0]}


def check_valid(k):

	t = str(k)
	if len(t) != 1:

		for i in range(len(t)-1):
			if int(t[i+1]) not in mydict[int(t[i])]:
				return False
		else:
			return True
	else:
		return True

a = int(input())
for i in range(a):
	b = int(input())
	temp3 = []
	for i in range(1000):
		if check_valid(i):
			temp3.append(i)
	temp4 = []
	for i in temp3:
		temp4.append((i, abs(b-i)))

	temp4 = sorted(temp4, key = lambda t: t[1])
	print(temp4[0][0])