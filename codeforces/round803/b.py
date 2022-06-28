import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    if k == 1:
        if n%2==1:
            print(n//2)
        else:
            print((n-1)//2)
    else:
        ans = 0
        for i in range(1,n-1):
            if xs[i] > xs[i-1]+xs[i+1]:
                ans += 1
        print(ans)