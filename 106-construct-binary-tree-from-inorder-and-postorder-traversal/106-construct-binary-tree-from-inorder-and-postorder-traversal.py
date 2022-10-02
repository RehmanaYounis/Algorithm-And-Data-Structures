# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return
        curVal=postorder[-1]
        index=inorder.index(curVal)
        root=TreeNode(curVal)
        root.left=self.buildTree(inorder[:index], postorder[:index])
        root.right=self.buildTree(inorder[index+1:], postorder[index:-1])
        return root
    
        