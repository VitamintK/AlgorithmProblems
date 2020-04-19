T = int(input())
for t in range(T):
    n = int(input())
    ps = []
    longest_pre = ''
    longest_suf = ''
    for i in range(n):
        p = input()
        p = p.split('*')
        ps.append(p)
        if len(p[0]) > len(longest_pre):
            longest_pre = p[0]
        if len(p[-1]) > len(longest_suf):
            longest_suf = p[-1]
    cant = False
    for p in ps:
        for l in range(len(p[0])):
            if p[0][l] != longest_pre[l]:
                cant = True
        for l in range(-1, -1*len(p[-1])-1, -1):
            if p[-1][l] != longest_suf[l]:
                cant = True
    if cant:
        ans = "*"
    else:
        ans = longest_pre
        for p in ps:
            for x in p[1:-1]:
                ans += x
        ans += longest_suf
    print("Case #{}: {}".format(t+1, ans))