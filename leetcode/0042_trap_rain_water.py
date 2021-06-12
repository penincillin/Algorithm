"""
Trapping Rain Water, https://leetcode.com/problems/trapping-rain-water/
The key is to first figure-out a brutal-force method, which consider for each point and the left-right values.
Given the brutal force method, extending it to DP method or O(n) method is straightforward
The two-pointer solution requires more thinking.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        else:
            return self.solve_two_point(height)

    def solve_brutal(self, height):
        N = len(height)
        res = 0
        for i in range(N):
            left_max, right_max = 0, 0
            for j in range(0, i):
                left_max = max(left_max, height[j])
            for j in range(i+1, N):
                right_max = max(right_max, height[j])
            res += max(min(left_max, right_max)-height[i], 0)
        return res

    def solve_dp(self, height):
        # init
        N = len(height)
        left_vals = [0 for i in range(N)]
        right_vals = [0 for i in range(N)]
        left_max, right_max = 0, 0

        # left is updated from left to right
        for i in range(N):
            left_max = max(left_max, height[i])
            left_vals[i] = left_max

        # right is updated from right to left
        for i in range(N-1, -1, -1):
            right_max = max(right_max, height[i])
            right_vals[i] = right_max

        res = 0
        for i in range(N):
            res += max(min(left_vals[i], right_vals[i])-height[i],0)
        return res
    

    def solve_two_point(self, height):
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            # print(left, right, height[left], height[right])
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += (right_max - height[right])
                right -= 1
        return res


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    height = [4, 2, 3]

    sol = Solution()
    res = sol.trap(height)
    print(res)


if __name__ == '__main__':
    main()
