# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        res=[]
        count=[0]
        good=[root.val]
        def dfs(root, maxV):
            if not root:
                return
            maxV=max(root.val, maxV)
            if root.val>=maxV:
                res.append(root.val)
                count[0]+=1
                maxV=root.val
            dfs(root.left,maxV)
            dfs(root.right,maxV)
        dfs(root, root.val)
        return count[0]
                
        
        