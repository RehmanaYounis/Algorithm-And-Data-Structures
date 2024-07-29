# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        if not root: return True
        
        def dfs(root, minVal, maxVal):
            if not root: return True
            if not (minVal<root.val<maxVal):
                return False
            return dfs(root.left, minVal,root.val) and dfs(root.right,root.val,maxVal)
        return dfs(root, float("-inf"), float("inf"))
       
    
    
    
    
    
    
    
    
    
    
#      minVal=float('-inf')
#         maxVal=float('inf')
        
#         def dfs(root, minVal, maxVal):
#             if not root:
#                 return True
            
#             if not (root.val > minVal and root.val < maxVal):
#                 return False
#             return dfs(root.left, minVal, root.val) and dfs(root.right, root.val, maxVal)
    
#         return dfs(root, minVal, maxVal)
        
        
        