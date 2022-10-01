# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        stack=[]
        while q:
            curLen=len(q)
           
            for i in range(curLen):
                Node=q.popleft()
                if Node and Node.left:
                    q.append(Node.left)
                if Node and Node.right:
                    q.append(Node.right)
            if Node:
                stack.append(Node.val)
        return stack
                    