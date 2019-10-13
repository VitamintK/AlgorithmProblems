n = int(input())
As = [int(x) for x in input().split()]
Bs = [int(x) for x in input().split()]
scores = [0,0]
As.sort()
Bs.sort()
for i in range(n*2):
	is_a = i%2==0
	if len(As) == 0:
		if is_a:
			Bs.pop()
		else:
			scores[1] += Bs.pop()
		#scores[i%2] += Bs.pop()
	elif len(Bs) == 0:
		if is_a:
			scores[0] += As.pop()
		else:
			As.pop()
		#scores[i%2] += As.pop()
	else:
		if As[-1] > Bs[-1]:
			if is_a:
				scores[i%2] += As.pop()
			else:
				As.pop()
		else:
			if is_a:
				Bs.pop()
			else:
				scores[1] += Bs.pop()
#			scores[i%2] += Bs.pop()
print(scores[0]-scores[1])

