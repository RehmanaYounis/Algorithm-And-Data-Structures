# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        height=[-1]
        res=[]
        def dfs(root, cur):
            if not root:
                return 
            if cur>height[0]:
                res.append(root.val)
                height[0]=cur
            dfs(root.right,cur+1)
            dfs(root.left,cur+1)
           
        dfs(root, 0)
        return res
            