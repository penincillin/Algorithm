"""
Longest Palindrome: https://leetcode.com/problems/longest-palindromic-substring/submissions/
The key idea is to use DP. And the DP target is flag[i][j] which is palindrome or not. Instead of max_len[i][j]
BTW, dynamically updating max_len and start can also save the time.
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve_dp(s)

    def solve_dp(self, s: str) -> str:
        valids = {}
        max_len = -1
        res = ""

        n = len(s)
        for i in range(n):
            valids[(i, i)] = True
            max_len = 1
            res = s[i]
        
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                cond0 = s[i] == s[j]
                cond1 = (l == 2) or valids[(i+1, j-1)]
                valid = cond0 and cond1
                valids[(i, j)] = valid
                if valid and l > max_len:
                    max_len = l
                    res = s[i : j+1]
        return res
        

def main():
    sol = Solution()

    # s = "babad"
    s = "cbbd"
    res = sol.longestPalindrome(s)
    print(res)


if __name__ == '__main__':
    main()
