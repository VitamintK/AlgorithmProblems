T = int(input())
for t in range(T):
    n,k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    sumx = sum(xs)
    sumsqx = sum(x*x for x in xs)
    diff = sumsqx - sumx*sumx
    if k > 1:
        ans = None
        for i in range(1000000000):
            num = diff-2*sumx*i
            denom = 2*sumx+2*i
            if denom!=0 and num%denom==0:
                ans=(i, num//denom)
                break
        if ans is None:
            print(f'Case #{t+1}: IMPOSSIBLE')
        else:
            print(f'Case #{t+1}:', *ans)
    else:
        if sumx==0:
            if diff==0:
                print(f'Case #{t+1}: 0')
            else:
                print(f'Case #{t+1}: IMPOSSIBLE')
        elif diff%(sumx*2)==0:
            ans = diff//(sumx*2)
            print(f'Case #{t+1}: {ans}')
        else:
            print(f'Case #{t+1}: IMPOSSIBLE')