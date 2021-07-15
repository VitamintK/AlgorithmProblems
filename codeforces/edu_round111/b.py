T = int(input())

def count_runs(s):
    ans = 0
    prev = '.'
    for x in s:
        if x != prev:
            ans += 1
        prev = x
    return ans

for t in range(T):
    n,a,b = map(int, input().split())
    s = input()
    if b > 0:
        ans = n * (a+b)
    else:
        runs = count_runs(s)
        actions = runs//2 + 1
        # print(actions)
        ans = actions * b + a * n
    print(ans)