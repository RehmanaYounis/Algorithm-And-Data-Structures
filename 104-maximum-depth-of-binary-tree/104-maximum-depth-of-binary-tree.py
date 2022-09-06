# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxVal=0
        def maxDep(root):
            if not root:
                return 0
            return 1+ max(maxDep(root.left),maxDep(root.right))
        return maxDep(root)
        