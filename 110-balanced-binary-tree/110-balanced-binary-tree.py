# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def isHB(root):
            if not root:
                return True
            left=isHB(root.left)
            right=isHB(root.right)
            if not left or not right:
                return False
            if abs(left - right)>1:
                 return False
            return 1+max(left,right)
        return isHB(root )
            
        