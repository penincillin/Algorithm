"""
Binary Tree Tilt, https://leetcode.com/problems/binary-tree-tilt/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTilt(self, root):
        res = self.solve(root)
        return res[1]
    
    def solve(self, node):
        if node is None:
            return (0, 0) # sum and tilt
        else:
            left_res = self.solve(node.left)
            right_res = self.solve(node.right)
            cur_sum = node.val + left_res[0] + right_res[0]
            cur_tilt = abs(left_res[0] - right_res[0])
            cur_tilt_sum = cur_tilt + left_res[1] + right_res[1]
            # print(cur_sum, cur_tilt_sum)
            return (cur_sum, cur_tilt_sum)


def build_tree():
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    '''

    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(9)
    root.left = left
    root.right = right
    left.left = TreeNode(3)
    left.right = TreeNode(5)
    right.right = TreeNode(7)
    return root


def main():
    root = build_tree()

    sol = Solution()
    res = sol.findTilt(root)
    print(res)


if __name__ == '__main__':
    main()
