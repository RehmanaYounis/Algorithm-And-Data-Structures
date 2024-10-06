class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        carry =1
        l=0
        while carry:
            if l<len(digits):
                if digits[l]==9:
                    digits[l]=0
                else:
                    digits[l]+=1
                    carry=0
            else:
                digits.append(carry)
                carry=0
            l+=1
        digits=digits[::-1]
        return digits