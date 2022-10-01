# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        curVal = preorder[0]
        index= inorder.index(curVal)
        root=TreeNode(curVal)
        root.left= self.buildTree(preorder[1: index+1], inorder[:index])
        root.right=self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
        
        