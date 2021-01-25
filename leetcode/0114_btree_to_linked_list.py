"""
Flatten Binary Tree to Linked List, https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Use preorder traverse
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        self.solve(root)

    def solve(self, root):
        if root is None:
            return None, None
        else:
            left_head, left_tail = self.solve(root.left)
            right_head, right_tail = self.solve(root.right)
            if left_head is not None:
                root.right = left_head
            else:
                left_tail = root
            if right_head is not None:
                left_tail.right = right_head
            else:
                right_tail = left_tail
            root.left = None
            return root, right_tail


def build_tree():
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3, TreeNode(4), TreeNode(5))
    return root


def main():
    root = build_tree()
    sol = Solution()
    sol.flatten(root)
    pdb.set_trace()


if __name__ == '__main__':
    main()
