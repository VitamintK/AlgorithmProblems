for i in range(1001):
    for j in range(i, 1001-i):
        k = 1000-i-j
        if k < 0:
            continue
        if i*i+j*j == k*k:
            print(i,j,k,i*j*k)
            break