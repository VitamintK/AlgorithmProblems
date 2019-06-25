# small tests only

def move(grid, r,c, v):
    grid = [[x for x in r] for r in grid]
    if grid[r][c] != '.':
        return 'lose'
    grid[r][c] = 'X'
    if v:
        rp = r-1
        while rp >= 0:
            if grid[rp][c] == '.':
                grid[rp][c] = 'X'
            elif grid[rp][c] == '#':
                return 'lose'
            else:
                break
            rp -= 1
        rp = r+1
        while rp < R:
            if grid[rp][c] == '.':
                grid[rp][c] = 'X'
            elif grid[rp][c] == '#':
                return 'lose'
            else:
                break
            rp += 1
    else:
        cp = c-1
        while cp >= 0:
            if grid[r][cp] == '.':
                grid[r][cp] = 'X'
            elif grid[r][cp] == '#':
                return 'lose'
            else:
                break
            cp -= 1
        cp = c+1
        while cp < C:
            if grid[r][cp] == '.':
                grid[r][cp] = 'X'
            elif grid[r][cp] == '#':
                return 'lose'
            else:
                break
            cp += 1
    return grid

def pretty(grid):
    s = ''
    for r in grid:
        s+= ''.join(r) + '\n'
    return s

def stringify(grid):
    s = ''
    for r in grid:
        s += ''.join(r)
    return s


my_memo = dict()
def my_turn(grid):
    #returns true if grid is winnable (has a move that I can pick which is win)
    # print("My turn:\n{}".format(pretty(grid)))
    sg = stringify(grid)
    if sg in my_memo:
        return my_memo[sg]
    grids = []
    for r in range(R):
        for c in range(C):
            g = move(grid,r,c,1)
            if g != 'lose':
                grids.append(g)
            g = move(grid,r,c,0)
            if g != 'lose':
                grids.append(g)
    results = [your_turn(p) for p in grids]
    ans = len([x for x in results if x])
    my_memo[sg] = ans
    print(pretty(grid))
    print(ans)
    print("PRINTING WINNERS")
    for x in range(len(results)):
        if results[x]:
            print(pretty(grids[x]))
    # print(grid)
    return ans

your_memo = dict()
def your_turn(grid):
    # returns true if grid is not winnable for you (no move picked will win for you)
    # print("Your turn:\n{}".format(pretty(grid)))
    sg = stringify(grid)
    if sg in your_memo:
        return your_memo[sg]
    grids = []
    for r in range(R):
        for c in range(C):
            g = move(grid,r,c,1)
            if g != 'lose':
                grids.append(g)
            g = move(grid,r,c,0)
            if g != 'lose':
                grids.append(g)
    results = [my_turn(p) for p in grids]
    # print(grid)
    your_memo[sg] = all(results)
    return all(results)

T = int(input())
for t in range(T):
    R, C, = map(int, input().split())
    grid = []
    for i in range(R):
        grid.append(input())
    print("Case #{}: {}".format(t+1, my_turn(grid)))