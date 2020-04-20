T = int(input())

dmap = {'W': (-1,0), 'E': (1,0), 'N': (0,1), 'S':(0,-1)}
for t in range(T):
    X, Y = map(int, input().split())
    if (X + Y)%2 == 0:
        print("Case #{}: {}".format(t+1, 'IMPOSSIBLE'))
        continue
    # if Y%2 == 1:
    #     X, Y = Y, X


    # xbits = []
    # ybits = []
    # xt, yt = X, Y
    # for i in range(34):
    #     xbits.append(xt%2)
    #     xt//=2
    #     ybits.append(yt%2)
    #     yt//=2
    # print(xbits)
    # print(ybits)
    # if any(x and y for x,y in zip(xbits,ybits)):
    #     # invert the odd no.
    #     xbits = [-1 for n in xbits if n == 1]
    #     xbits[0] = -1
    # print(xbits)
    # print(ybits)

        
    print("Case #{}: {}".format(t+1, ans))