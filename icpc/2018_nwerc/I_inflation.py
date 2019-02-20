n = int(input())
balloons = list(range(1,n+1))
canisters = [int(x) for x in input().split()]
canisters.sort()
ans = 1
ans = min(x/y if x<=y else -1 for x,y in zip(canisters, balloons))
if ans == -1:
    print('impossible')
else:
    print(ans)
