# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        maxd=[0]
        def findd(root):
            if not root:
                return -1
            left=findd(root.left)
            right=findd(root.right)
            cur=left+right+2
            maxd[0]=max(maxd[0], cur)
            return 1+max(left, right)
        findd(root)
        return maxd[0]