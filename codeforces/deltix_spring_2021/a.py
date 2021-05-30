T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    s = input()
    if all(x=='0' for x in s):
        print(s)
        continue
    for i in range(m):
        nxt = []
        updated = False
        for j in range(n):
            neighbs = 0
            if s[j] == '1':
                nxt.append('1')
                neighbs += 1
                continue
            neighbs = 0
            if j > 0 and s[j-1] == '1':
                neighbs +=1
            if j < n-1 and s[j+1] == '1':
                neighbs += 1
            if neighbs == 1:
                nxt.append('1')
                updated = True
            else:
                nxt.append('0')
        s = nxt
        if not updated:
            break
    print(''.join(s))
    # if m > n//2 + 1:
    #     print(''.join('1' * n))
    #     continue
    # closest = [12345678 for i in range(n)]
    # d = None
    # for i in range(n):
    #     if s[i] == '1':
    #         d = 0
    #     elif d is not None:
    #         d += 1
    #     if d is not None:
    #         closest[i] = d
    # d = None
    # for i in reversed(range(n)):
    #     if s[i] == '1':
    #         d = 0
    #     elif d is not None:
    #         d += 1
    #     if d is not None:
    #         closest[i] = min(closest[i], d)
    # ans = []
    # print(closest)
    # for i in range(n):
    #     if closest[i] <= m:
    #         ans.append('1')
    #     else:
    #         ans.append('0')
    # print(''.join(ans))