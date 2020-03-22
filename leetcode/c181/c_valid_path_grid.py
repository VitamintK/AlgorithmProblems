l = (0,-1)
r = (0,1)
u = (-1, 0)
d = (1, 0)
paths = {1: (l, r), 2: (u, d), 3: (l, d), 4: (d, r), 5: (l, u), 6: (u, r)}
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        stack = [(0,0)]
        explored = set()
        while len(stack) > 0:
            r,c = stack.pop()
            if (r,c) in explored:
                continue
            explored.add((r,c))
            if r == len(grid) - 1 and c == len(grid[0]) -1:
                return True
            for dr, dc in paths[grid[r][c]]:
                new_r, new_c = r+dr, c+dc
                if new_r >= len(grid) or new_r < 0 or new_c >= len(grid[0]) or new_c < 0:
                    continue
                if any((d_r * -1, d_c * -1) == (dr,dc) for d_r, d_c in paths[grid[new_r][new_c]]):
                    stack.append((new_r, new_c))
                # if (new_r, new_c) in explored:
                #     continue
        return False
                
            
        