alpha = 'abcdefghijklmnopqrstuvwxyz'
def cmp(a, b):
    if a is None:
        return b
    if b is None:
        return a
    c1, p1 = a
    c2, p2 = b
    if chainlen_length(c1)+p1 < chainlen_length(c2)+p2:
        return a
    if chainlen_length(c1)+p1 > chainlen_length(c2)+p2:
        return b
    if c1 > c2:
        return a
    else:
        return b

def chainlen_length(chainlen):
    if chainlen == 0:
        return 0
    if chainlen == 1:
        return 1
    else:
        return 1+len(str(chainlen))

def debug(*args):
    if False:
        print(*args)
    
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = [{l: None for l in alpha+'.'} for i in range(k+1)]
        dp[0]['.'] = (0,0)
        for index, letter in enumerate(s):
            debug('-----')
            debug(s[:index])
            new_dp = [{l: None for l in alpha+'.'} for i in range(k+1)]
            for i in range(k+1):
                for prev_letter in dp[i]:
                    if dp[i][prev_letter] is None:
                        continue
                    #use the letter
                    chainlen, prelen = dp[i][prev_letter]
                    debug(i, prev_letter, chainlen, prelen, chainlen_length(chainlen)+prelen)
                    if letter == prev_letter:
                        new_dp[i][letter] = cmp(new_dp[i][letter], (chainlen+1, prelen))
                    else:
                        new_dp[i][letter] = cmp(new_dp[i][letter], (1, prelen+chainlen_length(chainlen)))
                    #don't use the letter
                    if i < k:
                        new_dp[i+1][prev_letter] = cmp(new_dp[i+1][prev_letter], dp[i][prev_letter])
            dp = new_dp
        ans = 12345566
        for i in range(k+1):
            for l in dp[i]:
                if dp[i][l] is None:
                    continue
                c, p = dp[i][l]
                debug(i, l, c, p, chainlen_length(c)+p)
                ans = min(ans, chainlen_length(c)+p)
        return ans