# rip i originally read this as "any triplet p,q,r is bad if d(p,r)=d(p,q)=d(q,r)" which i think it impossible
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = n + n-1
    for i in range(n-2):
        # mx = max(xs[i], xs[i+1])
        # mn = min(xs[i], xs[i+1])
        # if mn < xs[i+2] < mx:
            # ans += 1
        if (xs[i+1]>xs[i] and xs[i+2]<xs[i+1]) or (xs[i+1]<xs[i] and xs[i+2]>xs[i+1]):
            ans += 1
            if i+3 < n and ((xs[i+1]>xs[i] and xs[i+2]<xs[i]) or (xs[i+1]<xs[i] and xs[i+2]>xs[i])):
                mx = max(xs[i], xs[i+1], xs[i+2])
                mn = min(xs[i], xs[i+1], xs[i+2])
                if mn < xs[i+3] < mx:
                    ans += 1 
    print(ans)