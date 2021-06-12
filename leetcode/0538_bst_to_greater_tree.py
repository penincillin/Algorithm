"""
Convert BST to Greater Tree, https://leetcode.com/problems/convert-bst-to-greater-tree
The core of recursion is to clearly decompose the problem into sub-problem and carefully determine the role and return value of each function
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def convertBST(self, root):
        sum_ = self.solve(root, 0)
        return root
    
    def solve(self, root, add):
        # the return value of solve is the sum of all nodes, with node.val updated implicitly
        if root is None:
            return 0
        else:
            # right
            sum_right = self.solve(root.right, add)
            val_ = root.val
            root.val += (sum_right + add)
            sum_left = self.solve(root.left, root.val)
            sum_ = val_ + sum_right + sum_left
            return sum_



def build_tree():
    '''
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    '''

    '''
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    '''

    '''
    root = TreeNode(4)
    left = TreeNode(1)
    right = TreeNode(6)
    root.left = left
    root.right = right

    left.left = TreeNode(0)
    left.right = TreeNode(2)
    left.right.right = TreeNode(3)

    right.left = TreeNode(5)
    right.right = TreeNode(7)
    right.right.right = TreeNode(8)
    '''

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)
    root.right = TreeNode(15)
    root.right.left= TreeNode(13)
    root.right.right = TreeNode(17)
    root.right.right.left = TreeNode(16)

    '''
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    '''

    return root


def main():
    root = build_tree()

    sol = Solution()
    res = sol.convertBST(root)
    #print(res.val, res.left.val, res.left.left.val)
    #pdb.set_trace()
    #print(res.val, res.right.right.left.val)
    print(res.val)


if __name__ == '__main__':
    main()
