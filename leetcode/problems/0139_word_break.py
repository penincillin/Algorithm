"""
Word Break, https://leetcode.com/problems/word-break/
DP: performs dp on s[:i].
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def wordBreak(self, s, wordDict):
        word_dict = dict()
        min_len, max_len = float('inf'), float('-inf')
        for word in wordDict:
            word_dict[word] = 1
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))

        # return self.solve_search(s, min_len, max_len, word_dict)
        return self.solve_dp(s, min_len, max_len, word_dict)
    
    def solve_dp(self, s, min_len, max_len, word_dict):
        N = len(s)
        if N <= 0:
            return True
        else:
            dp = [[False for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(i, N):
                    if (j-i+1)>=min_len and (j-i+1)<=max_len:
                        if s[i:j+1] in word_dict:
                            dp[i][j] = True

            for i in range(min_len, N+1): # i means length
                for j in range(min_len, i):
                    if dp[j][i-1] and dp[0][j-1]:
                        dp[0][i-1] = True

            return dp[0][N-1]

    def solve_search(self, s, min_len, max_len, word_dict):
        N = len(s)
        if N <= 0:
            return True
        else:
            for i in range(1, N+1):
                if i > max_len:
                    return False
                if i >= min_len:
                    if s[:i] in word_dict:
                        res = self.solve_search(s[i:], min_len, max_len, word_dict)
                        if res:
                            return True
            return False


def main():
    sol = Solution()
    s="leetcode"; wordDict=["leet","code"]
    #s="applepenapple"; wordDict=["apple","pen"]
    #s="catsandog"; wordDict=["cats","dog","sand","and","cat"]

    res = sol.wordBreak(s, wordDict)
    print(res)


if __name__ == '__main__':
    main()
