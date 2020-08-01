# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, distance):
        if node is None:
            return [0,0,0,0,0,0,0,0,0,0,0]
        if node.left is None and node.right is None:
            return [1,0,0,0,0,0,0,0,0,0,0]
        a = self.dfs(node.left, distance)
        b = self.dfs(node.right, distance)
        r = [0 for i in range(11)]
        for i in range(10):
            r[i+1] += a[i] + b[i]
        for i in range(1, len(b)):
            b[i] = b[i] + b[i-1]
        for d1, v in enumerate(a):
            d1 = d1+1
            d2 = distance - d1
            if d2 < 1:
                continue
            # print(d1, v, b[d2-1])
            self.ans += v * b[d2-1]
            # print(self.ans)
       
        # print('node', node.val, r)
        return r
        
                
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        self.dfs(root, distance)
        return self.ans