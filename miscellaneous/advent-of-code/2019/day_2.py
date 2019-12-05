if False:
    # part 1
    while True:
        try:
            a = [int(x) for x in input().split(',')]
        except EOFError:
            break
    i = 0
    print(a)
    a[1] = 12
    a[2] = 2
    while a[i] != 99:
        print(i)
        x, y, z = a[i+1], a[i+2], a[i+3]
        if a[i] == 1:
            a[z] = a[x] + a[y]
        elif a[i] == 2:
            a[z] = a[x] * a[y]
        else:
            raise ValueError(a[i])
        i += 4
    print(a)
    print(a[0])
else:
    # part 2
    while True:
        try:
            og = [int(x) for x in input().split(',')]
        except EOFError:
            break

    def f(A, B):
        a = og[:]
        a[1] = A
        a[2] = B
        i = 0
        while a[i] != 99:
            #print(i)
            x, y, z = a[i+1], a[i+2], a[i+3]
            if a[i] == 1:
                a[z] = a[x] + a[y]
            elif a[i] == 2:
                a[z] = a[x] * a[y]
            else:
                raise ValueError(a[i])
            i += 4
        return a[0]
        #print(a)
        #print(a[0])
    for i in range(117):
        for j in range(117):
            if f(i,j) == 19690720:
                print(100*i + j)
                exit()