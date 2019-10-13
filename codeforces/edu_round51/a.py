n = int(input())

for i in range(n):
	s = input()
	upp = 0
	low = 0
	dig = 0
	import string

	for j in s:
		if j in string.ascii_lowercase:
			low+=1
		if j in string.ascii_uppercase:
			upp+=1
		if j in string.digits:
			dig+=1

	q = []
	if upp == 0:
		q.append('A')
	if low == 0:
		q.append('a')
	if dig == 0:
		q.append('0')

	for j in range(len(s)):
		if len(q) == 0:
			break
		if s[j] in string.ascii_lowercase:
			if low > 1:
				s[j] = q.pop()
		elif s[j] in string.ascii_uppercase:
			if upp > 1:
				s[j] = q.pop()
		elif s[j] in string.digits:
			if dig > 1:
				s[j] = q.pop()

	print(s)