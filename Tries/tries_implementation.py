

class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.terminating = False

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        root = self.root
        l = len(word)
        for i in range(l):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            # root = root.children.get(index)
            root = root.children[index]

        root.terminating = True


t = Trie()

keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
output = ["Not present in trie", "Present in trie"]

for key in keys:
    t.insert(key)

print(t)