class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = [x for x,y in points]
        p.sort()
        ans = 0
        for i in range(1,len(p)):
            ans = max(ans, p[i]-p[i-1])
        return ans