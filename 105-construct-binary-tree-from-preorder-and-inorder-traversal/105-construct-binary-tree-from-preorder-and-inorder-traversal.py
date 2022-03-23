# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        index= inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not preorder or not inorder:
#             return
#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
#         return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        