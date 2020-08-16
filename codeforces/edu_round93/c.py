from collections import defaultdict
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input()]
    seen = defaultdict(int)
    ans = 0
    cum = 0
    seen[cum]+=1
    for i, x in enumerate(xs):
        x-=1
        cum+=x
        ans += seen[cum]
        seen[cum]+=1
    print(ans)