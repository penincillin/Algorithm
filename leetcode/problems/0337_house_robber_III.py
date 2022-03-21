"""
House Robber III, https://leetcode.com/problems/house-robber-iii/
DFS, the key is to return two values together: using root (res0) and not using root (res1)
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        res0, res1 = self.solve(root)
        return max(res0, res1)

    def solve(self, root):
        if root is None:
            return 0, 0
        else:
            left_res0, left_res1 = self.solve(root.left)
            right_res0, right_res1 = self.solve(root.right)
            res0 = root.val + left_res1 + right_res1
            res1 = max(left_res0, left_res1) + max(right_res0, right_res1)
            return res0, res1
        

def build_tree():
    root = TreeNode(3)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    left.right = TreeNode(3)
    right.right = TreeNode(1)
    return root


def main():
    sol = Solution()
    root = build_tree()
    res = sol.rob(root)
    print(res)


if __name__ == '__main__':
    main()
