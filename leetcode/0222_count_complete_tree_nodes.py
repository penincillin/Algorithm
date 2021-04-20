"""
Count Complete Tree Nodes, https://leetcode.com/problems/count-complete-tree-nodes/
The O(N) solution is straightforward. An improved version is O(log(n)^2).
The idea is to check the height of tree and check the height of it's right-subtree and divide and conquer. See annotations for details.
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    left.left = TreeNode(4)
    left.right = TreeNode(5)
    right.left = TreeNode(6)
    return root


class Solution(object):
    def countNodes(self, root):
        return self.solve(root)

    def solve_linear(self, root):
        # O(N) time complexity
        if root is None:
            return 0
        else:
            left_res = self.solve(root.left)
            right_res = self.solve(root.right)
            return left_res + right_res + 1

    def get_height(self, node):
        h = 0
        while (node is not None):
            node = node.left
            h += 1
        return h

    def solve(self, root):
        h = self.get_height(root)
        if h == 0:
            return 0
        else:
            res = 0
            while root is not None:
                h_r = self.get_height(root.right)
                if h_r == h-1: # last node on right subtree, count all nodes in left subtree and recursive to right
                    res += 2**(h-1)
                    root = root.right
                else: # last node on left subtree, count all nodes in right subtree and recursive to left
                    res += 2**(h-2)
                    root = root.left
                h -= 1
            return res

def main():
    sol = Solution()
    root = build_tree()
    res = sol.countNodes(root)
    print(res)


if __name__ == '__main__':
    main()
