class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        tens=1
        num=digits[-1]
        i=len(digits)-2
        while i>=0:
            tens=10* tens
            print(tens)
            num=tens*digits[i] +num
            i-=1
        num+=1
        res=[]
        while num:
            digit=num%10
            res.append(digit)
            num=num//10
        return res[::-1]