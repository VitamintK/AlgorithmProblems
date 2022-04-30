T = int(input())
for t in range(T):
    n,r,b = map(int, input().split())
    val = (r+b)//(b+1)
    ans = []
    remaining_rs = r
    for i in range(b):
        for k in range(val):
            ans.append('R')
            remaining_rs -= 1
            if remaining_rs == b-i-1:
                break
        ans.append('B')
    for k in range(r - val*b):
        ans.append('R')
    print(''.join(ans))