m, n = map(int, input().split())
grid = []

for i in range(n):
    grid.append(input())
    if 'P' in grid[-1]:
        location = (i, grid[-1].index('P'))

safe = [[1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'T':
            for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_x = j+x
                new_y = i+y
                if 0 <= new_x < m and 0<=new_y < n:
                    safe[new_y][new_x] = 0

stack = [location]
G = 0
been = set()
while(len(stack) > 0):
    old_y, old_x = stack.pop()
    #print(old_x, old_y)
    if (old_y, old_x) in been:
        continue
    been.add((old_y, old_x))
    if grid[old_y][old_x] == 'G':
        G+= 1
    if not safe[old_y][old_x]:
        continue
    for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
        #print(old_x+x, old_y+y)
        new_x = old_x + x
        new_y = old_y + y
        if 0 <= new_x < m and 0<=new_y < n and (new_y, new_x) not in been and grid[new_y][new_x] != '#':
            stack.append((new_y, new_x))

print(G)
