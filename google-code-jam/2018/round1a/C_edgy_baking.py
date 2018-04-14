#case 1: max < p -> output max
#case 2: single min + already > p -> output already
#case 3:
#bleh i'm just gonna guess
#post-contest edit: turns out the main solution they envisioned was knapsack
#although they also proved that my solution works
#https://codejam.withgoogle.com/2018/challenges/0000000000007883/analysis/000000000002fff7
def combine_ranges(ranges):
    stack = []
    for r in ranges:
        if len(stack) == 0:
            stack.append(r)
        else:
            if stack[-1][1] >= r[0]:
                stack[-1][1] = max(stack[-1][1], r[1])
            else:
                stack.append(r)
    return stack

import math

T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    biggest_ans = 0
    ranges = [[0,0]]
    baseline = 0
    for i in range(N):
        W, H = map(int, input().split())
        baseline += W+W+H+H
        small = min(W, H)*2
        big = math.sqrt(W*W + H*H)*2
        for j in range(len(ranges)):
            ss, bb = ranges[j]
            ranges.append([ss+small, bb+big])
        ranges.sort()
        ranges = combine_ranges(ranges)
    ans = 0
    margin = P-baseline
    for j in ranges:
        if j[0] > margin:
            print("Case #{}: {}".format(t+1, baseline+ans))
            break
        elif j[1] >= margin:
            print("Case #{}: {}".format(t+1, P))
            break
        else:
            ans = j[1]
    else:
        print("Case #{}: {}".format(t+1, baseline+ans))
