T = int(input())
from collections import Counter
for t in range(T):
    n, p = map(int, input().split())
    g = [int(x)%p for x in input().split()]
    G = Counter(g)
    ans = 1
    ans += G[0]
    G[0] = 0
    if p == 2:
        ans += G[1]//2
        G[1] -= 2*(G[1]//2)
    elif p == 3:
        ot = min(G[1], G[2])
        ans += ot
        G[1] -= ot
        G[2] -= ot
        ans += max(G[1], G[2])//3
        G[1]%=3
        G[2]%=3
    else:
        #p == 4
        ot = min(G[1], G[3])
        ans += ot
        ans += G[2]//2
        G[1] -= ot
        G[3] -= ot
        G[2] -= 2*(G[2]//2)
        if G[2] > 0 and G[1] >= 2:
            ans += 1
            G[2] -=1
            G[1] -=2
        if G[2] > 0 and G[3] >= 2:
            ans +=1
            G[2] -=1
            G[3] -=2
        ans += max(G[1], G[3])//4
        G[1]%=4
        G[3]%=4
    if sum(G.values()) == 0:
        ans -= 1
    print("Case #{}: {}".format(t+1, ans))
