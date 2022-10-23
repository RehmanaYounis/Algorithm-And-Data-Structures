class Solution(object):
    def platesBetweenCandles(self, s, queries):
        starSum=[0]*len(s)
        candleToLeft=[-1]*len(s)
        candleToRight=[len(s)]*len(s)
        
        starSum[0]=1 if s[0]=='*' else 0
        candleToLeft[0]=0 if s[0]=='|' else -1
        for i in range(1, len(s)):
            if s[i]=='*':
                starSum[i]=1+starSum[i-1]
            else:
                prev=i-1
                starSum[i]=starSum[i-1]
            if s[i]=='|':
                candleToLeft[i]=i
            else: candleToLeft[i]=candleToLeft[i-1]
        if s[len(s)-1]=='|': candleToRight[len(s)-1]=len(s)-1
        for i in range(len(s)-2, -1, -1):
            if s[i]=='|':
                candleToRight[i]=i
            else:
                candleToRight[i]=candleToRight[i+1]
        ans=[0]*len(queries)
        
        for i in range(len(queries)):
            start=queries[i][0]
            end=queries[i][1]
            if candleToLeft[end]<start or candleToRight[start]>end:
                continue
            ans[i]=starSum[candleToLeft[end]]-starSum[candleToRight[start]]
        return ans
        

        
        
#         if prefcandle[r]<l or suffcandle[l]>r:
# #                     continue

# #                 #desired answer is no of pplates(*) only inside 2 candles (|) inside the given boundary area
# #                 ans[i]=pref[prefcandle[r]]-pref[suffcandle[l]]
        ##################################
        n=len(s)
        prefcandle=[-1]*n #this stores the position of closest candle from current towards left
        suffcandle=[0]*n #this stores the position of closest candle from current towards right

        pref=[0]*n #stores the number of plates  till ith position from 0 - for i = 0 -> n 

        ind=-1
        c=0

        for i in range(n):
            if ind!=-1 and s[i]=='*':
                c+=1
            elif s[i]=='|':
                ind=i
            pref[i]=c


        ind =-1
        for i in range(n):
            if s[i] == '|':
                ind=i
            prefcandle[i]=ind

        

        #this method calculates the right nearest candle to a point
        #intial is infinity as to right of rightmost element no candle can be present
        ind = float('inf')       
        for i in range(n-1, -1, -1):
            if s[i]=='|':
                ind=i
            suffcandle[i]=ind
        print(prefcandle, suffcandle)
#             #m = no of queries
#             m=len(qs)
#             ans=[0]*m

#             for i in range(m):
#                 c=0
#                 l=qs[i][0]
#                 r=qs[i][1]

#                 #check if left nearest candle of right boundary is after left boundary
#                 #check if right nearest candle of left boundary is before right boundary
#                 # to summarise - here we find if there is a pair of candle present within the given range or not
#                 if prefcandle[r]<l or suffcandle[l]>r:
#                     continue

#                 #desired answer is no of pplates(*) only inside 2 candles (|) inside the given boundary area
#                 ans[i]=pref[prefcandle[r]]-pref[suffcandle[l]]
#             return ans