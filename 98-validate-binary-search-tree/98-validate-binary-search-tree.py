# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal=float('-inf')
        maxVal=float('inf')
        def dfs(root, minVal,maxVal):
            if not root:
                return True
            if not(root.val< maxVal  and root.val>minVal):
                return False
            return (dfs(root.left, minVal, root.val) and dfs(root.right, root.val, maxVal))
        return dfs(root, minVal, maxVal)
            
        
# def isValidBST(self, root: TreeNode) -> bool:
#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (node.val < right and node.val > left):
#                 return False

#             return valid(node.left, left, node.val) and valid(
#                 node.right, node.val, right
#             )

#         return valid(root, float("-inf"), float("inf"))








