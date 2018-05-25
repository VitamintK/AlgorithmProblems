T = int(input())

from collections import defaultdict
def check_board(board, i, N):
    ans = 0
    rows = [defaultdict(int) for x in range(N)]
    cols = [defaultdict(int) for x in range(N)]
    i<<=1
    for r in range(len(board)):
        for c in range(len(board)):
            i>>=1
            if i&1!=0:
                ans+=1
                continue
            rows[r][board[r][c]]+=1
            cols[c][board[r][c]]+=1
            if rows[r][board[r][c]] > 1:
                return -1
            if cols[c][board[r][c]] > 1:
                return -1
##    for r in range(len(bored)):
##        for c in range(len(bored)):
##            if bored[r][c] is not None:
##                for cp in range(len(bored)):
##                    if bored[r][cp] == bored[r][c] and c!=cp:
##                        return -1
##                for rp in range(len(bored)):
##                    if bored[rp][c] == bored[r][c] and r!=rp:
##                        return -1
    #if ans == 0:
    #    print(cols)
    return ans

for t in range(T):
    N = int(input())
    board = []
    for i in range(N):
        board.append([int(x) for x in input().split()])

    ans = 1000
    for i in range(pow(2,N*N)):
        check = check_board(board, i, N)
        if check > -1:
            ans = min(ans, check)
    print("Case #{}: {}".format(t+1, ans))
