"""
Predict the Winner, https://leetcode.com/problems/predict-the-winner/
DP
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def PredictTheWinner(self, nums):
        # sum1, sum2 = self.solve_search(nums, True) # sum1 means the optimal value of player-1, sum2 means for player-2
        sum1, sum2 = self.solve_dp(nums)
        return sum1 >= sum2

    def solve_dp(self, nums):
        N = len(nums)
        dp = [[[None for k in range(2)] for j in range(N)] for i in range(N)] # dp[i][j][0/1] = (sum1, sum2) [i,j]

        for i in range(N):
            dp[i][i][0] = (0, nums[i])
            dp[i][i][1] = (nums[i], 0)

        for l in range(2, N+1):
            for i in range(N):
                j = i+l-1
                if j >= N: break

                sum1, sum2 = dp[i][j-1][0]
                sum3, sum4 = dp[i+1][j][0]
                sum1 += nums[j]
                sum3 += nums[i]
                if sum1-sum2 >= sum3-sum4:
                    dp[i][j][1] = (sum1, sum2)
                else:
                    dp[i][j][1] = (sum3, sum4)

                sum1, sum2 = dp[i][j-1][1]
                sum3, sum4 = dp[i+1][j][1]
                sum2 += nums[j]
                sum4 += nums[i]
                if sum2-sum1 >= sum4-sum3:
                    dp[i][j][0] = (sum1, sum2)
                else:
                    dp[i][j][0] = (sum3, sum4)

        sum1, sum2 = dp[0][N-1][1]
        return sum1, sum2


    def solve_search(self, nums, my_turn):
        """
        my_turn is a boolean, true means play-1 select, false means player-2 select
        return value sum1, sum2. sum1 means the optimal value of player-1, sum2 means for player-2
        """
        if len(nums) == 1:
            if my_turn:
                return nums[0], 0
            else:
                return 0, nums[0]

        else:
            sum_head1, sum_head2 = self.solve(nums[1:], not my_turn)
            sum_tail1, sum_tail2 = self.solve(nums[:-1], not my_turn)

            # player-1 select
            if my_turn: 
                sum_head1 += nums[0]
                sum_tail1 += nums[-1]
                if sum_head1-sum_head2 >= sum_tail1-sum_tail2:
                    return sum_head1, sum_head2
                else:
                    return sum_tail1, sum_tail2
            # player-2 select
            else: 
                sum_head2 += nums[0]
                sum_tail2 += nums[-1]
                if sum_head2-sum_head1 >= sum_tail2-sum_tail1:
                    return sum_head1, sum_head2
                else:
                    return sum_tail1, sum_tail2

def main():
    nums = [1,5,2]
    # nums = [1,5,233,7]

    sol = Solution()
    res = sol.PredictTheWinner(nums)
    print(res)


if __name__ == '__main__':
    main()
