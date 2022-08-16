# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return
        level=0
        q=deque([root])
        res=[]
        while q:
            cur=[]
            for i in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                print(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur) 
        return(res)
        
        
        
        
        
        
        
        
        
        
        
        
# Recursive Call       
#         if not root:
#             return
#         result={}
#         def dfs(root,level):
#             if not root:
#                 return
#             if root:
#                 if level not in result:
#                     result[level]=[]
#                 result[level].append(root.val)
#             dfs(root.left, level+1)
#             dfs(root.right, level+1)
            
#         dfs(root,0)
#         res = [x for x in result.values()]
#         return res