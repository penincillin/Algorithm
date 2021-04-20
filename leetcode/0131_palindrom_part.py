"""
Palindrome Partitioning, https://leetcode.com/problems/palindrome-partitioning/
This problem cannot be solved with O(N^2) or O(N^3), although the final time complexity is O(N^4), it's still better than O(2^N).
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

    def partition(self, s):
        N = len(s)
        dp = {0:[[]], 1:[[s[0],]]} # dp[i] stores the result for substring s[:i]
        for i in range(2, N+1): # i stands for length
            mid_res = []
            for j in range(0, i):
                if self.is_palindrome(s[j:i]): # check every possible substring ends with (i-1)-th, and add this to previous results.
                    for prev_res in dp[j]:
                        mid_res.append(prev_res + [s[j:i],])
            dp[i] = mid_res
        return dp[N]
                    

def main():
    sol = Solution()
    s = "aab"
    res = sol.partition(s)
    print(res)


if __name__ == '__main__':
    main()
