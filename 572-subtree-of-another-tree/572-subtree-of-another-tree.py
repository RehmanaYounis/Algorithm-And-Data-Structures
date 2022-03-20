# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        # if subRoot and not root: return False
        if (self.isSame(root, subRoot)):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
    def isSame(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val==subRoot.val:
            return (self.isSame( root.left, subRoot.left) and self.isSame(root.right, subRoot.right))
        return False
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         if self.sameTree(root, subRoot):
#             return True
        
#         return (self.isSubtree(root.left, subRoot) or
#             self.isSubtree(root.right, subRoot))
        
        
    
#     def sameTree(self, s, t):
#         if not s and not t:
#             return True 
        
#         if s and t and s.val == t.val:
#             return (self.sameTree(s.left, t.left) and
#             self.sameTree(s.right, t.left))
#         return False