#what a question
T = int(input())
for t in range(T):
    a = int(input())

    x, y = None, None
    i = 0
    while (x,y) != (0,0):
        if a == 20:
            v, w = [(3,3),(4,3),(3,4),(4,4),(3,5),(4,5)][i%6]
        else:
            v,w = (3, 3 + (i%68))
        print(v, w)
        i+=1
        x,y = map(int, input().split())
        if (x,y) == (-1,-1):
            exit()

