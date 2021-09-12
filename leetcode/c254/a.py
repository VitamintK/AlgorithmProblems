class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for w in patterns:
            if w in word:
                ans +=1
        return ans