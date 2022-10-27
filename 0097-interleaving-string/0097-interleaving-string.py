class Solution(object):
    def isInterleave(self, s1, s2, s3):
        dp={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1,i2)]
            if i1==len(s1) and i2==len(s2):
                return True
            case1=False
            case2=False
            if i1<len(s1) and s1[i1]==s3[i1+i2]:
                case1=dfs(i1+1, i2)
            if i2<len(s2) and s2[i2]==s3[i1+i2]:
                case2=dfs(i1, i2+1)
            if case1 or case2: dp[(i1, i2)]=True
            else: dp[(i1, i2)]=False
            return dp[(i1, i2)]
        return dfs(0,0)
        