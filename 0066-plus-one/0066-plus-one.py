class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        carry=1
        l=0
        while carry:
            if digits[l]==9:
                digits[l]=0
                # print('coming here', digits)
                l+=1
                if l==len(digits):
                    digits.append(1)
                    carry=0
                    break
            else:
                digits[l]+=1
                carry=0
                l+=1
            
            # print(digits)
        return digits[::-1]