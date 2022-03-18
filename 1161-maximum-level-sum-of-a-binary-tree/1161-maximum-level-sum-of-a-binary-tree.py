# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        if not root: return 
        que =deque()
        que.append(root)
        min_level = 1
        level = 0
        sumVal=root.val
        while que:
            curSum=0
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                curSum=curSum+node.val
            level=level+1
            print(curSum, level)
            if curSum>sumVal:
                sumVal=curSum
                min_level=level
        return min_level
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root: return
#         que = deque()
#         que.append(root)
#         level=0
#         max_level=1
#         max_sum= root.val
#         while (que):
#             cur_sum=0
#             level+=1
#             for i in range(len(que)):
#                 node=que.popleft()
#                 cur_sum += node.val
#                 if node.left:
#                     que.append(node.left)
#                 if node.right:
#                     que.append(node.right)
#             print(cur_sum, max_sum)
#             if cur_sum> max_sum:
#                     max_sum=cur_sum
#                     max_level = level
#             print(level, max_level)


#         return max_level
                    
        