# no extra credit

T = int(input())
for t in range(T):
    x,y,s = input().split()
    x,y = int(x), int(y)
    cost_by_latter = {'C':y,'J':x}
    prev = None
    ans = 0
    for i in range(len(s)):
        if s[i] != '?' and s[i] != prev and prev is not None:
            ans += cost_by_latter[s[i]]
        if s[i] != '?':
            prev = s[i]
    print(f'Case #{t+1}: {ans}')