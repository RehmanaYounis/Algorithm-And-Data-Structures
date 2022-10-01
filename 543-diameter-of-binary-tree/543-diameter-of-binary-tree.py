# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res=[0]
        def dfs(root):
            # nonlocal res
            if not root:
                return 0
            leftHeight=dfs(root.left)
            rightHeight = dfs(root.right)
            res[0]=max(res[0], leftHeight+rightHeight)
            return 1+ max(leftHeight, rightHeight)
        dfs(root)
        return res[0]