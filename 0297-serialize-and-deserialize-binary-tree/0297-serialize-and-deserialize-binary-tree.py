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
        
        return ','.join(res)

    def deserialize(self, data):
        string=data.split(',')
        self.index=0
        def createTree():
            if self.index == len(string):
                return 
            if string[self.index]=='N':
                self.index+=1
                return None
            root=TreeNode(string[self.index])
            self.index+=1
            root.left=createTree()
            root.right=createTree()
            return root
        return createTree()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))