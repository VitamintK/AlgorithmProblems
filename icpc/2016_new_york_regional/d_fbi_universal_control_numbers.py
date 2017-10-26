T = int(input())
values = '0123456789ACDEFHJKLMNPRTVWX'
confuse = {'B': 8, 'G': 'C', 'I': 1, 'O':0, 'Q':0, 'S':5, 'U':'V', 'Z': 2}
for t in range(T):
    n = input().split()[1]
    n = [confuse[x] if x in confuse else x for x in n]
    value = 0
    for x in n[:-1]:
        value*=27
        value += values.index(x)
    vs = [values.index(x) for x in n[:-1]]
    ans = sum(a*b for a,b in zip(vs, [2,4,5,7,8,10,11,13]))%27
    if ans == values.index(n[-1]):
        print(t+1, value)
    else:
        print(t+1, "INVALID")
