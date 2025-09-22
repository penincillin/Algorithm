"""
https://leetcode.com/problems/count-bowl-subarrays/description/
Use mono stack, the stack only keeps the item (in the form of indx) in descending order
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, cur_num in enumerate(nums):
            while stack and nums[stack[-1]] < cur_num:
                j = stack.pop()
                if i - j + 1 >= 3:
                    res += 1
            if stack and i - stack[-1] + 1 >= 3:
                res += 1
            stack.append(i)
        return res


def main():
    sol = Solution()

    # nums = [3,5]
    # nums = [-1,1,2]
    # nums = [2,5,3,1,4]
    nums = [5,1,2,3,4]
    res = sol.bowlSubarrays(nums)
    print(res)


if __name__ == '__main__':
    main()
