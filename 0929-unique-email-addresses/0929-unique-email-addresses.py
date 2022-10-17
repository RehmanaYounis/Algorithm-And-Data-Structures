class Solution(object):
    def numUniqueEmails(self, emails):
        
        def createEmail(email):
            res=''
            plusFlag=0
            for i in range(len(email)):
                if email[i]=='@':
                    res+=email[i:]
                    return res
                elif email[i]=='.':
                    continue
                elif email[i]=='+':
                    plusFlag=1
                if plusFlag==0:
                    res+=email[i]
        hashMap={}
        for email in emails:
            hashMap[createEmail(email)]=True
        return len(hashMap)
        
    
    