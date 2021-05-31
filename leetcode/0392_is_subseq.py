"""
Is Subsequence, https://leetcode.com/problems/is-subsequence/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True
        else:
            i, j = 0, 0
            while i<len(s) and j<len(t):
                if s[i] == t[j]:
                    i += 1
                    if i == len(s):
                        return True
                j += 1
            return False


def main():
    sol = Solution()
    s="abc"; t="ahbgdc"
    res = sol.isSubsequence(s, t)
    print(res)


if __name__ == '__main__':
    main()
