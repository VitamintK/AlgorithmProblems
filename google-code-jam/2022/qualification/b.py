T = int(input())
for t in range(T):
    printers = []
    for i in range(3):
        printers.append([int(x) for x in input().split()])
    inks = []
    for i in range(4):
        inks.append(min(printer[i] for printer in printers))
    if sum(inks) < 1000000:
        ans = "IMPOSSIBLE"
    else:
        used = 0
        for i in range(4):
            inks[i] = min(1000000 - used, inks[i])
            used += inks[i]
        ans = ' '.join(str(x) for x in inks)
    print(f"Case #{t+1}: {ans}")
            