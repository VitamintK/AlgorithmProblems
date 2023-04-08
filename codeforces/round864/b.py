# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append([int(x) for x in input().split()])
    swaps = 0
    for r in range((n+1)//2):
        if n%2==1 and r==n//2:
            nn=n//2
        else:
            nn=n
        for c in range(nn):
            rr, cc = (n-r-1), (n-c-1)
            if grid[r][c] != grid[rr][cc]:
                swaps += 1
    if swaps > k:
        print("NO")
    else:
        if n%2==1:
            print("YES")
        elif (k-swaps)%2==1:
            print("NO")
        else:
            print("YES")
    
