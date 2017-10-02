def mex(sub_nimbers):
    for i in range(5):
        if i not in sub_nimbers:
            return i

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        board = []
        board_i = 0
        for board_i in range(n):
            board_t = str(input().strip())
            board.append(board_t)
        # Write Your Code Here
        nimber = [[-1 for i in range(n)] for j in range(n)]
        ans = 0
        nimber_count = {i:0 for i in range(5)}
        for row in range(n):
            for col in range(n):
                sub_nimbers = []
                for dr, dc in [(-1,-1), (-1,0), (0,-1)]:
                    new_r, new_c = dr+row, dc+col
                    if 0 <= new_r and 0 <= new_c and board[new_r][new_c] != 'X':
                        sub_nimbers.append(nimber[new_r][new_c])
                nimber[row][col] = mex(sub_nimbers)
                if board[row][col] == 'K':
                    for sub_nimber in sub_nimbers:
                        nimber_count[sub_nimber^nimber[row][col]]+=1
                    ans ^= nimber[row][col]
        #print(nimber)
        if nimber_count[ans] == 0:
            print("LOSE")
        else:
            print("WIN", nimber_count[ans])
        
