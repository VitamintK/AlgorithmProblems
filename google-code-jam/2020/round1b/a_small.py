T = int(input())

dmap = {'W': (-1,0), 'E': (1,0), 'N': (0,1), 'S':(0,-1)}
for t in range(T):
    X, Y = map(int, input().split())
    # dp or bfs, either should be fine.  bfs seems a little easier?
    # from collections import deque
    # q = deque([((0,0, ''))])
    q = [(0,0,'')]
    ans = None
    for i in range(9):
        new_q = []
        pow2 = pow(2,i)
        while len(q) > 0:
            x,y,path = q.pop()
            if x==X and y==Y:
                ans = path
                break
            for direction in dmap:
                dx, dy = dmap[direction]
                nx, ny = dx*pow2 + x, dy*pow2 + y
                if nx > 100 or nx < -100 or ny > 100 or ny <-100:
                    continue
                new_q.append((nx, ny, path+direction))
        q = new_q
        if ans is not None:
            break
    if ans is None:
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(t+1, ans))