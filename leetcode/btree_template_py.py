"""
Maximum Depth of Binary Tree, https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        return self.solve_iter(root)
    
    def solve(self, root):
        if root is None:
            return 0
        else:
            left = self.solve(root.left)
            right = self.solve(root.right)
            return max(left, right) + 1

    def solve_iter(self, root):
        if root is None:
            return 0
        else:
            queue = list()
            queue.append( (root, 1) )
            res = -1
            while(len(queue)>0):
                cur = queue.pop(0)
                node, depth = cur
                if node is not None:
                    res = max(depth, res)
                    queue.append( (node.left, depth+1) )
                    queue.append( (node.right, depth+1) )
            return res


def main():
    sol = Solution()


if __name__ == '__main__':
    main()
