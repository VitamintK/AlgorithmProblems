
class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:
        def find(s, start, end):
            if start == end:
                return [set()]
            # best = 0
            # argbest = None
            ans = []
            for last_char in range(start, end):
                x = find(s,last_char+1, end)
                for y in x:
                    y.add(s[start:last_char+1])
                ans.extend(x)
            return ans
        return max(len(x) for x in find(s, 0, len(s)))