MOD = 1000000007
T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    ans = 0
    prev = None
    prev_index = None
    for i, x in enumerate(s):
        if x == 'F':
            continue
        if prev is not None and x != prev:
            ans += (prev_index+1) * (n-i)
            ans %= MOD
        prev = x
        prev_index = i
    print(f'Case #{t+1}: {ans}')