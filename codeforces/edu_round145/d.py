import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    s = input().strip()
    l = len(s)
    # print(s, l)
    total_ones = s.count('1')
    total_zeroes = l - total_ones
    zeroes_seen = 0
    best_cost = None
    for i in range(l+1):
        ones_seen = i - zeroes_seen
        zeroes_remaining = total_zeroes - zeroes_seen
        cost = ones_seen + zeroes_remaining
        cost = cost * 1000000000000 + cost
        if i > 0 and i < l:
            if s[i-1] == '1' and s[i] == '0':
                # print("boop")
                cost -= 1000000000002
        if best_cost is None or cost < best_cost:
            best_cost = cost
        if i==l:
            break
        if s[i] == '0':
            zeroes_seen += 1
    print(best_cost)