# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        self.small='zzzzzzzzzzzzzzzzzzzzzzz'
        path=''
        def dfs(root, path):
            if not root: return
            if not root.left and not root.right:
                newpath=path+chr(97+root.val)
                self.small=min(self.small, newpath[::-1])
                
            temp=path+chr(97+root.val)
            dfs(root.left, temp)
            dfs(root.right, temp)
        dfs(root,path)
        return self.small

                