#that darned starts_at==0 edge case got me on the hidden testcases :(

T = int(input())
for t in range(T):
    l = [int(x) for x in input().split()]
    s = sum(l)
    if s == 0:
        print(0)
        continue
    if s%2 == 0:
        bottom = s//2 + 1
        top = s//2 - 1
    else:
        bottom = (s+1)//2
        top = (s)//2
    rsum = 0
    for i in l:
        rsum += i
        if rsum >= bottom:
            starts_at = rsum-i 
            extra = rsum - bottom
            break
    subtract = 0
    #print(extra, starts_at)
    if extra >= starts_at:
        if starts_at == 0:
            subtract = extra
        else:
            subtract = extra - starts_at + 1
    print(top - subtract)
