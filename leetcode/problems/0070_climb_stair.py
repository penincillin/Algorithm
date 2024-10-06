"""
Climbing Stairs, https://leetcode.com/problems/climbing-stairs/
"""

import os, sys, shutil


class Solution(object):
    def climbStairs(self, n):
        res = [0 for i in range(n+1)]
        res[1] = 1
        if n >= 2:
            res[2] = 2
        for i in range(3, n+1):
            res[i] = res[i-2] + res[i-1]
        return res[n]


def main():
    sol = Solution()
    n = 3
    res = sol.climbStairs(n)
    print(res)


if __name__ == '__main__':
    main()
