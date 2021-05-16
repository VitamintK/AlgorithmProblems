T = int(input())
def opp(x):
    if x=='M':
        return 'G'
    else:
        return 'M'
for t in range(T):
    R,C,F,S = map(int, input().split())
    have = []
    want = []
    # G = 0
    components = [[-1 for i in range(C)] for j in range(R)]
    def dfs(r,c,w):
        if components[r][c] != -1:
            return 0
        # print(r,c,R,C)
        if have[r][c] == want[r][c]:
            return 0
        if w != want[r][c]:
            return 0
        a = 1
        components[r][c] = 1
        for dr,dc in [(0,-1), (0,1), (1,0), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C:
                sub = dfs(nr,nc,opp(w))
                a += sub
        return a
    for r in range(R):
        have.append(input())
    for r in range(R):
        want.append(input())
    ans = 0
    for r in range(R):
        for c in range(C):
            wrongs = dfs(r,c,want[r][c])
            if wrongs%2 == 0:
                ans += wrongs//2
            else:
                ans += wrongs//2 + 1
    print(f'Case #{t+1}: {ans}')