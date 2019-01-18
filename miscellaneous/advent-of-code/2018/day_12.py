from collections import defaultdict
if True:
    inp = input()
    inp = inp.split()[-1]
    #inp = '....................'+inp+'....................'+
    old = defaultdict(lambda: '.')
    for j in range(len(inp)):
        old[j] = inp[j]
    new = defaultdict(lambda: '.')
    rules = dict()
    input()
    while True:
        try:
            x = input().split()
            rules[x[0]] = x[2]
        except EOFError:
            break

    last_seen_at = dict()
    for i in range(150):
        print(''.join([old[x] for x in range(-100,1000)]))
        for j in list(old.keys()):
            nstr = ''
            for k in range(j-2, j+3):
                nstr+=old[k]
            if nstr in rules:
                new[j] = rules[nstr]
            else:
                new[j] = '.'
                #raise ValueError
        old = new
        new = defaultdict(lambda: '.')

        ans = 0
        for k in old:
            if old[k]=='#':
                ans+= k
        print(ans)
    ans = 0
    for k in old:
        if old[k]=='#':
            ans+= k
    print(ans)

else:
    pass