class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0
        for i in range(len(bottomLeft)):
            for j in range(i):
                x = [(bottomLeft[i][0], topRight[i][0]), (bottomLeft[j][0], topRight[j][0])]
                y = [(bottomLeft[i][1], topRight[i][1]), (bottomLeft[j][1], topRight[j][1])]
                x.sort()
                y.sort()
                if x[0][1] <= x[1][0]:
                    continue
                if y[0][1] <= y[1][0]:
                    continue
                best = min(
                    min(x[0][1], x[1][1]) - max(x[0][0], x[1][0]),
                    min(y[0][1], y[1][1]) - max(y[0][0], y[1][0]),
                )
                ans = max(ans, best * best)
        return ans
                