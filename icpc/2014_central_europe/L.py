a = int(input())
for i in range(a):
	b = int(input())	
	temp = []
	for i in range(b):
		temp2 =[]
		for i in range(3):
			temp2.append(int(input()))
		temp.append(temp2)
temp3 = []
for i in temp:
	temp3.append(tuple(i))

temp3 = sorted(temp3, key = lambda t: (t[0]))
while(True):
if temp3[0][0] == 1:
	return max([i[2] for i in temp3])
else:
	for i in temp3:
		i[2] = i[2] - 1
		i[0] = i[0] -1

