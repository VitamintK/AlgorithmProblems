n, m = map(int, input().split())
s = input()

errs = []
lss = ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
for i in range(len(lss)):
    err = []
    # err[i] contains the num of errs up to and including i
    cum = 0
    ls = lss[i]
    for j in range(n):
        l = j%3
        if s[j] != ls[l]:
            cum +=1
        err.append(cum)
    errs.append(err)

# print(errs)
for i in range(m):
    l, r = map(int, input().split())
    l-=1
    r-=1
    ans = n+1
    for j in range(len(errs)):
        lefterrs = 0 if l==0 else errs[j][l-1]
        ans = min(ans, errs[j][r]-lefterrs)
    print(ans)