# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        def dfs(root, MinVal, MaxVal):
            if not root:
                return True
            if not (MinVal<root.val<MaxVal):
                return False
            return dfs(root.left,MinVal,root.val) and dfs(root.right,root.val, MaxVal)
            return True
        
        
        
        return dfs(root,float("-inf"), float("inf"))