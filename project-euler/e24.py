def get_next(perm):
    for i in reversed(range(len(perm))):
        if perm[i-1] < perm[i]:
            n = i-1
            break
    for i in reversed(range(n+1, len(perm))):
        if perm[i] > perm[n]:
            m = i
            break
    perm[m], perm[n] = perm[n], perm[m]
    perm[n+1:] = perm[:n:-1]
    return perm
perm = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,1000000):
    perm = get_next(perm)
    # print(perm)
print(*perm, sep='')