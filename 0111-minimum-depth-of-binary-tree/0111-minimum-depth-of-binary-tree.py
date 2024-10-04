# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q=deque([root])
        depth=1
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if not node.left and not node.right:
                    return depth
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            depth+=1
        return depth