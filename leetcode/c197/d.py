class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def f(x, y):
            return sum(math.sqrt((xp-x)*(xp-x) + (yp-y)*(yp-y)) for xp,yp in positions)
        # lo = 0
        # hi = 100
        # for i in range(112345):
        #     m1 = (lo*2/3+hi*1/3)
        #     m2 = (lo*1/3+hi*2/3)
        #     if f(1,m2) < f(1,m1):
        #         lo = m1
        #     else:
        #         hi = m2
        # print(lo)
        precision = 20
        x, y = 50, 50
        for i in range(1234):
            cands = []
            for dirx,diry in [(0,-1), (0,1), (1,0), (-1,0)]:
                dx, dy = dirx*precision, diry*precision
                xp, yp = dx+x, dy+y
                cands.append((f(xp, yp), xp, yp))
            best = min(cands)
            b, x, y = best
            precision *= 0.9
        return b