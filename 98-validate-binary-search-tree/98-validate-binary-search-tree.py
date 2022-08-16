# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        def chkBST(root, minv, maxv):
            if not root:
                return True
            if not (root.val>minv and root.val<maxv):
                return False
            return (chkBST(root.left, minv,root.val ) and chkBST(root.right, root.val,maxv))
            
        
        return chkBST(root, float("-inf"), float("inf"))
        