class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        # should be back tracking becasue we could have many words
        def backtracking(index, node):
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if backtracking(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return backtracking(0, self.root)
