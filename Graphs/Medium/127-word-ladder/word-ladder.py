class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        
        all_patterns = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                all_patterns[pat].append(word)

        # Standard BFS initialization
        queue = deque([(beginWord, 1)])  
        visited = {beginWord}


        while queue:
            word, depth = queue.popleft()

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                
                for nei in all_patterns[pat]:
                    if nei == endWord:
                        return depth + 1
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, depth + 1))

                all_patterns[pat].clear()

        return 0
