# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

# I think this is purely a maximum nonoverlapping intervals problem
# ah wait I guess endpoints can intersect... but I guess we can just duplicate the DP table to account for that?

T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    # intervals = []
    backlink = []
    last_seen = dict()
    for i in range(n):
        if xs[i] in last_seen:
            backlink.append(last_seen[xs[i]])
        else:
            backlink.append(None)
        last_seen[xs[i]] = i
    # dp[i] gives the maximum coverage up to i, assuming i is not a right endpoint.
    dp = [0]
    # dp2[i] gives the maximum coverage up to i, assuming i *is* a right endpoint.
    dp2 = [0]
    for i in range(n):
        prev = max(dp[-1], dp2[-1])
        dp.append(prev)
        if backlink[i] is None:
            dp2.append(0)
        else:
            dp2.append(max(
                dp[backlink[i]+1] + i-backlink[i] + 1,
                dp2[backlink[i]+1] + i-backlink[i],
            ))
    # print(dp)
    print(max(dp[-1], dp2[-1]))
