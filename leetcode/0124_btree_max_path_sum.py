"""
Binary Tree Maximum Path Sum, https://leetcode.com/problems/binary-tree-maximum-path-sum/
The idea is DP (recursively), The return value are two-fold: 
    1. Max path sum traversing the current node (be 0 if the value is less than 0)
    2. Max path sum of this sub-tree (the path may not include current node).
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        return self.solve(root)[1]


    def solve(self, node):
        if node is None:
            return 0, float('-inf')
        else:
            left0, left1 = self.solve(node.left)
            right0, right1 = self.solve(node.right)
            left0 = 0 if left0 < 0 else left0
            right0 = 0 if right0 < 0 else right0
            max_val = max(left1, right1, node.val+left0+right0)
            return node.val+max(left0, right0), max_val


def build_tree():
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    '''
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def main():
    sol = Solution()
    root = build_tree()
    res = sol.maxPathSum(root)
    print(res)


if __name__ == '__main__':
    main()

