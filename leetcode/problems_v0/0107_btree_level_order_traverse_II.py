"""
Binary Tree Level Order Traversal II, https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
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
    def levelOrderBottom(self, root):
        return self.solve(root)

    def solve(self, root):
        res = list()
        if root is None:
            return res
        else:
            queue = list()
            queue.append( (root, 1) )
            while len(queue) > 0:
                node, depth = queue.pop(0)
                if depth > len(res):
                    res.append( [node.val] )
                else:
                    res[-1].append(node.val)
                if node.left is not None:
                    queue.append( (node.left, depth+1) )
                if node.right is not None:
                    queue.append( (node.right, depth+1) )
            return res[::-1]


def main():
    sol = Solution()
    root = build_tree()
    res = sol.levelOrderBottom(root)
    print(res)


if __name__ == '__main__':
    main()
