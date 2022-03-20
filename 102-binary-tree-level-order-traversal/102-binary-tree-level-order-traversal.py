# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: return
        q = deque()
        q.append(root)
        elements=[]
        while q:
            temp=[]
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            elements.append(temp)
        return elements
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if root is None: return []
        
#         queu=deque()
#         queu.append(root)
#         elements=[]
#         while queu:
#             temp=[]
#             for i in range(len(queu)):
#                 node=queu.popleft()
#                 if node.left:
#                     queu.append(node.left)
#                 if node.right:
#                     queu.append (node.right)
#                 temp.append(node.val)
#             elements.append(temp)
#         return elements

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return []
        
#         output=[]
#         elements=[]
#         q=deque([root])
#         while q:
#             for i in range(len(q)):
#                 node=q.popleft()
#                 elements.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             output.append(elements)
#             elements=[]
#         return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  