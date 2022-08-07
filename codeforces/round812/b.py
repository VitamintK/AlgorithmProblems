import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    decrease_encountered = False
    ans = "YES"
    for i in range(1,n):
        if xs[i] > xs[i-1]:
            if decrease_encountered:
                ans = "NO"
                break
        if xs[i] < xs[i-1]:
            decrease_encountered = True
    print(ans)