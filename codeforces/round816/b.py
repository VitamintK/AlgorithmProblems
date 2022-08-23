import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n,k,b,s = map(int, input().split())
    # waste = (n-1) * (k-1)
    # remaining = s - waste
    big_pipe = k * b
    if big_pipe > s:
        print(-1)
        continue
    topping = min(k-1, s-big_pipe)
    big_pipe += topping
    remaining = s - big_pipe
    if remaining > (k-1) * (n-1):
        print(-1)
        continue
    ans = [str(big_pipe)]
    for i in range(n-1):
        small_pipe = min(remaining, k-1)
        ans.append(str(small_pipe))
        remaining -= small_pipe
    print(' '.join(ans))