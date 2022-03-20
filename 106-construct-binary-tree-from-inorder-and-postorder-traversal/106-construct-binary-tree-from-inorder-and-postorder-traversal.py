# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:return
        lastInd=len(postorder)-1
        # print(lastInd)
        root = TreeNode(postorder[lastInd])
        index = inorder.index(postorder[lastInd])
        # print('for left: ', inorder[0:index] ,postorder[0:index])
        # print('for right: ', inorder[index+1:],postorder[index:lastInd])
        root.left=self.buildTree(inorder[0:index], postorder[0:index])
        root.right=self.buildTree(inorder[index+1:], postorder[index:lastInd])
        return root        
        
        