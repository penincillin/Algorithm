"""
Largest Rectangle in Histogram, https://leetcode.com/problems/largest-rectangle-in-histogram/
The straight forward idea is O(N^2), solve_01.
The better idea is solve_02, the whole algorithm is accelerated, however, it's still not guaranteed to be O(n)
The best idea is to use stack, with O(N)
"""

import os, sys, shutil

class Solution(object):
    def largestRectangleArea(self, heights):
        return self.solve_03(heights)
    
    def solve_01(self, heights):
        # O(n^2)
        if len(heights) == 0:
            return 0
        else:
            N = len(heights)
            res = 0

            for i in range(N):
                left_id, right_id = -1, N

                # left
                p = i-1
                while p>=0 and heights[p]>=heights[i]:
                    p -= 1
                left_id = p

                # right
                p = i+1
                while p<N and heights[p]>=heights[i]:
                    p += 1
                right_id = p
                res = max(res, heights[i] * (right_id - left_id - 1))
            return res


    def solve_02(self, heights):
        # better than O(n^2), but might not be the exactly O(n)
        if len(heights) == 0:
            return 0
        else:
            N = len(heights)
            left_idxs = [-1 for i in range(N)]
            right_idxs = [N for i in range(N)]

            # left
            for i in range(N):
                p = i-1
                while p>=0 and heights[p]>=heights[i]:
                    p = left_idxs[p]
                left_idxs[i] = p

            # right
            for i in range(N):
                i = N-i-1
                p = i+1
                while p<N and heights[p]>=heights[i]:
                    p = right_idxs[p]
                right_idxs[i] = p

            res = 0
            for i in range(N):
                res = max(res, heights[i] * (right_idxs[i] - left_idxs[i] - 1))
            return res


    def solve_03(self, height):
        # O(n)
        height.append(0) # add zero to tail
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1 # this operation is important, since
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
   

def main():
    sol = Solution()
    # heights = [2,1,5,6,2,3]
    # heights = [2]
    heights = [1, 2, 3, 4, 5]
    res = sol.largestRectangleArea(heights)
    print(res)


if __name__ == '__main__':
    main()
