l, r, a = map(int, input().split())
small, big = sorted((l, r))
if big-small > a:
    print(2* (small+a))
else:
    a-=(big-small)
    print(2*(big + a//2))
