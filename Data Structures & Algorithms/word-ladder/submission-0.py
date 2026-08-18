from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord,1)])
        visited = set([beginWord])
        setOfWords= set(wordList)
        alphabets=[chr(x+ord('a')) for x in range(26)]
        while queue:
            word,turn = queue.popleft()
            for idx in range(len(word)):
                for char in alphabets:
                    newWord=word[:idx]+char+word[idx+1:]
                    if newWord not in visited and newWord in setOfWords:
                        if newWord == endWord:
                            return turn+1
                        visited.add(newWord)
                        queue.append((newWord,turn+1))
        return 0
                
