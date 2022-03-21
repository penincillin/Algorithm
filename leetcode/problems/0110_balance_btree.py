"""
Balanced Binary Tree, https://leetcode.com/problems/balanced-binary-tree/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    right.left = TreeNode(15)
    right.right = TreeNode(7)
    return root


class Solution(object):
    def isBalanced(self, root):
        return self.solve(root)
    
    def solve(self, root):
        height = self.get_height(root)
        return height != -1

    def get_height(self, node):
        if node is None:
            return 0
        else:
            h_left = self.get_height(node.left)
            h_right = self.get_height(node.right)

            # -1 means invalid
            if h_left == -1 or h_right == -1:
                return -1

            # abs(h_left-h_right) <= 1
            elif h_left-h_right < -1 or h_left-h_right > 1:
                return -1

            else:
                height = 1 + max(h_left, h_right)
                return height

def main():
    sol = Solution()
    root = build_tree()
    res = sol.isBalanced(root)
    print(res)


if __name__ == '__main__':
    main()
