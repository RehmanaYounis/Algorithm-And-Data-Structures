# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        def dfs( root, path):
            if not root:
                return
            if not root.left and not root.right:
                output.append(path+'->'+str(root.val)if path else str(root.val))
            temp= path+'->'+str(root.val)if path else str(root.val)
            dfs(root.left,temp)
            dfs(root.right,temp)

        output=[]
        path=''
        dfs(root,path)
        return output
       