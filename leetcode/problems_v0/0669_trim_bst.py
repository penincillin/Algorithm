"""
Trim a Binary Search Tree, https://leetcode.com/problems/trim-a-binary-search-tree/
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimBST(self, root, low, high):
        return self.solve(root, low, high)

    def solve(self, root, low, high):
        if root is None:
            return root
        else:
            if root.val < low:
                right = self.solve(root.right, low, high) # trim right
                return right
            elif root.val > high:
                left = self.solve(root.left, low, high)
                return left
            else:
                left = self.solve(root.left, low, high)
                right = self.solve(root.right, low, high)
                root.left = left
                root.right = right
                return root


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    return root


def main():
    root = build_tree()
    low, high = 1, 2

    sol = Solution()
    res = sol.trimBST(root, 1, 2)


if __name__ == '__main__':
    main()
