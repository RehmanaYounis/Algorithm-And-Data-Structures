# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxDepth=[0]
        def dfs(root):
            if not root:
                return 0
            return 1+max(dfs(root.left), dfs(root.right))
        # dfs(root)
        return dfs(root)