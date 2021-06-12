"""
Word Search II, https://leetcode.com/problems/word-search-ii/
DFS + Trie. The key is to build trie for query words, instead of building trie for input
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb

class TrieNode(object):
    def __init__(self, char=''):
        self.child_nodes = defaultdict(list)
        self.char = char
        self.count = 0 # may not be useful


class Trie(object):
    
    def __init__(self):
        self.root = TrieNode('')
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.child_nodes:
                pass
            else:
                node.child_nodes[char] = TrieNode(char)
            node = node.child_nodes[char]
        node.count += 1
        

class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        root = trie.root

        n = len(board)
        m = len(board[0])
        used = [[False for j in range(m)] for i in range(n)]
        
        res = list()
        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if c in root.child_nodes:
                    used[i][j] = True
                    child_node = root.child_nodes[c]
                    mid_res = self.search(board, used, child_node, i, j)
                    # print("mid_res:", mid_res)
                    used[i][j] = False
                    for r in mid_res:
                        res.append(c + r)
        return res

    def search(self, board, used, node, i0, j0):
        res = list()

        # check whether reaches end
        if node.count > 0:
            res.append("")
            node.count -= 1

        n = len(board)
        m = len(board[0])
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            i = i0 + di
            j = j0 + dj
            if i>=0 and i<n and j>=0 and j<m and not used[i][j]:
                c = board[i][j]
                if c in node.child_nodes:
                    child_node = node.child_nodes[c]
                    used[i][j] = True
                    mid_res = self.search(board, used, child_node, i, j)
                    used[i][j] = False
                    for r in mid_res:
                        res.append(c + r)
        return res


def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    """
    board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    """

    """
    board = [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"]]
    words = ["a", "aa", "aaa"]
    """

    sol = Solution()
    res = sol.findWords(board, words)
    print(res)


if __name__ == '__main__':
    main()
