class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp={}
        def dfs(i1, i2):
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if  i1>=len(text1) or i2>=len(text2):
                return 0
            case1=dfs(i1+1, i2)
            
            case2=0
            
            index=text2.find(text1[i1],i2)
            if index !=-1:
                case2 = 1+ dfs(i1+1, index+1)
            dp[(i1,i2)]=max(case1, case2)
            return dp[(i1,i2)]
        return dfs(0,0)
        