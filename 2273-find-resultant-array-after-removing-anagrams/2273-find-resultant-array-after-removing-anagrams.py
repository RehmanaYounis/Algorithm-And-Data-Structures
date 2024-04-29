class Solution(object):
    def removeAnagrams(self, words):
        i =0 
        while i < len(words)-1:
            print (i, words[i], i+1, words[i+1])
            if self.anagram(words[i], words[i+1]):
                words.pop(i+1)
            else:
                i+=1
            print(words)
            
        return words  
        
    def anagram(self, s,t):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        