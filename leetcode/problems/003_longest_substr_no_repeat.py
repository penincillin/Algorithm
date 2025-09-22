"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Use sliding window. The idea is to keep the track of index of each character (refreshed the latest existence).
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter
import pdb


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.solve_02(s)

    def solve_01(self, s: str) -> int:
        n = len(s)
        pos = {c : -1 for c in s}
        head = 0
        tail = 0
        res = 0

        while (tail < n):
            if pos[s[tail]] < 0:
                pos[s[tail]] = tail
                tail += 1
                res = max(res, tail - head)
            else:
                head_new = pos[s[tail]] + 1
                for i in range(head, head_new):
                    pos[s[i]] = -1
                head = head_new
        return res
    
    def solve_02(self, s: str) -> int:
        head = 0
        tail = 0
        pos = {c : -1 for c in s}
        res = 0
        for tail, c in enumerate(s):
            p = pos[c]
            if p >= head:
                head = p + 1
            pos[c] = tail # always update the existence
            res = max(tail - head + 1, res) 
        return res
        

def main():
    s = "abba"

    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)


if __name__ == '__main__':
    main()