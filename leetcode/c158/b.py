class Solution:
    def queensAttacktheKing(self, queens, king):
        board = [[0 for i in range(8)] for j in range(8)]
        for q in queens:
        	board[q[0]][q[1]] = 1
        kr, kc = king
        ans = []
        for i in reversed(range(kr)):
        	if board[i][kc] == 1:
        		ans.append((i, kc)) 
        		break
        for i in range(kr+1, 8):
        	if board[i][kc] == 1:
        		ans.append((i, kc))
        		break
        for j in range(kc+1, 8):
        	if board[kr][j] == 1:
        		ans.append((kr, j))
        		break
        for j in reversed(range(kc)):
        	if board[kr][j] == 1:
        		ans.append((kr, j))
        		break

        for i in range(1, min(8 - kr, 8 - kc)):
        	if board[kr+i][kc+i] == 1:
        		ans.append((kr+i, kc+i))
        		break
        for i in range(1, min(kr+1, 8-kc)):
        	if board[kr-i][kc+i] == 1:
        		ans.append((kr-i, kc+i))
        		break
        for i in range(1, min(kr+1, kc+1)):
        	if board[kr-i][kc-i] == 1:
        		ans.append((kr-i, kc-i))
        		break
        for i in range(1, min(8-kr, kc+1)):
        	if board[kr+i][kc-i] == 1:
        		ans.append((kr+i, kc-i))
        		break
        return [list(x) for x in ans]