T = int(input())
for t in range(T):
    n = int(input())
    ls = [int(x) for x in input().split()]
    ans = 0
    for i in range(len(ls)-1):
        minimum = min(enumerate(ls[i:]),key=lambda x:x[1])[0]
        ans += minimum + 1
        minimum += i + 1
        # print(list(reversed(ls[i:minimum])))
        ls[i:minimum] = list(reversed(ls[i:minimum]))
        # print(ls)
    print(f'Case #{t+1}: {ans}')