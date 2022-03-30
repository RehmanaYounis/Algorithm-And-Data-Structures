# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        pathSum=0
        
        def dfs(root, targetSum, pathSum):
            if not root: return 
            pathSum+=root.val
            if pathSum==targetSum:
                self.count+=1
            
            dfs(root.left, targetSum, pathSum) 
            dfs(root.right, targetSum, pathSum)
        
        
        
        dfs(root, targetSum, pathSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        
        return self.count
        