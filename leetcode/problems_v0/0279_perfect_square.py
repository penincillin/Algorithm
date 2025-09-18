"""
Perfect Squares, https://leetcode.com/problems/perfect-squares/
DP. However, the most straightforward idea runs in O(N^2). While a improved version can run in O(N*log(N))
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb
#import math
from math import sqrt


class Solution(object):
    def numSquares(self, n):
        return self.solve_dp_faster(n)

    def solve_dp(self, n):
        dp = [0 for i in range(n+1)]
        res = [list() for i in range(n+1)]
        cur = 1
        while cur*cur <= n:
            dp[cur*cur] = 1
            res[cur*cur].append(cur)
            cur += 1

        if dp[n] == 1:
            return 1, res[n]
        else:
            for cur in range(2, n+1): # [2, n]
                if dp[cur] != 1:
                    mid_dp = n+10 # n+10 will be larger than any minimal result
                    mid_res = None
                    for j in range(1, cur//2+1): # [1, cur/2]
                        left = j
                        right = cur-left
                        if dp[left]+dp[right] < mid_dp:
                            mid_dp = dp[left] + dp[right]
                            mid_res = res[left] + res[right]
                    dp[cur] = mid_dp
                    res[cur] = mid_res
            # print(res[n])
            return dp[n], res[n]


    def solve_dp_faster(self, n):
        dp = [0 for i in range(n+1)]
        res = [list() for i in range(n+1)]
        cur = 1

        while cur*cur <= n:
            dp[cur*cur] = 1
            res[cur*cur].append(cur)
            cur += 1

        if dp[n] == 1:
            return 1
        else:
            for cur in range(2, n+1): # [2, n]
                if dp[cur] != 1:
                    mid_res = n+10 # n+10 will be larger than any minimal result
                    root = int(sqrt(cur))
                    for j in range(root, 0, -1): # [root, 1]
                        # right = j*j
                        #left = cur-j*j
                        mid_res = min(mid_res, 1 + dp[cur-j*j])
                        #mid_res = min(mid_res, left + right)
                    dp[cur] = mid_res
            return dp[n]



def main():
    n = 7691
    sol = Solution()
    res = sol.numSquares(n)
    print(res)
    """
    for i in range(1, 100):
        res, factor = sol.numSquares(i)
        print(i, res, factor)
    print(res)
    """


if __name__ == '__main__':
    main()
