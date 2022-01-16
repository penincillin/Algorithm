"""
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def numDistinct(self, s, t):
        n = len(s)
        m = len(t)
        if m > n:
            return 0
        else:
            dp = [[0 for j in range(m+1)] for i in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if i==0 and j==0:
                        dp[i][j] = 1
                    elif i>0 and j==0:
                        dp[i][j] = 1 # to be updated
                    elif i==0 and j>0:
                        dp[i][j] = 0
                    else:
                        if j > i:
                            dp[i][j] = 0
                        else:
                            if s[i-1] == t[j-1]:
                                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                            else:
                                dp[i][j] = dp[i-1][j]
            #for j in range(1, m+1):
                #for i in range(1, n+1):
                    #print(dp[i][j], end=' ')
                #print()
            return dp[n][m]
                            

def main():
    sol = Solution()
    # s = "rabbbit"; t = "rabbit"
    # s = "babgbag"; t = "bag"
    s = "aabb"; t = "ab"
    res = sol.numDistinct(s, t)
    print(res)


if __name__ == '__main__':
    main()

