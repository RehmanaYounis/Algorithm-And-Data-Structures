# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        res=[]
        if not root:
            return []
        maxVal=root.val
        def dfs(root, maxVal):
            if not root:
                return
            if root.val>=maxVal:
                res.append(root.val)
            maxVal=max(root.val, maxVal)
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        dfs(root, maxVal)
        return len(res)