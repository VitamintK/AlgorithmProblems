# https://codeforces.com/contest/1326/problem/A
T = int(input())
for t in range(T):
    n = int(input())
    if n == 1:
        print(-1)
        continue
    for i in range(2,10):
        ans = str(i)*(n-1)
        for k in [3,4,6,7,8,9]:
            cand = int(ans+str(k))
            if cand%k == 0 or cand%i == 0:
                continue
            ans += str(k)
            print(ans)
            break
        else:
            continue
        break