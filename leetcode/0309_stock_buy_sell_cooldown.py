"""
Best Time to Buy and Sell Stock with Cooldown, https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Use DP or search
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):

    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        else:
            self.record = dict()
            #return self.solve(prices, 0)
            return self.solve(prices)


    def solve(self, prices):
        # DP
        N = len(prices)
        dp = [0 for _ in range(N+1)]
        for l in range(2, N+1):
            start = N-l
            low, high = prices[start], -1
            res = dp[l-1]
            for i in range(start+1, N):
                if prices[i] > low:
                    high = prices[i]
                    next_start = i+2
                    mid_res = dp[N-next_start] if next_start <= N-2 else 0
                    res = max(res, mid_res+prices[i]-low)
                else:
                    low = prices[i]
                    high = -1
            dp[l] = res
        #print(dp)
        return dp[N]

    
    def solve_01(self, prices, start):
        # search with memorization.
        N = len(prices)
        if start > N-2:
            return 0
        else:
            if start in self.record:
                return self.record[start]
            else:
                res = 0
                low, high = prices[start], -1
                for i in range(start+1, N):
                    if prices[i] > low:
                        high = prices[i]
                        mid_res = self.solve(prices, i+2)
                        res = max(res, mid_res + prices[i]-low)
                    else:
                        low = prices[i]
                        high = -1
                self.record[start] = res
                return res


def main():
    sol = Solution()
    # prices = [1,2,3,0,2]
    prices = [1,2,3,0,2]
    # prices = [0, 2]
    profit = sol.maxProfit(prices)
    print(profit)


if __name__ == '__main__':
    main()
