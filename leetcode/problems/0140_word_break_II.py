"""
Word Break II, https://leetcode.com/problems/word-break-ii/
Similar to "Word Break" (https://leetcode.com/problems/word-break/)
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
            return []
        else:
            dp = [[ [] for _ in range(N)] for _ in range(N)] # dp[i][j] = [s1, s2, ...]
            for i in range(N):
                for j in range(i, N):
                    if (j-i+1)>=min_len and (j-i+1)<=max_len:
                        if s[i:j+1] in word_dict:
                            dp[i][j] = [s[i:j+1], ]

            for i in range(min_len, N+1): # i means length
                for j in range(min_len, i):
                    for s1 in dp[0][j-1]:
                        for s2 in dp[j][i-1]:
                            s = s1 + ' ' + s2
                            dp[0][i-1].append(s.strip())

            return dp[0][N-1]


def main():
    sol = Solution()
    # s="leetcode"; wordDict=["leet","code"]
    # s="catsanddog"; wordDict=["cat","cats","and","sand","dog"]
    # s="pineapplepenapple"; wordDict=["apple","pen","applepen","pine","pineapple"]
    s="catsandog"; wordDict=["cats","dog","sand","and","cat"]

    res = sol.wordBreak(s, wordDict)
    print(res)


if __name__ == '__main__':
    main()
