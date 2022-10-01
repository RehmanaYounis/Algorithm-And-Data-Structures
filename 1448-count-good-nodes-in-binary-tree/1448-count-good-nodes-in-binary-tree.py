# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[]
        curMax=root.val
        def dfs(root, curMax):
            if not root:
                return
            if root.val>=curMax:
                res.append(root.val)
            curMax=max(root.val, curMax)
            dfs(root.left, curMax)
            dfs(root.right, curMax)
        dfs(root, root.val)
        return len(res)