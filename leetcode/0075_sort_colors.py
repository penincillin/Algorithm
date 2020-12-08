"""
Sort Colors, https://leetcode.com/problems/sort-colors/
This code share the same spirit as quit sort, pivoting
"""

from collections import defaultdict


class Solution(object):
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
    

def main():
    nums = [2,0,2,1,1,0]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
        
