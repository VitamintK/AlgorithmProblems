T = int(input())
for t in range(T):
    n,k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    sumx = sum(xs)
    sumsqx = sum(x*x for x in xs)
    diff = sumsqx - sumx*sumx
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