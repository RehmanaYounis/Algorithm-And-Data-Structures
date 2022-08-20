"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        cloneToCopy={}
        def clone(node):
            if node in cloneToCopy:
                return cloneToCopy[node]
            copy=Node(node.val)
            cloneToCopy[node]=copy
            for neg in node.neighbors:
                copy.neighbors.append(clone(neg))
            return copy
        return clone(node)
    
    
#     oldToNew = {}

#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]

#             copy = Node(node.val)
#             oldToNew[node] = copy
#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei))
#             return copy

#         return dfs(node) if node else None