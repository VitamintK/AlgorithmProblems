# just kmp

class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0 for i in s]
        l = 0
        i = 1
        while i < len(s):
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i+= 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = l
                    i += 1
        return s[:lps[-1]]
                
                
                
        