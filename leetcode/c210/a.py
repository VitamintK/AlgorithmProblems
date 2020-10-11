class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        b = 0
        for l in s:
            if l == '(':
                b += 1
            elif l == ')':
                b -= 1
            ans = max(b, ans)
        return ans
        