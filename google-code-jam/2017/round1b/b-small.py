T = int(input())
for t in range(T):
    n, r, o, y, g, b, v = map(int, input().split())
    if r > n//2 or b > n//2 or y > n//2:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue
    m = {'R':r, 'Y':y, 'B':b}
    s = ""
    j = None
    while m['R'] > 0 or m['Y'] > 0 or m['B'] > 0:
        z = sorted(m.items(), key=lambda x: x[1], reverse=True)
        if z[0][0] == j:
            c = z[1][0]
            m[c] -= 1
        else:
            c = z[0][0]
            m[c] -=1 
        s+= c
        j = c
    if s[-1] == s[0]:
        s = s[:-2] + s[-1] + s[-2]
    for i in range(len(s)):
        if s[i] == s[i-1]:
            print("Case #{}: IMPOSSIBLE".format(t+1))
            raise ValueError
            break
    else:
        print("Case #{}: {}".format(t+1, s))
