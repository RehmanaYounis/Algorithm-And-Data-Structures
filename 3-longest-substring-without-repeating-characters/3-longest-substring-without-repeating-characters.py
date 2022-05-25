class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxcount = 0
        count = 0
        hashmap={}
        l,r= 0, 0
        while r < (len(s)):            
            if s[r] in hashmap:
                hashmap.pop(s[l]) 
                l = l+1
            else:
                hashmap[s[r]]=r
                maxcount = max(maxcount, len(hashmap.keys()))               
                r=r+1
        return maxcount
        
  
        
        
#         p1= 0; p2= 1
#         sub_len=0
#         temp_len=0
                
#         for p2 in range( len(s)):
#             print(s[p2])
#             for j in range(p2-1,0, -1):
#                 # print(i, j)
#                 if (s[p2] == s[j]):
#                     print('matching position :', p2, j)
#                     p1 = j
#                     temp_len=p2-j
#                     if sub_len<temp_len:
#                         sub_len=temp_len
#                     break
#                 temp_len=p2-j
#                 if sub_len<temp_len:
#                     sub_len=temp_len
#         print('string length',sub_len)
        
        
#         print(s)
#         stack=[]
#         subStr_len= 0
#         sub = 0
#         for i in s: 
#             stack.append(i)
#             print(stack)
            
#             for j in stack: 
#                 print(i,j)
#                 if i ==j:
#                     stack=[]
#                     if sub<subStr_len:
#                         sub=subStr_len
#                     subStr_len=0
#                     break
#                 else:
#                     stack.append(j)
#                     subStr_len+=1
#                 if sub<subStr_len:
#                         sub=subStr_len   
            
#         return sub
                