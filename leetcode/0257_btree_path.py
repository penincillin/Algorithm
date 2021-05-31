"""
Binary Tree Paths, https://leetcode.com/problems/binary-tree-paths/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    return root


class Solution(object):
    def binaryTreePaths(self, root):
        nodes_list = self.solve(root)
        res = list()
        for nodes in nodes_list:
            res.append('->'.join(map(str,nodes)))
        return res

    def solve(self, root):
        if root is None:
            return []
        else:
            left_res = self.solve(root.left)
            right_res = self.solve(root.right)
            res = list()
            for lr in left_res:
                res.append([root.val,] + lr)
            for rr in right_res:
                res.append([root.val,] + rr)
            if len(res) == 0:
                res = [[root.val,]]
            return res


def main():
    root = build_tree()
    sol = Solution()
    res = sol.binaryTreePaths(root)
    print(res)


if __name__ == '__main__':
    main()
