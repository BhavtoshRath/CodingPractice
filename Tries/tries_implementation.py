

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.terminating = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getNode(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        pCrawl = self.root  # pCrawl is the word's character pointer

        for i in range(len(word)):
            ind = self.get_index(word[i])

            if pCrawl.children[ind] is None:
                pCrawl.children[ind] = self.getNode()

            pCrawl = pCrawl.children[ind]

        pCrawl.terminating = True

    def search(self, word):
        pCrawl = self.root
        for i in range(len(word)):
            ind = self.get_index(word[i])
            if pCrawl.children[ind] is None:
                return False
            pCrawl = pCrawl.children[ind]

        return pCrawl != None and pCrawl.terminating


t = Trie()

keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
output = ["Not present in trie", "Present in trie"]

for key in keys:
    t.insert(key)

print("{} ---- {}".format("the",output[t.search("the")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("there",output[t.search("there")]))