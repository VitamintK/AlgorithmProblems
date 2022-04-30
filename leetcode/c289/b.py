from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        ts = Counter(tasks)
        for k, v in ts.items():
            if v==1:
                return -1
            ans += (v+2)//3
        return ans