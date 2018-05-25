T = int(input())
for t in range(T):
    C = int(input())
    bs = [int(x) for x in input().split()]
    impossible = False
    if bs[0] == 0:
        impossible = True
    if bs[-1] == 0:
        impossible = True
    if sum(bs) != C:
        impossible = True
    if impossible:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue
    
    my_dict = dict()
    count = 0
    for b in range(C):
        for x in range(bs[b]):
            my_dict[count] = b
            count+=1

    height = max(abs(k-v) for k,v in my_dict.items())
    #print(height)
    height+=1

    board = [['.' for i in range(C)] for j in range(height)]
    for i in my_dict:
        if i == my_dict[i]:
            continue
        if i > my_dict[i]:
            for j in range(i-my_dict[i]):
                #print(i, j)
                board[j][i-j] = '/'
        if i < my_dict[i]:
            for j in range(my_dict[i]-i):
                board[j][i+j] = '\\'
    print("Case #{}: {}".format(t+1, height))
    for l in board:
        print(''.join(l))
