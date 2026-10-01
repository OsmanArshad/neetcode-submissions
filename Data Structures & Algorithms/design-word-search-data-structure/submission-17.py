class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            node = curr

            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for child in node.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                    
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.word

        return dfs(0, self.root)
