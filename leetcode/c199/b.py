class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        c = '0'
        for i in range(len(target)):
            if target[i] != c:
                ans +=1
                c = target[i]
        return ans