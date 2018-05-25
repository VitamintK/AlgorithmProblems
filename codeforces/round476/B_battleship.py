n, k= map(int, input().split())
board = []
for i in range(n):
    board.append(input())

argmax = (0,0)
best = -1

for i in range(n):
    for j in range(n):
        ans = 0
        if board[i][j] == '#':
            continue
        up = 0
        while i-up-1 >= 0 and board[i-up-1][j]=='.' and up+1<k:
            up+=1
        down = 0
        while i+down+1 < n and board[i+down+1][j]=='.' and down+1<k:
            down+=1
        left = 0
        while j-left-1 >= 0 and board[i][j-left-1]=='.' and left+1<k:
            #print(left, j)
            left+=1
        right=0
        while j+right+1 < n and board[i][j+right+1]=='.' and right+1<k:
            right+=1
        if up+down+1>=k:
            ans+=up+down+1-k+1
        if right+left+1>=k:
            ans+=right+left+1-k+1
        if ans > best:
            argmax = (i,j)
            best = ans
        #print(up, down, left, right)
        #print(i, j, ans)
print(argmax[0]+1, argmax[1]+1)
