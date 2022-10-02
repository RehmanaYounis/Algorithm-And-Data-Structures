# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        maxPath=[root.val]
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            left=max(left, 0)
            right=max(right, 0)
            maxPath[0]=max(maxPath[0], root.val+left+right)
            return root.val+max(left, right)
        dfs(root)
        return maxPath[0]