# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(tree1, tree2):
            if not tree1 and not tree2:
                return 
            root=TreeNode()
            root.val=(tree1.val if tree1 else 0) + (tree2.val if tree2 else 0)
            root.left=dfs(tree1.left if tree1 else None, tree2.left if tree2 else None)
            root.right=dfs(tree1.right if tree1 else None, tree2.right if tree2 else None)
            return root
        return dfs(root1, root2)
    