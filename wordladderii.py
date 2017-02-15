import sys
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList:
            return []
        n = len(beginWord)
        m = len(wordList)
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        visited = {}
        mindepth = m
        buf = {}
        transforms = {}
        
        queue = [([], beginWord, 0)]
        visited[beginWord] = 0
        while queue:
            path, word, depth = queue.pop(0)
            if depth > mindepth:
                continue
                
            # print path, word, depth, queue
            duppath = path[:]
            duppath.append(word)
            
            if word == endWord:
                if depth <= mindepth:
                    buf.setdefault(depth, [])
                    buf[depth].append(duppath)
                    mindepth = depth
                continue
                    
            if word not in transforms:
                s = set()
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newword = word[:i] + c + word[i+1:]
                        if newword in wordset and newword != word:
                            s.add(newword)
                transforms[word] = list(s)
                            
            for newword in transforms[word]:
                # print newword
                if visited.get(newword, sys.maxint) >= depth+1:
                    queue.append((duppath, newword, depth+1))
                    visited[newword] = depth+1
        return buf.get(mindepth, [])
        
s = Solution()
b, e = 'hit', 'cog'
wordlist = ["hot","dot","dog","lot","log","cog"]
print s.findLadders(b, e, wordlist)
        