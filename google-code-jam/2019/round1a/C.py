def find_longest_unused(w1, w2, already_used):
    pre = ""
    for x,y in zip(reversed(w1), reversed(w2)):
        if x == y:
            pre += x
        else:
            break
    while pre in already_used:
        pre = pre[:-1]
    if pre == "":
        return None
    return pre

#find_longest_unused('a', 'aa', {'a'})

T = int(input())
for t in range(T):
    n = int(input())
    ws = []
    for i in range(n):
        w = input()
        ws.append(w)
    import itertools
    ansans = 0
    for j in itertools.permutations(ws):
        already_used = set()
        ans = 0
        for i in range(1,len(j),2):
            x = find_longest_unused(j[i-1], j[i], already_used)
            if x is None:
                pass
            else:
                already_used.add(x)
                ans += 2
        # if ans > ansans:
        #     print(already_used)
        #     print(j)
        #     print(ans)
        ansans = max(ans, ansans)
    print("Case #{}: {}".format(t+1, ansans))