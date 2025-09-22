"""
https://leetcode.com/problems/add-two-numbers/description/
Duplicate and sort the string, e.g. [a, c, f, i, s, z]
Iterate over sorted list, a -> c, c -> f, f -> i, i -> s, s -> z
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter
import pdb


class Solution:
    def minOperations(self, s: str) -> int:
        return self.solve(s)


    def solve(self, s: str) -> int:
        # remove duplicate, sort, and remove leading a
        chars = sorted(list(set(s)))
        # if chars[0] == "a":
            # chars = chars[1:]
        res = 0

        n = len(chars)
        for i in range(n - 1):
            if chars[i] != "a":
                c0 = chars[i]
                c1 = chars[i+1]
                res += (ord(c1) - ord(c0)) % 26
        
        # last one
        c = chars[-1]
        res += (ord("a") - ord(c)) % 26
        return res
        

def main():
    s = "abcd"    

    sol = Solution()
    res = sol.minOperations(s)
    print(res)


if __name__ == '__main__':
    main()