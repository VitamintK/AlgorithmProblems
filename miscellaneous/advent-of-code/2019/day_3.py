a = input().split(',')
b = input().split(',')
mp = dict()
ans = 1000000000
def go(x, care):
    global ans
    t = 0
    m = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1,0)}
    r, c = 0, 0
    for instr in x:
        # print(instr)
        print(r,c)
        d = instr[0]
        dr, dc = m[d]
        dr *= int(instr[1:])
        dc *= int(instr[1:])
        for i in range(abs(dr)):
            t += 1
            r += dr/abs(dr)
            if care:
                if (r, c) in mp:
                    #print(r, c)
                    ans = min(ans, t + mp[(r,c)])
            else:
                if (r,c) not in mp:
                    mp[(r,c)] = t
        for i in range(abs(dc)):
            t += 1
            c += dc/abs(dc)
            if care:
                if (r, c) in mp:
                    #print(r, c)
                    ans = min(ans, t + mp[(r,c)])
            else:
                if (r,c) not in mp:
                    mp[(r,c)] = t



go(a, False)
go(b, True)
print(ans)