# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=defaultdict(list)
        def dfs(root,level):
            if not root:
                return
            res[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        
        final=[res[i] for i in res.keys()]
        return final
                
        
        
        
        
        
        
        
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
                    