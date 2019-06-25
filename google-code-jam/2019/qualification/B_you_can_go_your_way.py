T = int(input())
other = {'S':'E', 'E':'S'}
for t in range(T):
    n = int(input())
    p = input()
    if p[0] != p[-1]:
        if p[0] == 'E':
            ans = 'S'*(n-1) + 'E'*(n-1)
        else:
            ans = 'E'*(n-1) + 'S'*(n-1)
    else:
        x, y = 0, 0
        for i in range(len(p)-1):
            if p[i] == 'E':
                x += 1
            else:
                y += 1
            if p[i] == other[p[0]] and p[i+1] == other[p[0]]:
                if p[0] == 'S':
                    ans = 'E'*x + 'S'*(n-1) + 'E'*(n-1-x)
                else:
                    ans = 'S'*y + 'E'*(n-1) + 'S'*(n-1-y)
                break
    print("Case #{}: {}".format(t+1, ans))

