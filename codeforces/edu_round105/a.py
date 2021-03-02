# ABC String
n = int(input())

def check(s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        else:
            raise ValueError
        if cnt < 0:
            return False
    return cnt == 0

for i in range(n):
    s = input()
    ans = False
    for a in '()':
        for b in '()':
            for c in '()':
                ss = s.replace('A', a).replace('B', b).replace('C', c)
                ans = ans or check(ss)
    if ans:
        print("YES")
    else:
        print("NO")