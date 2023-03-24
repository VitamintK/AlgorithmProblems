import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    arr = [-1000] * n
    pos = 0
    for i in range(n):
        if pos + i+1 <= k:
            arr[i] = 2
            pos += i+1
            continue
        desire = k - pos
        arr[i] = - 2 * (i - desire) - 1
        break
    print(' '.join(str(x) for x in arr))