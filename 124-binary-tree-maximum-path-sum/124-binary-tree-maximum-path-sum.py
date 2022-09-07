# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val
        def pathFind(root):
            nonlocal res
            if not root:
                return 0
            leftSum=pathFind(root.left)
            rightSum=pathFind(root.right)
            leftSum=max(leftSum, 0)
            rightSum=max(rightSum, 0)
            res= max(res, root.val+leftSum+rightSum)
            return root.val+max(leftSum, rightSum)
        pathFind(root)
        return res
    
#         res = [root.val]

#             # return max path sum without split
#         def dfs(root):
#             if not root:
#                 return 0

#             leftMax = dfs(root.left)
#             rightMax = dfs(root.right)
#             leftMax = max(leftMax, 0)
#             rightMax = max(rightMax, 0)

#             # compute max path sum WITH split
#             res[0] = max(res[0], root.val + leftMax + rightMax)
#             return root.val + max(leftMax, rightMax)

#         dfs(root)
#         return res[0]