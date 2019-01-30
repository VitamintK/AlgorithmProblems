#UNFINISHED

while True:
    n = int(input())
    if n == 0:
        break
    cents = []
    for i in range(n):
        usd = input()
        cent = int(usd[:-3])*100 + int(usd[-2:])
        cents.append(cent)
    cents.sort()
    we_want = sum(cents)/len(cents)

    r = len(cents)-1
    l = 0

    ans = 0
    while r > l:
        if cents[r]-we_want > we_want - cents[l]:
            exchange = (ceil(we_want)-cents[l])
            ans+=exchange
            cents[r] -= exchange
            cents[l] = ceil(we_want)
            r-=1
        else:
            exchange = (floor)