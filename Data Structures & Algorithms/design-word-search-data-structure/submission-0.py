class TrieNode:

    def __init__(self):
        self.characters = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            curr = curr.characters[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.characters.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.characters:
                        return False
                    cur = cur.characters[c]
            return cur.word

        return dfs(0, self.root)