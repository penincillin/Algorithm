"""
Kth Smallest Element in a BST, https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Use inorder traverse
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = TreeNode(1)
    left.right = TreeNode(3)
    right.right = TreeNode(6)
    return root


class Solution():
    def kthSmallest(self, root, k):
        return self.solve(root, k)
    
    def solve(self, node, k):
        stack = list()
        res = list()
        while node is not None or len(stack)>0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
            if len(res) == k:
                return res[-1]


def main():
    sol = Solution()
    root = build_tree()
    k = 2
    res = sol.kthSmallest(root, k)
    print(res)


if __name__ == '__main__':
    main()
