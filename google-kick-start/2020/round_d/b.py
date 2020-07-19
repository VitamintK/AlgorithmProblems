T = int(input())
for t in range(T):
    n = int(input())
    ps = [int(x) for x in input().split()]
    ns = []
    for i in range(len(ps)):
        if i == 0:
            continue
        if ps[i] > ps[i-1]:
            ns.append(1)
        elif ps[i] == ps[i-1]:
            continue
        else:
            ns.append(-1)
    cnt = 0
    ans = 0
    for i in range(len(ns)):
        if i != 0 and ns[i] != ns[i-1]:
            cnt = 0
        cnt += ns[i]
        if cnt > 3 or cnt < -3:
            ans +=1
            cnt = 0
    print("Case #{}: {}".format(t+1, ans))