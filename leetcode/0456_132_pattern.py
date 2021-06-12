"""
132 Pattern, https://leetcode.com/problems/132-pattern/
The normal idea is to consider s1, s2, s3 (s1 < s2, s1 < s3 and s2 > s3). The good idea is to consider (s2 > s3) (from tail to head).
The idea is to keep track of the highest possible s3 (using stack), to maximum the possibility of finding s1, 
One key idea is that the stack will only keep the value that higher than current S3, otherwise, the function just return.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def find132pattern(self, nums):
        s3 = float('-inf')
        stack = list()
        for num in nums[::-1]:
            if num < s3:
                return True
            else:
                while len(stack)>0 and num>stack[-1]:
                    s3 = stack.pop()
            stack.append(num)
       

def main():
    sol = Solution()
    # nums = [1, 3, -10, -2, -3]
    nums = [5, -5, -10, 10, 1]
    res = sol.find132pattern(nums)
    print(res)


if __name__ == '__main__':
    main()
