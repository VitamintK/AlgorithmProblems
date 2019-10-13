class Solution:
    def balancedStringSplit(self, s: str):
        i = 0
        ans = 0
        for c in s:
        	if c == 'R':
        		i += 1
        	else:
        		i -=1
        	if i == 0:
        		ans +=1
        return ans