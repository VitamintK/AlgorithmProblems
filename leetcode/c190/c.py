# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(1234567)

def dfs(node, counts):
    global ans
    counts = [c for c in counts]
    counts[node.val] += 1
    if node.left is None and node.right is None:
        print(counts)
        if len([cnt for cnt in counts if cnt%2 == 1]) <= 1:
            return 1
    ans = 0
    if node.left is not None:
        ans += dfs(node.left, counts)
    if node.right is not None:
        ans += dfs(node.right, counts)
    return ans
        
    
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        dfs(root, [0 for i in range(10)])
        return ans
        