T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    ans = []
    while a > 0 and b > 0:
        a-=1
        b-=1
        ans.append('0')
        ans.append('1')
    for i in range(b):
        ans.append('1')
    for i in range(a):
        ans.append('0')
    print(''.join(ans))