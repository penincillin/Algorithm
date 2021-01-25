"""
Implement Trie (Prefix Tree), https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class TrieNode(object):
    def __init__(self, char):
        self.next_nodes = dict()
        self.char = ''
        self.count = 0

        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode('')
        
    def insert(self, word):
        root = self.root
        for char in word:
            if char in root.next_nodes:
                pass
            else:
                root.next_nodes[char] = TrieNode(char)
            root = root.next_nodes[char]
        root.count += 1
        

    def search(self, word):
        root = self.root
        for char in word:
            if char in root.next_nodes:
                root = root.next_nodes[char]
            else:
                return False
        return root.count > 0 or len(word) == 0
        

    def startsWith(self, prefix):
        root = self.root
        for char in prefix:
            if char in root.next_nodes:
                root = root.next_nodes[char]
            else:
                return False
        return True
        

if __name__ == '__main__':
    trie = Trie()
    trie.insert("abc")
    print(trie.search("ab"))
    print(trie.startsWith("ab"))
    trie.insert("abcd")
    print(trie.search("abcd"))
