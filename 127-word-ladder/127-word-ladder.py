class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wmap=collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+ "*" +word[j+1:]
                wmap[pattern].append(word)
        count=1
        visited=set([beginWord])
        q=deque([beginWord])
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word == endWord:
                    return count
                visited.add(word)
                for j in range(len(word)):
                    pattern=word[:j] + "*" +word[j+1:]
                    for nei in wmap[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            count+=1
        return 0
            
                