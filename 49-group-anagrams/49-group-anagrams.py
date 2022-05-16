class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for s in strs:
            temp = "".join(sorted(s))
            temp=tuple(sorted(s))
            # print(temp)
            if temp not in hashmap.keys():
                hashmap[temp]=[s]
            else:
                hashmap[temp]=hashmap[temp]+[s]
                
        return hashmap.values()
        
        
        
        
        
        
        
        
    
        
        
#         gmap = {}
#         temp=''
#         for str1 in strs:
#             temp= "".join(sorted(str1))            
#             if temp in gmap.keys():
#                 gmap[temp]=gmap[temp] + [str1]
#             else:
#                 gmap[temp]= [str1]
#         return (gmap.values())
    