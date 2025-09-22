"""
https://leetcode.com/problems/two-sum/description/
Use dict
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.solve_brutal(nums, target)
        return self.solve_linear(nums, target)

    def solve_brutal(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def solve_linear(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for idx, num in enumerate(nums):
            num1 = target - num
            if num1 in exists:
                idx1 = exists[num1]
                return [idx1, idx]
            else:
                exists[num] = idx

def main():
    sol = Solution()

    nums = [2,5,5,11]; target = 10

    res = sol.twoSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
