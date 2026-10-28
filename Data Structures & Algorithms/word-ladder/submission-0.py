class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        

        queue = collections.deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return 0
                