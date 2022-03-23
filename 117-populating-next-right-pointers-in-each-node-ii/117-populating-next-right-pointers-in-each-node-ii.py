"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if not root: return
        q =deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if q:node.next=q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            node.next=None
        return root
                    