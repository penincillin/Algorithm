"""
Longest Univalue Path, https://leetcode.com/problems/longest-univalue-path/
Different from classic bst-recursion problem, the final answer is obtained during recursion instead of at the end of recusrion (stack pop-out and return back to root).
Therefore, global variable is required to maintain the status.
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath(self, root):
        self.res = 0
        self.solve(root)
        return self.res
    
    def solve(self, root):
        """
        return the length of longest left or right path that contains root
        """
        if root is None:
            return 0
        else:
            left_res = self.solve(root.left)
            right_res = self.solve(root.right)
            if root.left is not None and root.left.val == root.val:
                left_res += 1
            else:
                left_res = 0
            if root.right is not None and root.right.val == root.val:
                right_res += 1
            else:
                right_res = 0
            self.res = max(self.res, left_res+right_res)
            return max(left_res, right_res)
        
        

def build_tree():
    root = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    return root


def main():
    root = build_tree()
    sol = Solution()
    res = sol.longestUnivaluePath(root)
    print(res)


if __name__ == '__main__':
    main()
