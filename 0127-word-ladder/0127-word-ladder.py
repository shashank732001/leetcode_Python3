class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
                
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 0
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res+1
                
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res+=1
        return 0    