n = int(input())
inps = []
for i in range(n):
    x,y = map(int, input().split())
    inps.append((x,y))
if n <= 1000:
    ans = 123456789876542323
    argbest = None
    for i in range(n):
        cost = 0
        x,y = inps[i]
        for j in range(n):
            xx, yy = inps[j]
            cost += max(abs(xx-x), abs(yy-y))
        if cost < ans:
            ans = cost
            argbest = i
    print(argbest+1)
else:
    inps = [inp[0] for inp in inps]
    srt = [(v,i) for i,v in enumerate(inps)]
    srt.sort()
    sorted_index_to_original_index = dict()
    for sorted_index, vi in enumerate(srt):
        v, i = vi
        sorted_index_to_original_index[sorted_index] = i
    inps = [vi[0] for vi in srt]
    total = sum(inps)
    running_total = 0
    ans = 123456789876523232323
    argbest = None
    for i in range(n):
        cost = inps[i] * i - running_total
        cost += (total - inps[i] - running_total) - inps[i] * (n-i-1)
        # print(i, cost)
        if cost < ans:
            ans = cost
            argbest = [i]
        elif cost == ans:
            argbest.append(i)
        running_total += inps[i]
    args = [sorted_index_to_original_index[x] for x in argbest]
    print(min(args)+1)