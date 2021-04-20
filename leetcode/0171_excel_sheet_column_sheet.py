"""
Excel Sheet Column Number, https://leetcode.com/problems/excel-sheet-column-number/
"""

import os, sys, shutil


class Solution(object):
    def titleToNumber(self, s):
        res = 0
        high = 1
        for c in s[::-1]:
            digit = (ord(c)-ord('A')+1)
            cur = high * digit
            res += cur
            high *= 26
        return res


def main():
    sol = Solution()
    s = "AB"
    res = sol.titleToNumber(s)
    print(res)


if __name__ == '__main__':
    main()
