# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=root.val
        def findSum(root):
            nonlocal maxSum
            if not root:
                return 0
            left=findSum(root.left)
            right=findSum(root.right)
            left=max(0, left)
            right=max(0,right)
            maxSum=max(maxSum, root.val+left+right)
            return root.val+max(left, right)
        findSum(root)
        return maxSum
        