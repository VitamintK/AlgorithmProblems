T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    all_paths = []
    inputs = []
    for i in range(n):
        xs = [int(x) for x in input().split()]
        for j,x in enumerate(xs):
            all_paths.append((x,i,j))
        inputs.append(xs)
    all_paths.sort()
    # my_desired_path = dict()
    # for i in range(m):
    #     my_desired_path[i] = all_paths[i]
    for i in range(n):
        paths = [-1 for j in range(m)]
        used = set()
        for j in range(m):
            if all_paths[j][1] == i:
                paths[j] = all_paths[j][2]
                used.add(paths[j])
        cnt = 0
        for j in range(m):
            while cnt in used:
                cnt += 1
            if paths[j] == -1:
                paths[j] = cnt
                cnt += 1
        print(*[inputs[i][x] for x in paths])