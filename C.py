T = int(input())
for t in range(T):
	n = int(input())
	g = []
	for i in (0,1):
		g.append(list(map(lambda x: 1 if x=='*' else 0, input())))
	ans = 1e10
	if not any(x and y for x,y in zip(g[0], g[1])):
		ans = [x or y for x,y in zip(*g)].count(1) -1
		if ans == -1:
			ans = 0
	a = 0
	b = 0
	p = 0
	for i in range(n):
		if (g[0][i] == 1 and a) or (g[1][i] == 1 and b):
			p+=1
			a = 0
			b = 0
		if g[0][i] == 1 and a==0:
			a = 1
		if g[1][i] == 1 and b==0:
			b = 1
		
	print(min(ans, p+1))
