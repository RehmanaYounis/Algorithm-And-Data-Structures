# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        res=[]
        q= deque([root])
        while q:
            stack=[]
            for i in range(len(q)):
                node=q.popleft()
                if node: stack.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(stack)
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:return
#         q=deque([root])
#         res=[]
#         while q:
#             stack=[]
#             for _ in range(len(q)):
#                 node=q.popleft()
#                 stack.append(node.val)
#                 if node.left:q.append(node.left)
#                 if node.right:q.append(node.right)
#             res.append(stack)
#         return res
                    