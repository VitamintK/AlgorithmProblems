T = int(input())
for t in range(T):
    n = int(input())
    intervals = []
    for i in range(n):
        s, e = map(int, input().split())
        intervals.append((s, e, i))
    intervals.sort()
    assignments = [None for i in range(n)]
    c_end = 0
    j_end = 0
    impossible = False
    for interval in intervals:
        s, e, i = interval
        if s >= c_end:
            c_end = e
            assignments[i] = 'C'
        elif s >= j_end:
            j_end = e
            assignments[i] = 'J'
        else:
            impossible = True
            break
    ans = "IMPOSSIBLE" if impossible else ''.join(assignments)
    print("Case #{}: {}".format(t+1, ans))
