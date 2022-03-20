# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def maxDepth(self, root):
            if not root: return 0
            que = deque()
            que.append(root)
            depth=0
            while que:
                for i in range(len(que)):
                    node=que.popleft()
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                depth +=1
            return depth
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             level=0
#             if not root:
#                 return 0
#             q=deque([root])
#             while q:   
#                 for i in range(len(q)):
#                     cur=q.popleft()
#                     print(cur.val)
#                     if cur.left:
#                         q.append(cur.left)
#                     if cur.right:
#                         q.append(cur.right)
#                 level += 1
#             return level
            
            
                       
                        
            
# #             if not root:
# #                 return 0
# #             # return max(1 + self.maxDepth(root.left), 1+self.maxDepth(root.right))

 






















    
    
    
    
    
#     def maxDepth(self, root):
#         if not root:
#             return 0
        
#         level = 0
#         q = deque([root])
        
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level+=1
#         return level
        
        
        
        
        
        
        
# #         Sol 1:
# #         if not root:
# #             return 0
        
# #         return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right) )
        