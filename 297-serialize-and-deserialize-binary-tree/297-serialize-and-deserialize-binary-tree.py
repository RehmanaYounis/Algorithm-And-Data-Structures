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
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        
        

    def deserialize(self, data):
        i=0
        data=data.split(',')
        def dfs():
            nonlocal i
            if data[i]=="N":
                i+=1
                return 
            node=TreeNode(int(data[i]))
            i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))