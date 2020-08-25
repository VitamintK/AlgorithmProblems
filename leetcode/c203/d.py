
dp = dict()
def dfs(prefixes, i, j):
    # i and j inclusive
    if (i,j) in dp:
        return dp[(i,j)]
    ans = 0
    for s in range(i, j):
        # split right between s and s+1
        lsum = prefixes[s+1] - prefixes[i]
        # print(j+1, s+1)
        rsum = prefixes[j+1] - prefixes[s+1] 
        if rsum > lsum:
            l = dfs(prefixes, i, s)
            ans = max(ans, lsum + l)
        elif lsum > rsum:
            r = dfs(prefixes, s+1, j)
            ans = max(ans, rsum + r)
        else:
            l = dfs(prefixes, i, s)
            r = dfs(prefixes, s+1, j)
            ans = max(ans, lsum + l, rsum + r)
    dp[(i,j)] = ans
    return ans
        

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        print(len(stoneValue))
        prefixes = [0]
        # prefix[i] = sum up to but not including i
        for i in range(len(stoneValue)):
            prefixes.append(stoneValue[i] + prefixes[-1])
        # print(prefixes)
        dp.clear()
        return dfs(prefixes, 0, len(stoneValue)-1)