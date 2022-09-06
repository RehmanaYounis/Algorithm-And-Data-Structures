# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        maxVal=0
        q=deque([root])
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            maxVal+=1
        return maxVal
        
        
        
        
        
        
        
        
        
        #         maxVal=0
#         def maxDep(root):
#             if not root:
#                 return 0
#             return 1+ max(maxDep(root.left),maxDep(root.right))
#         return maxDep(root)
        