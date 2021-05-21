from collections import defaultdict
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    nums = defaultdict(list)
    for i,x in enumerate(xs):
        nums[x].append(i)
    ans = 0
    for num in nums:
        subweight = 0
        for i in nums[num]:
            ans += (n-i)*subweight
            subweight += i+1
    print(ans)