# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res=[]
        def dfs(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return (','.join(res))
                
        

    def deserialize(self, data):
        cur = data.split(',')
        self.index=0
        def buildTree():
            if cur[self.index]=='N':
                self.index+=1
                return None
            root= TreeNode(int(cur[self.index]))
            self.index+=1
            root.left=buildTree()
            root.right=buildTree()
            return root
        return buildTree()
        

        
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))