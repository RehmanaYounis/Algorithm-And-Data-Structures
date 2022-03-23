# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output=[]
        path=[]
        def dfs(root, targetSum,path ):
            if not root: return
            path.append(root.val)
            # print(path)

            if targetSum == root.val and root.left is None and root.right is None:
                print(path)
                output.append(path)
                return
            
            targetSum=targetSum-root.val
            dfs(root.left,targetSum, path.copy())
            dfs(root.right,targetSum, path.copy() )
        dfs(root, targetSum, [])
        return output