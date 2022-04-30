def diff(a,b):
    return {2: a[2]-b[2], 5: a[5]-b[5]}
def add(a,b):
    return {2:a[2]+b[2], 5:a[5]+b[5]}

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        ho = [[{2:0, 5:0} for x in r] for r in grid]
        ve = [[{2:0, 5:0} for x in r] for r in grid]
        for r in range(len(grid)):
            twos = 0
            fives = 0
            for c in range(len(grid[r])):
                n = grid[r][c]
                while n%5==0:
                    fives+=1
                    n//=5
                while n%2==0:
                    twos+=1
                    n//=2
                ho[r][c][2] = twos
                ho[r][c][5] = fives
        for c in range(len(grid[0])):
            twos = 0
            fives = 0
            for r in range(len(grid)):
                n = grid[r][c]
                while n%5==0:
                    fives+=1
                    n//=5
                while n%2==0:
                    twos+=1
                    n//=2
                ve[r][c][2] = twos
                ve[r][c][5] = fives
        # for r in ve:
        #     print(ve)
        # for r in ho:
        #     print(ho)
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                ho_tot = ho[r][-1]
                # don't count myself for ho
                if c==0:
                    ho_left = {2:0, 5:0}
                    ho_right = diff(ho_tot, ho[r][c])
                else:
                    ho_left = ho[r][c-1]
                    ho_right = diff(ho_tot, ho[r][c])
                #but count myself for vert
                ve_tot = ve[-1][c]
                if r==0:
                    ve_up = ve[r][c]
                    ve_down = ve_tot
                else:
                    ve_up = ve[r][c]
                    ve_down = diff(ve_tot, ve[r-1][c])
                for v in (ve_down, ve_up):
                    for h in (ho_left, ho_right):
                        agg = add(v,h)
                        ans = max(ans, min(agg[2], agg[5]))
        return ans