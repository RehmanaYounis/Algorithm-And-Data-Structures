# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def maxPathSum(self, root):
            maxSum=[float('-inf')]
            def postTraversal(root):
                if not root: return 0
                left= max(postTraversal(root.left), 0)
                right= max(postTraversal(root.right), 0)
                maxSum[0]= max(maxSum[0], left+right+root.val)
                return max(left, right) +  root.val
            postTraversal(root)
            return maxSum[0]
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             maxSum=[root.val]
            
#             def dfs(root):
#                 if not root:
#                     return
#                 left = max(0, dfs(root.left))
#                 right=max(0, dfs(root.right))
                
#                 splitSum=root.val + left +right
#                 maxSum[0] = max(maxSum[0], splitSum)
#                 CombineSum = root.val + max(left, right)
#                 return CombineSum
#             dfs(root)
#             return maxSum[0]
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def maxPathSum(self, root):
#         maxSum = [root.val]
        
#         def dfs(root):
#             if not root:
#                 return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
#             left= max(0, left)
#             right = max(0, right)
            
#             splitSum = root.val + left + right
#             maxSum[0] = max(maxSum[0], splitSum)
#             CombineSum = root.val+ max(left, right)
#             return CombineSum
        
#         dfs(root)
#         return maxSum[0]
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
# #         maxSum=[root.val]
        
#         def dfs(root):
#             if not root:
#                 return 0
#             leftM = dfs(root.left)
#             rightM = dfs(root.right)
#             leftM = max(leftM, 0)
#             rightM = max(rightM,0)

#             temp= root.val + leftM + rightM
#             maxSum[0] = max(maxSum[0],temp)
        
#             return root.val + max (leftM, rightM)
        
#         dfs(root)
#         return maxSum[0]
        