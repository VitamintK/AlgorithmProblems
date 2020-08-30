class BST:
    def __init__(self, v):
        self.l = None
        self.r = None
        self.v = v
    def add(self, v):
        if v < self.v:
            if self.l is None:
                self.l = BST(v)
            else:
                self.l.add(v)
        else:
            if self.r is None:
                self.r = BST(v)
            else:
                self.r.add(v)
    

MOD = 1000000007

cache = dict()
def comb(n, r):
    if (n,r) in cache:
        return cache[(n,r)]
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    for j in range(1,r+1):
        ans //= j
    cache[(n,r)] = ans
    # print(n, r, ans)
    return ans
    
def dfs(bst):
    if bst is None:
        return 1, 0
    x, lsize = dfs(bst.l)
    y, rsize = dfs(bst.r)
    # print('dfs', bst.v)
    # print(' ', lsize, rsize)
    return (x * y * 1 * comb(lsize+rsize, min(lsize,rsize)))%MOD, lsize+rsize+1
    
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        bst = BST(nums[0])
        for i in range(1, len(nums)):
            bst.add(nums[i])
        ans = dfs(bst)
        return (ans[0] - 1)%MOD