class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k-1
        ans = 0
        vowels = 0
        vlist = 'aeiou'
        for i in range(k):
            if s[i] in vlist:
                vowels +=1
        ans = vowels
        for i in range(k, len(s)):
            if s[i] in vlist:
                vowels +=1
            if s[i-k] in vlist:
                vowels -= 1
            ans = max(ans, vowels)
        return ans