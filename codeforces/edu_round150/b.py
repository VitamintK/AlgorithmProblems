import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    q = int(input())
    xs = [int(x) for x in input().split()]
    ans = []
    gone_down = False
    last = None
    for x in xs:
        if last is None:
            ans.append(1)
            last = x
            continue
        if x < last:
            if gone_down:
                ans.append(0)
                continue
            if x > xs[0]:
                ans.append(0)
                continue
            gone_down = True
            ans.append(1)
            last = x
        else:
            if gone_down and x > xs[0]:
                ans.append(0)
                continue
            ans.append(1)
            last = x
    print(''.join(map(str, ans)))
            
