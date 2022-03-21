"""
Different Ways to Add Parentheses, https://leetcode.com/problems/different-ways-to-add-parentheses/
DP.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb


class Solution(object):
    def diffWaysToCompute(self, expression):
        return self.solve(expression)
    
    def parse_exp(self, exp):
        cur_num = 0
        nums, ops = list(), list()
        for c in exp:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                nums.append(cur_num)
                cur_num = 0
                ops.append(c)
        nums.append(cur_num)
        return nums, ops
    
    def calc_exp(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        else:
            assert op == '*'
            return num1 * num2

    def solve(self, expression):
        nums, ops = self.parse_exp(expression)
        N = len(ops)

        if N == 0:
            return [nums[0],]
        else:
            # init; assert len(nums) == len(ops) + 1
            dp = [[list() for j in range(N+1)] for i in range(N+1)]

            for i, num in enumerate(nums):
                dp[i][i].append(num)

            for l in range(2, N+2): # range from 2 to N+1
                for i in range(0, N):
                    j = i+l-1
                    # dp between [i, j]
                    if j < N+1:
                        res = list()
                        for k in range(i, j):
                            left_res = dp[i][k]
                            right_res = dp[k+1][j]
                            op = ops[k]
                            for lr in left_res:
                                for rr in right_res:
                                    res.append(self.calc_exp(lr, rr, op))
                        dp[i][j] = res
            return dp[0][N]


def main():
    # expression = "2*3-4*5"
    expression = "0"

    sol = Solution()
    res = sol.diffWaysToCompute(expression)
    print(res)


if __name__ == '__main__':
    main()
