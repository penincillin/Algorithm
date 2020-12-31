"""
Edit Distance, https://leetcode.com/problems/edit-distance/
classical DP problem
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        record = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            record[i][0] = i
        for j in range(1, m+1):
            record[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                record[i][j] = min(record[i][j-1]+1, record[i-1][j]+1)
                record[i][j] = min(record[i][j], record[i-1][j-1] + (word1[i-1]!=word2[j-1])*1)
        return record[n][m]


def main():
    sol = Solution()
    word1 = "horse"; word2 = "ros"
    res = sol.minDistance(word1, word2)
    print(res)
  

if __name__ == '__main__':
    main()
