n = int(input())
MAX = 25
matrix = [[0 for i in range(25)] for j in range(25)]
for i in range(1,25+25):
    for r in range(25):
        c = i-r
        if c < 0 or c >= 25:
            continue
        if r%2:
            matrix[r][c] = pow(2,i-1)
for r in range(n):
    print(' '.join(str(x) for x in matrix[r][:n]))
q = int(input())
for i in range(q):
    k = int(input())
    x,y = 0,0
    path = [(0,0)]
    for i in range(n+n-2):
        p = k%2
        down_is_zero = (x)%2 #down is zero
        if down_is_zero == (p == 0):
            x+=1
        else:
            y+=1
        path.append((x,y))
        k//=2
    for x,y in path:
        print(x+1, y+1)
