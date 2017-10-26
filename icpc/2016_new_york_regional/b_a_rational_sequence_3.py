T = int(input())
for t in range(T):
    n = int(input().split()[1])
    x = 0
    p = 1
    q = 1
    stack = []
    nn = n
    while(nn != 1):
        stack.append(nn%2)
        nn//=2
    for i in reversed(stack):
        if i ==  0:
            q = p+q
        else:
            p = p+q
    print(t+1, str(p)+'/'+str(q))


 
