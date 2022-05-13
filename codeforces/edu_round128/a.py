T = int(input())
for t in range(T):
    l1,r1,l2,r2 = map(int, input().split())
    ll = max(l1,l2)
    rr = min(r1,r2)
    if rr >= ll:
        print(ll)
    else:
        print(l1 + l2)