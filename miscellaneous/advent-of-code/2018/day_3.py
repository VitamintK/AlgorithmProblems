if False:
	s = set()
	d = set()
	while True:
		try:
			inp = input().split()
			x,y = map(int, inp[2][:-1].split(','))
			w,h = map(int, inp[3].split('x'))

			for i in range(h):
				for j in range(w):
					xp, yp = x+j, y+i
					if (xp, yp) in s:
						d.add((xp, yp))
					s.add((xp, yp))
		except EOFError:
			break
	print(len(d))
else:
	d = dict()
	goodness_of_claims = []
	while True:
		try:
			inp = input().split()
			x,y = map(int, inp[2][:-1].split(','))
			w,h = map(int, inp[3].split('x'))

			good = 1
			for i in range(h):
				for j in range(w):
					xp, yp = x+j, y+i
					if (xp, yp) in d:
						goodness_of_claims[d[(xp, yp)]] = 0
						good = 0 
					d[(xp, yp)] = int(inp[0][1:])-1
			goodness_of_claims.append(good)
		except EOFError:
			break
	for i in range(len(goodness_of_claims)):
		if goodness_of_claims[i]:
			print(i+1)