# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):
            if not root:
                return True
            if not ( left<root.val and root.val<right):
                return False
            return (dfs(root.left, left, root.val) and dfs(root.right,root.val, right ))

        return dfs(root, float('-inf'), float('inf'))


# def valid(node, left, right):
#             if not node:
#                 return True
#             if not (node.val < right and node.val > left):
#                 return False

#             return valid(node.left, left, node.val) and valid(
#                 node.right, node.val, right
#             )

#         return valid(root, float("-inf"), float("inf"))














































