"""
Excel Sheet Column Title, https://leetcode.com/problems/excel-sheet-column-title/
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def convertToTitle(self, n):
        info = dict()
        for i in range(0, 26):
            info[i] = chr(ord('A') + i)

        res = ''
        while (n > 0):
            mode = (n-1) % 26
            n = (n-1) // 26
            res += info[mode]
        return res[::-1]


def main():
    sol = Solution()
    res = sol.convertToTitle(27)
    print(res)


if __name__ == '__main__':
    main()
