# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth=[0]
        # def findDepth(root,cur):
        #     if not root:
        #         depth[0]=max(cur, depth[0])
        #         return
        #     findDepth(root.left, cur+1)
        #     findDepth(root.right, cur+1)
        # findDepth(root, 0)
        # return depth[0]
        if not root:
            return 0
        stack=[[root, 0]]
        depth=0
        while stack:
            node, cur = stack.pop()
            depth=max(depth,cur )
            if node:
                stack.append([node.left, cur+1])
                stack.append([node.right, cur+1])
        return depth                
            