T = int(input())
for t in range(T):
    s = input()
    ans = []
    l = 0
    for i in s:
        n = int(i)
        while n > l:
            ans.append('(')
            l+=1
        while n < l:
            ans.append(')')
            l-=1
        ans.append(i)
    # deal with closing here
    for i in range(l):
        ans.append(')')
    print("Case #{}: {}".format(t+1, ''.join(ans)))