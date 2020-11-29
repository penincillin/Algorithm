"""
Plus One, https://leetcode.com/problems/plus-one/
"""

import os, sys, shutil

class Solution(object):
    def plusOne(self, digits):
        digits = digits[::-1]
        add = 1
        for i in range(len(digits)):
            cur = (add + digits[i]) % 10
            add = (add + digits[i]) // 10
            digits[i] = cur
            if add == 0:
                break
        if add > 0:
            digits.append(1)
        return digits[::-1]

def main():
    sol = Solution()
    digits = [1, 9]
    res = sol.plusOne(digits)
    print(res)


if __name__ == '__main__':
    main()
