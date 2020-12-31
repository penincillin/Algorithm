"""
Path Sum II, https://leetcode.com/problems/path-sum-ii/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        return self.solve(root, sum)


    def solve(self, root, sum):
        if root is None:
            return [[]]
        elif root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return [[]]
        else:
            left_res = self.solve(root.left, sum-root.val)
            right_res = self.solve(root.right, sum-root.val)
            result = list()
            for mid_res in left_res:
                if len(mid_res) > 0:
                    result.append( [root.val] + mid_res )
            for mid_res in right_res:
                if len(mid_res) > 0:
                    result.append( [root.val] + mid_res )
            if len(result) == 0:
                result = [[]]
            return result


def build_tree():
    root = TreeNode(10)
    root.left = TreeNode(-2)
    root.right = TreeNode(2)
    return root


def main():
    sol = Solution()
    root = build_tree()
    sum = 12
    res = sol.pathSum(root, sum)
    print(res)


if __name__ == '__main__':
    main()
