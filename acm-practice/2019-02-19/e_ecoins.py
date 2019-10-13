T = int(input())

for t in range(T):
    m, s = map(int, input().split())
    coins = []
    for i in range(m):
        a, b = map(int, input().split())
        coins.append((a,b))

    ans = None
    DP = [[None for i in range(s+1)] for j in range(s+1)]
    DP[0][0] = 0
    for r in range(len(DP)):
        if ans:
            break
        for c in range(len(DP[0])):
            if ans or r*r+c*c>s*s:
                break
            for dr, dc in coins:
                if dr > r or dc > c:
                    continue
                if DP[r-dr][c-dc] is None:
                    continue
                if DP[r][c] is None:
                    DP[r][c] = DP[r-dr][c-dc]+1
                else:
                    DP[r][c] = min(DP[r][c], DP[r-dr][c-dc]+1)
                if r*r+c*c==s*s and ans is None:
                    ans = DP[r][c]
    if ans is None:
        print("not possible")
    else:
        print(ans)
    if t < T-1:
        input()
