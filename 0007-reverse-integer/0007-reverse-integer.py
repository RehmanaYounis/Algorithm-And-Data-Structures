class Solution:
    def reverse(self, x: int) -> int:
        
        MIN= -2147483648
        MAX= 2147483647
        res=0
        
        while x:
            last_digit= int(math.fmod(x, 10))
            rem_num= int(x /10)
            if res > MAX//10 or (res == MAX//10 and last_digit> MAX%10):
                return 0
            if res < MIN//10 or (res == MIN//10 and last_digit < MIN%10):
                return 0
            
            res= res*10 + last_digit
            x=rem_num
        return res
        

#             digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
#             x = int(x / 10)  # (python dumb) -1 // 10 = -1

#             if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
#                 return 0
#             if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
#                 return 0
#             res = (res * 10) + digit

#         return res