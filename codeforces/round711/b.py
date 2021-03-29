from collections import Counter
T = int(input())
for t in range(T):
    n, W = map(int, input().split())
    ws = [int(x) for x in input().split()]
    ws = Counter(ws)
    ans = 1
    lineleft = W
    while n > 0:
        cands = [w for w in ws if ws[w]>0 and w<=lineleft]
        if len(cands) == 0:
            ans += 1
            lineleft = W
        else:
            pick = max(cands)
            n -=1
            ws[pick] -= 1
            lineleft -= pick
    print(ans)