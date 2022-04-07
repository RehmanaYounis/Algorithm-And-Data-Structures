# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        nodeMap=defaultdict(list)
        def parse(root, parent, direction):
            if not root: return
            if parent:
                nodeMap[root.val].append([parent.val, 'U'])
                nodeMap[parent.val].append([root.val, direction])
            parse(root.left, root, 'L')
            parse(root.right, root, 'R')
        parse(root, None, None)
        
        q = deque()
        visited=set()
        
        q.append([startValue, ''])
        visited.add(startValue)
        while q:
            val, result = q.popleft()
            if val==destValue:
                return result
            for node in nodeMap[val]:
                nodeVal, direction = node[0], node[1]
                if nodeVal not in visited:
                    visited.add(nodeVal)
                    q.append([nodeVal, result+direction])
        return ''