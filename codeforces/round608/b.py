n = input()
s = list(input())

if s.count("B")%2 == 1 and s.count("W")%2 == 1:
    print(-1)
else:
    ans = []
    for j in (0,1):
        for i in range(len(s)-1):
            if s[i] != 'WB'[j]:
                ans.append(i)
                s[i] = 'W' if s[i] == 'B' else 'B'
                s[i+1] = 'W' if s[i+1] == 'B' else 'B'
                # print(i, s)
        if s.count('W') == 0 or s.count('B') == 0:
            break
    print(len(ans))
    print(' '.join(str(x+1) for x in ans))