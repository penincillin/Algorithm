"""
 Design Add and Search Words Data Structure, https://leetcode.com/problems/design-add-and-search-words-data-structure/
 Use trie to implement, remember to add 'is_leaf'
"""

from collections import defaultdict

class TrieNode(object):
    def __init__(self, char=''):
        self.childs = dict()
        self.is_leaf = False
        self.char = char

        
class WordDictionary(object):
    
    def __init__(self):
        self.root = TrieNode()

        
    def addWord(self, word):
        node = self.root
        for c in word:
            if c in node.childs:
                node = node.childs[c]
            else:
                new_node = TrieNode(c)
                node.childs[c] = new_node
                node = new_node
        node.is_leaf = True

        
    def search(self, word):
        node = self.root
        return self.solve(word, node)
    
    def solve(self, word, node):
        for i in range(len(word)):
            c = word[i]
            if c != '.':
                if c in node.childs:
                    node = node.childs[c]
                else:
                    return False
            else:
                for child in node.childs.values():
                    mid_res = self.solve(word[i+1:], child)
                    if mid_res:
                        return True
                return False
        return node.is_leaf
        
        
def main():
    wd  =  WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    val1 = wd.search("bad")
    val2 = wd.search("ba")
    print(val1, val2)
    #val1 = wd.search("pad")
    #val2 = wd.search("bad")
    #val3 = wd.search(".ad")
    #val4 = wd.search("b..")
    #val5 = wd.search("....")
    #print(val1, val2, val3, val4, val5)


if __name__ == '__main__':
    main()
