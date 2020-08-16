T = int(input())
for t in range(T):
    s = input()
    blocks = s.split('0')
    size = [len(block) for block in blocks]
    ans = 0
    for i, x in enumerate(sorted(size, reverse=True)):
        if i%2 == 0:
            ans += x
    print(ans)