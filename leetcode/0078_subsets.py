"""
subsets, https://leetcode.com/problems/subsets/
"""

from collections import defaultdict


class Solution(object):
    def subsets(self, nums):
        return self.solve(nums, 0)
    
    def solve(self, nums, start):
        if start == len(nums):
            return [[],]
        else:
            result = [[],]
            for i in range(start, len(nums)):
                mid_res = self.solve(nums, i+1)
                for mr in mid_res:
                    result.append(nums[i:i+1] + mr)
            return result
        
            
def main():
    nums = [1,2,3]
    sol = Solution()
    res = sol.subsets(nums)
    print(res)


if __name__ == '__main__':
    main()
        
