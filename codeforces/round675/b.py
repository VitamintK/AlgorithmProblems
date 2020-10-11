T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append([int(x) for x in input().split()])
    def get_neighbs(i,j):
        neighbs = set([(n-i-1, j), (i,m-j-1), (n-i-1, m-j-1), (i,j)])
        # print(neighbs)
        return [mat[i][j] for i,j in neighbs]
    ans = 0
    for i in range((n+1)//2):
        for j in range((m+1)//2):
            neighbs = get_neighbs(i,j)
            neighbs.sort()
            mid = neighbs[len(neighbs)//2]
            a = sum(abs(x-mid) for x in neighbs)
            mid = neighbs[(len(neighbs)-1)//2]
            b = sum(abs(x-mid) for x in neighbs)
            ans += min(a,b)
    print(ans)