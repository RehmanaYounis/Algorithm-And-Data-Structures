# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxLen=[0]
        def dfs(root):
            if not root:
                return 0 
            left=1+ dfs(root.left)
            right=1+dfs(root.right)
            maxLen[0]=max(left, right)
            return maxLen[0] 
        dfs(root)
        return maxLen[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         maxVal=0
#         def maxDep(root):
#             if not root:
#                 return 0
#             return 1+ max(maxDep(root.left),maxDep(root.right))
#         return maxDep(root)
        