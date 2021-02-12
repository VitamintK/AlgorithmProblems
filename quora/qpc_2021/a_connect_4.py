def add_to_board(board, n, player):
    for i in range(H):
        if board[n][i] == -1:
            board[n][i] = player
            return (n, i)

def get_winner(board, w, h, p):
    for w in range(W):
        for h in range(H):
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if dx == 0 and dy == 0:
                        continue
                    win = True
                    nx, ny = w, h
                    for i in range(4):
                        if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                            win = False
                            break
                        if board[nx][ny] != p:
                            win = False
                            break
                        nx += dx
                        ny += dy
                    if win:
                        return True

W, H = 7, 6
board = [[-1 for i in range(H)] for i in range(W)]
for i in range(42):
    player = i%2
    n = int(input())-1
    x, y = add_to_board(board, n, player)
    is_win = get_winner(board, x, y, player)
    if is_win:
        print('RED' if player==0 else 'YELLOW', i+1)
        break
else:
    print('DRAW')