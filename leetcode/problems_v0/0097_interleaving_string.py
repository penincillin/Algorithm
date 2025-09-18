"""
Interleaving String, https://leetcode.com/problems/interleaving-string/
DP
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        return self.solve(s1, s2, s3)

    def solve(self, s1, s2, s3):
        if len(s1)+len(s2) != len(s3):
            return False
        else:
            n = len(s1)
            m = len(s2)
            dp = [[False for j in range(m+1)] for i in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if i==0 and j==0:
                        dp[i][j] = True
                    elif i>0 and j==0:
                        dp[i][j] = (s1[i-1]==s3[i+j-1] and dp[i-1][j])
                    elif i==0 and j>0:
                        dp[i][j] = (s2[j-1]==s3[i+j-1] and dp[i][j-1])
                    else:
                        dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or \
                                (dp[i][j-1] and s2[j-1]==s3[i+j-1])
            return dp[n][m]


def main():
    sol = Solution()
    
    s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
    res = sol.isInterleave(s1, s2, s3)
    print(res)


if __name__ == '__main__':
    main()
