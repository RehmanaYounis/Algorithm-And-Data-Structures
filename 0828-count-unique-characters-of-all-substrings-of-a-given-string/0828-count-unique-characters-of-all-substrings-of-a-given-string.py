class Solution(object):
    def uniqueLetterString(self, s):
        hashMap=defaultdict(list)
        for ind,c in enumerate(s):
            hashMap[c].append(ind)
        
        print(hashMap)
        count=0
        for key in hashMap:
            cur=hashMap[key]
            cur=[-1]+cur+[len(s)]
            print(cur)
            for j in range(1, len(cur)-1):         
                count+= (cur[j]-cur[j-1]) * (cur[j+1]-cur[j])                             
        return count   
      
        
        
        
        
        
        
        
#         # find all the characotrs' indexes first
#         char_idx = defaultdict(list)
#         for i, char in enumerate(s):
#             char_idx[char].append(i)
        
#         res = 0
#         for char in char_idx:
#             all_idxs = [-1] + char_idx[char] + [len(s)] # adding boundaries for each charactors
#             for i in range(1, len(all_idxs)-1):
#                 res += (all_idxs[i] - all_idxs[i-1]) *  (all_idxs[i+1] - all_idxs[i])
        
#         return res

        