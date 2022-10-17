class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        flag=False
        # print('see',s[5])
        right=len(s)-1
        
        while right>=0:
            if s[right] == " " and flag==False:
                right-=1
                continue
            flag=True
            if s[right] == " " and flag ==True:
                return count
            count+=1
            right-=1
        return count


                
            
        