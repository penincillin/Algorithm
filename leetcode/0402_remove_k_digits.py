"""
Remove K Digits, https://leetcode.com/problems/remove-k-digits/discuss/?currentPage=1&orderBy=most_votes&query=
This local optimial, sequential, greedy problem can be solved using stack.
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math
import heapq


class Solution(object):

    def removeKdigits(self, num, k):
        return self.solve(num, k)

    def solve(self, digits, k):
        if k >= len(digits):
            return "0"
        else:
            stack = list()
            stack.append(digits[0])
            i = 1
            left = k
            while i<len(digits) and left>0:
                while len(stack)>0 and stack[-1]>digits[i] and left>0:
                    stack.pop()
                    left -= 1
                stack.append(digits[i])
                i += 1

            for _ in range(left):
                stack.pop()

            j = 0
            while j<len(stack) and stack[j]=='0':
                j += 1
            if j == len(stack):
                while i<len(digits) and digits[i]=='0':
                    i += 1
            res = ''.join(stack[j:]) + digits[i:]
            res = res if len(res)>0 else '0'
            return res


def main():
    sol = Solution()
    # num="1432219"; k=3
    num="112"; k=1
    res = sol.removeKdigits(num, k)
    print(res)


if __name__ == '__main__':
    main()
