class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        end=max(len(num1), len(num2))
        
        l1=len(num1)-1
        l2=len(num2)-1
        
        start=0
        num1=num1[::-1]
        num2=num2[::-1]
        carry=0
        result=''
        while start<end or carry!=0:
            if start<=l1:
                val1=int(num1[start])
            else: val1=0
            if start<=l2:
                val2=int(num2[start])
            else: val2=0
            
            carry=carry+val1+val2
            if carry < 10:
                result = result+str(carry)
                carry=0
            else:
                result=result+str(carry%10)
                carry=carry//10
            start+=1
        return(result[::-1])
           