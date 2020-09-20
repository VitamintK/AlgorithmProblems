T = int(input())

def need(n):
    return (n*(n+1))//2

for t in range(T):
    x = int(input())
    ans = 0
    nxt = 1
    while True:
        if x < need(nxt):
            break
        ans+=1
        x -= need(nxt)
        nxt = nxt*2+1
    print(ans)