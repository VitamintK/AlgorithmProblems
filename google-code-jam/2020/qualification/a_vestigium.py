T = int(input())
for t in range(T):
    N = int(input())
    square = []
    for i in range(N):
        square.append([int(x) for x in input().split()])
    cols = 0
    rows = 0
    trace = 0
    for i in range(N):
        trace += square[i][i]
    for i in range(N):
        if len(set(square[i])) != N:
            rows += 1
        if len(set(square[j][i] for j in range(N))) != N:
            cols +=1
    print("Case #{}: {} {} {}".format(t+1, trace, rows, cols))