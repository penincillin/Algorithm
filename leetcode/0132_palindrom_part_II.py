"""
Palindrome Partitioning II, https://leetcode.com/problems/palindrome-partitioning-ii/
Use DP, the time complexity is O(N^2). This problem contains two DP: DP on overall problem and DP on checking palindrome
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    
    def is_palindrome(self, s):
        start, end = 0, len(s)-1
        while(start <= end):
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

    def minCut(self, s):
        N = len(s)
        dp = {0:0, 1:1} # dp[i] stores the result for substring s[:i]
        is_pa = [[False for _ in range(N)] for _ in range(N)] # is_pa[i:j] means s[i:j] is palindrome
        for i in range(N):
            is_pa[i][i] = True

        for i in range(2, N+1): # i stands for length
            mid_res = float('inf')
            for j in range(0, i):
                if j+1 <= i-2:
                    is_pa[j][i-1] = (s[j] == s[i-1]) and is_pa[j+1][i-2]
                else:
                    is_pa[j][i-1] = (s[j] == s[i-1])
                if is_pa[j][i-1]:
                    prev_res = dp[j]
                    mid_res = min(mid_res, prev_res+1) 
            dp[i] = mid_res
        return dp[N]-1


def main():
    sol = Solution()
    # s = "cabababcbc"
    s = "cabababcbc"
    res = sol.minCut(s)
    print(res)


if __name__ == '__main__':
    main()
