n, m = map(int, input().split())
grid = []
for i in range(n):
	grid.append(input())
	if grid[-1].find('S') > -1:
		S = (i, grid[-1].find('S'))
	if grid[-1].find('E') > -1:
		E = (i, grid[-1].find('E'))

string = input()

directions = []
def all_permutations(seq):
	if len(seq) == 0:
		yield []
	for i in seq:
		for p in all_permutations([x for x in seq if x!=i]):
			yield [i] + p

d_map = [(0,-1), (1,0), (0,1), (-1,0)]
ans = 0
for p in all_permutations([0,1,2,3]):
	#0 goes in direction d_map[p[0]]
	cr = S[0]
	cc = S[1]
	for i in string:
		cr = cr + d_map[p[int(i)]][0]
		cc = cc + d_map[p[int(i)]][1]
		if cr >= n or cr < 0 or cc >= m or cc < 0 or grid[cr][cc] == "#":
			break
		if grid[cr][cc] == "E":
			ans += 1
			break
		

print(ans)