def can_place(poss, i):
    return poss[i] < n*n

def get_pos(pos):
    r = pos//n
    c = pos%n
    if r%2 == 1:
        c = n-c-1
    return r, c

def place(poss, i, color):
    r, c = get_pos(poss[i])
    print(color+1, r+1, c+1)
    poss[i] += 2

n = int(input())
poss = [0,1]
for i in range(n*n):
    a = int(input()) - 1
    if a == 2:
        if can_place(poss, 0):
            place(poss, 0, 0)
        else:
            place(poss, 1, 1)
    elif a == 1:
        if can_place(poss, 0):
            place(poss, 0, 0)
        else:
            place(poss, 1, 2)
    elif a == 0:
        if can_place(poss, 1):
            place(poss, 1, 1)
        else:
            place(poss, 0, 2)