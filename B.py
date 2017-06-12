T = int(input())

def get_stuff(y,x):
	return [(y+y_off, x+x_off) for y_off,x_off in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]]
for t in range(T):
	n, m = map(int, input().split())
	#mx = (0, (0,0))
	#for i in range(n):
	#	for j, v in enumerate(map(int, input().split())):
	#		mx = max(mx, (k,(i,j)))
	g = []
	for i in range(n):
		g.append([int(x) for x in input().split()])
	target = max(max(v for v in r) for r in g)
	gn = [[0]*m for i in range(n)]
	good = False
	its = 0
	if all(all(x == target for x in r) for r in g):
		print(0)
		continue
	while not good:
		good = True
		its += 1
		for y in range(n):
			for x in range(m):
				gn[y][x] = max(g[yy][xx] for yy,xx in get_stuff(y,x) if yy >= 0 and yy < n and xx >= 0 and xx < m)
				if gn[y][x] != target:
					good = False
		g = gn
	print(its)

