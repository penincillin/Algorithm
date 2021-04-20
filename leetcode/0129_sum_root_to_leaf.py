"""
Sum Root to Leaf Numbers, https://leetcode.com/problems/sum-root-to-leaf-numbers/
DFS
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def sumNumbers(self, root):
        nums = self.solve(root)
        res = 0
        for val, _ in nums:
            res += val
        return res

    def __is_leaf(self, node):
        return node.left is None and node.right is None

    def solve(self, node):
        if node is None:
            return []
        elif self.__is_leaf(node):
            return [(node.val, 1), ]
        else:
            left_res = self.solve(node.left)
            right_res = self.solve(node.right)
            res = list()
            for val, depth in left_res:
                res.append( (node.val*10*depth+val, depth*10) )
            for val, depth in right_res:
                res.append( (node.val*10*depth+val, depth*10) )
            return res


def build_tree():
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    '''
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    return root


def main():
    sol = Solution()
    root = build_tree()
    res = sol.sumNumbers(root)
    print(res)


if __name__ == '__main__':
    main()
