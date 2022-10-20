# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return
        val=preorder[0]
        index=inorder.index(val)
        root=TreeNode(val)
        root.left=self.buildTree(preorder[1:index+1], inorder[:index])
        root.right=self.buildTree(preorder[index+1:], inorder[index+1:])
        return root