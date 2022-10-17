class Solution(object):
    def generate(self, numRows):
        res=[[1]]
        for i in range(1, numRows):
            temp=[0]+res[-1]+[0]
            curRow=[]
            for j in range(len(res[-1])+1):
                curRow.append(temp[j]+temp[j+1])
            res.append(curRow)
        return res