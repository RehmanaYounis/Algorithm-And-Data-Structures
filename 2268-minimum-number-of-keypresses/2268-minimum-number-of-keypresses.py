class Solution(object):
    def minimumKeypresses(self, s):
        hashMap=Counter(s)
        hashMap=sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        print(hashMap)
        keyPress=0
        block=0
        for i in range(len(hashMap)):
            if block<9:
                keyPress+=hashMap[i][1]
            elif block<18:
                keyPress+=(2*hashMap[i][1])
            elif block<27:
                keyPress+=(3*hashMap[i][1])
            block+=1
        return keyPress
          
            
            
            
            
#             print(hashMap[s[i]])
#             if block<9:
#                 keyPress+=hashMap[s[i]]
#             elif block<18:
#                 keyPress+=(2*hashMap[s[i]])
#             elif block<27:
#                 keyPress+=(3*hashMap[s[i]])
#             block+=1
#         return keyPress
        