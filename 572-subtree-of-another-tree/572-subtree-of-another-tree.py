# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return (dfs(r.left, s.left) and dfs(r.right, s.right))
        
        if not subRoot:
            return True
        if not root:
            return False
        
        # if not root and not subRoot:
        #     return True
        # if not root or not subRoot:
        #     return False
        
        return (dfs(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))