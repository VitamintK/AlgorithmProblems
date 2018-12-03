if False:
	a = 0
	b = 0

	from collections import Counter

	while True:
		try:
			s = input()
			c = Counter(s)
			cnts = set(c.values())
			if 2 in cnts:
				a += 1
			if 3 in cnts:
				b += 1
		except:
			break

	print(a*b)
else:
	xs = []
	while True:
		try:
			p = input()
			for x in xs:
				cnt = 0
				ans = ""
				for k in range(len(x)):
					if x[k] == p[k]:
						ans+=x[k]
					else:
						cnt += 1
				if cnt == 1:
					print(ans)
					raise ValueError
			xs.append(p)
		except:
			break