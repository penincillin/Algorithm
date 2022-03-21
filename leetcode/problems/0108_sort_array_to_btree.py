"""
Convert Sorted Array to Binary Search Tree, https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.solve(nums)

    def solve(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            root = TreeNode(nums[0])
        elif len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
        else:
            mid = (0 + len(nums)) // 2
            root = TreeNode(nums[mid])
            left = self.solve(nums[:mid])
            right = self.solve(nums[mid+1:])
            root.left = left
            root.right = right
        return root


def main():
    nums = [-10,-3,0,5,9]
    sol = Solution()
    res = sol.sortedArrayToBST(nums)
    print(res)


if __name__ == '__main__':
    main()
