# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:return
        q =deque()
        q.append(root)
        result=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(node.val)
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         right=[]
#         def sumRight(root):
#             if not root: return
#             right.append(root.val)
#             if root.right:
#                 sumRight(root.right)
#             else:
#                 sumRight(root.left)
#             return right
#         sumRight(root)

#         return right