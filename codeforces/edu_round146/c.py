# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n,s1,s2 = map(int, input().split())
    rs = [int(x) for x in input().split()]
    ans = [[], []]
    c1, c2 = 0,0
    rs = [(rs[i], i) for i in range(len(rs))]
    rs.sort(reverse=True)
    for r, i in rs:
        t1, t2 = len(ans[0])*s1+s1, len(ans[1])*s2+s2
        if t1 < t2:
            ans[0].append(i+1)
        else:
            ans[1].append(i+1)
    print(len(ans[0]), ' '.join(map(str, ans[0])))
    print(len(ans[1]), ' '.join(map(str, ans[1])))