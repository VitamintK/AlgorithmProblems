# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def issorted(l):
    x = -1
    for i in l:
        if i <= x:
            return False
        x = i
    return True

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = 0
        frontier = [root]
        while len(frontier) > 0:
            nfront = []
            for i in frontier:
                if i.left is not None:
                    nfront.append(i.left)
                if i.right is not None:
                    nfront.append(i.right)
            vals = [x.val for x in frontier]
            if level == 0:
                if not (issorted(vals) and all(x%2 == 1 for x in vals)):
                    print(vals)
                    return False
            else:
                if not (issorted(reversed(vals)) and all(x%2 == 0 for x in vals)):
                    print(vals, 'x')
                    return False
            level = (level+1)%2
            frontier = nfront
        return True