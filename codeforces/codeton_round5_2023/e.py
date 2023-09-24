# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

# I think this is purely a maximum nonoverlapping intervals problem
# ah wait I guess endpoints can intersect... but I guess we can just duplicate the DP table to account for that?

T = int(input())
for t in range(T):
    n, k, A = map(int, input().split())
    inputs = []
    for i in range(n):
        inputs.append(tuple(map(int, input().split())))
    inputs.sort(key=lambda x: (x[0], -x[1]))
    # dp[i] = cost up to and including point i.
    dp = []
    # last_a = (i, x, y)
    last_a = None

    all_points = [[0 for i in range(n)]]
    nn = n
    while nn > 1:
        nn = (nn+1)//2
        all_points.append([0 for i in range(nn)])
    all_points.reverse()

    for i in range(n):
        x,y,c = inputs[i]
        # don't use i
        ans = dp[-1] + c
        # # or use i, extending previous used
        # last_i, last_x, last_y = last_a
        # cost_diff = -(min(x,last_x) + min(y,last_y)) + last_x + last_y
        # ans = min(ans, dp[last_i] + A * cost_diff)
        # # or use i, making a new use
        # ans = min(ans, )

