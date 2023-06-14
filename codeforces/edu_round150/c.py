import sys
input = sys.stdin.readline

IMP = -1123456789123456789
d = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}
vals = [1,10,100,1000,10000]

def maxNone(a,b):
    if a is None:
        return b
    return b

T = int(input())
for t in range(T):
    s = [d[x] for x in input().strip()]
    # pre = [[0,0,0,0,0]]
    # for i in range(len(s)):
    #     last = pre[-1][:]
    #     last[s[i]] += 1
    #     pre.append(last)
    # dp[used][j] = value so far if j is biggest number seen, and used==we've used our one move
    dp = [[0,IMP,IMP,IMP,IMP], [IMP,IMP,IMP,IMP,IMP]]
    # dp[0][j] = dp[0][j]
    for i in reversed(range(len(s))):
        x = s[i]
        val = vals[x]
        dp2 = [[IMP,IMP,IMP,IMP,IMP], [IMP,IMP,IMP,IMP,IMP]]
        for biggest_seen_yet in range(5):
            if x < biggest_seen_yet:
                dp2[0][biggest_seen_yet] = max(dp2[0][biggest_seen_yet], dp[0][biggest_seen_yet] - val)
                dp2[1][biggest_seen_yet] = max(dp2[1][biggest_seen_yet], dp[1][biggest_seen_yet] - val)
            else:
                # if x == 2 and biggest_seen_yet == 0:
                #     print(dp, val, dp[0][biggest_seen_yet] + val)
                dp2[0][x] = max(dp2[0][x], dp[0][biggest_seen_yet] + val)
                dp2[1][x] = max(dp2[1][x], dp[1][biggest_seen_yet] + val)
        for biggest_seen_yet in range(5):
            for switch in range(5):
                switchval = vals[switch]
                if switch==x:
                    continue
                if switch < biggest_seen_yet:
                    continue
                    # dp2[1][biggest_seen_yet] = max(dp2[1][biggest_seen_yet], dp[0][biggest_seen_yet] - val)
                else:
                    # if switch==4 and biggest_seen_yet==0:
                    #     print(switch, biggest_seen_yet, dp, switchval)
                    dp2[1][switch] = max(dp2[1][switch], dp[0][biggest_seen_yet] + switchval)
        dp = dp2
        # print(dp)
    ans = -100000000000
    for used in dp2:
        for i in range(5):
            ans = max(ans, used[i])
    print(ans)

