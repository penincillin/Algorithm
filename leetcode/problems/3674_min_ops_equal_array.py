"""
https://leetcode.com/problems/minimum-operations-to-equalize-array/description/
1. If all elements are the same, the result is 0.
2. If not, just AND all the elements, the result is 1.
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter
import pdb


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        all_equal = self.equal(nums)
        if all_equal:
            return 0
        else:
            return 1

    def equal(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                return False
        return True
        

def main():
    nums = [2]

    sol = Solution()
    res = sol.minOperations(nums)
    print(res)


if __name__ == '__main__':
    main()