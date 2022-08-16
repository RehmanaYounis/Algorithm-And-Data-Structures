# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res=[]
        q = deque([root])
        
        while q:
            rightSide=None
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return(res)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
#         height=[-1]
#         res=[]
#         def dfs(root, cur):
#             if not root:
#                 return 
#             if cur>height[0]:
#                 res.append(root.val)
#                 height[0]=cur
#             dfs(root.right,cur+1)
#             dfs(root.left,cur+1)
           
#         dfs(root, 0)
#         return res
            