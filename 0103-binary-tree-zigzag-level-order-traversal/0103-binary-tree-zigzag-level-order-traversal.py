# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        res=[]
        depth=0
        # res.append([root.val])
        if not root:
            return []
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.popleft()
             
                if node: 
                    temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth+=1
            if depth % 2 == 0:
                temp=temp[::-1]
            res.append(temp)
        return res