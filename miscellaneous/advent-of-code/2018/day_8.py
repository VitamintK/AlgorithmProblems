import sys
sys.setrecursionlimit(10000)
ans = 0
if False:
    def r(l):
        global ans
        print(l[0], l[1])
        children = l[0]
        meta = l[1]
        print(children, meta, "cm")
        allskip = 2
        for i in range(children):
            print(allskip)
            c = l[allskip]
            m = l[allskip+1]
            skip = r(l[allskip:])
            allskip+=skip
        ans = ans + sum(l[allskip:allskip+meta])
        print("returning", allskip+meta, allskip, meta)
        return allskip + meta
    while True:
        try:
            i = map(int, input().split())
        except EOFError:
            break
    r(list(i))
    print(ans)
else:
    def r(l):
        global ans
        print(l[0], l[1])
        children = l[0]
        meta = l[1]
        print(children, meta, "cm")
        allskip = 2
        vals = [None for i in range(children)]
        my_val = 0
        for i in range(children):
            print(allskip)
            c = l[allskip]
            m = l[allskip+1]
            skip, val = r(l[allskip:])
            vals[i] = val
            allskip+=skip
        #ans = ans + sum(l[allskip:allskip+meta])
        print("returning", allskip+meta, allskip, meta)
        if children == 0:
            my_val = sum(l[allskip:allskip+meta])
        else:
            my_val = sum(vals[x-1] for x in l[allskip:allskip+meta] if 0 < x <= children)
        return allskip + meta, my_val
    while True:
        try:
            i = map(int, input().split())
        except EOFError:
            break
    print(r(list(i)))
    