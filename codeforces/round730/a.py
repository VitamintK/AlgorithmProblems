T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    a, b = sorted([a,b])
    if a == b:
        print(0, 0)
        continue
    diff = b-a
    target = diff - (b%diff)
    target2 = b%diff
    if a < target2:
        target2 = 112345678901234567890
    print(diff, min(target, target2))