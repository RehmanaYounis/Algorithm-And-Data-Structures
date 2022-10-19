# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root, prev):
            nonlocal count
            if not root:
                return
            if root.val>=prev:
                count+=1
            maxV=max(root.val, prev)
            dfs(root.left, maxV)
            dfs(root.right, maxV)
        dfs(root, root.val)
        return count