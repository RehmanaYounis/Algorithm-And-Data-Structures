# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return
        print(targetSum, root.val)
        if targetSum == root.val and (root.left is None and root.right is None):
            return True
        targetSum=targetSum - root.val
        
        
        return(self.hasPathSum(root.left, targetSum ) or self.hasPathSum(root.right, targetSum ))
        