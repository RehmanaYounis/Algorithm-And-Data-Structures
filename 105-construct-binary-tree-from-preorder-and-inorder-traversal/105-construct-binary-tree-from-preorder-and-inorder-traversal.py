# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        res=[]
        def buildT(preOdr, inOdr):
            if len(preOdr) ==0 or len(inOdr)==0:
                return    
            start=preOdr[0]
            root=TreeNode(start)
            ind=inOdr.index(start)
            root.left=buildT(preOdr[1:ind+1], inOdr[:ind])
            root.right= buildT(preOdr[ind+1:], inOdr[ind+1:])
            return root
        return buildT(preorder, inorder)
   
    
    
#     root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
#         return root