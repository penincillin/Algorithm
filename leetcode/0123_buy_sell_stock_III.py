"""
Best Time to Buy and Sell Stock III, https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Use DP. A straightforward idea is to use O(N^2) DP, while this can be done in O(N)
Refer to this link for more details (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution)
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def maxProfit(self, prices):
        return self.solve(prices)

    def solve(self, prices):
        N = len(prices)
        if N <= 1:
            return 0
        else:
            dp = [[0 for _ in range(N)] for _ in range(3)] # [3, N]
            for k in range(1, 3):
                min_value = float('inf')
                for i in range(0, N):
                    dp[k][i] = max(dp[k][i-1], prices[i]-min_value)
                    min_value = min(min_value, prices[i]-dp[k-1][i])
            return dp[2][N-1]
         

    def solve_dp_head(self, prices):
        # overall time complexity is O(N^2)
        # DP from start to end
        N = len(prices)
        if N <= 1:
            return 0
        else:
            dp = [[0 for _ in range(N)] for _ in range(3)] # [3, N]
            for k in range(1, 3):
                for i in range(1, N):
                    min_value = float('inf')
                    for j in range(i):
                        # it's easy to find that this operation is repeated as i increasing,
                        # therefore, this for loop (for j) can be removed and obtain algorithm above
                        min_value = min(min_value, prices[j]-dp[k-1][j]) 
                    dp[k][i] = max(dp[k][i-1], prices[i]-min_value)
            return dp[2][N-1]


    def solve_dp_tail(self, prices):
        # overall time complexity is O(N^2).
        # DP from end to start.
        N = len(prices)
        if N <= 1:
            return 0
        else:
            dp1 = [0 for _ in range(N+1)]
            dp2 = [0 for _ in range(N+1)]
            for i in range(N-2, -1, -1):
                low, high = prices[i], -1
                res1, res2 = 0, 0
                for j in range(i+1, N):
                    res1 = max(res1, dp1[j])
                    res2 = max(res2, dp2[j])
                    if prices[j]>low:
                        high = prices[j]
                        mid_res = high-low
                        res1 = max(res1, mid_res)
                        res2 = max(res2, mid_res + dp1[j+1])
                    else:
                        low = prices[j]
                        high = -1
                dp1[i] = res1
                dp2[i] = res2
            res = max(dp1[0], dp2[0])
            return res
                    

def main():
    sol = Solution()
    prices = [1,2,3,4,5]
    #prices = [7,6,4,3,1]
    res = sol.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
