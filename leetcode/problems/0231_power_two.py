"""
Power of Two, https://leetcode.com/problems/power-of-two/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def isPowerOfTwo(self, n):
        cands = dict()
        cur = 1
        for i in range(33):
            cands[cur] = 1
            cur *= 2
        return (n in cands)
        
   

def main():
    sol = Solution()
    n = 2
    res = sol.isPowerOfTwo(n)
    print(res)


if __name__ == '__main__':
    main()
