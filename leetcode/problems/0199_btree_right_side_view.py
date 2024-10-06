"""
Binary Tree Right Side View, https://leetcode.com/problems/binary-tree-right-side-view/
BFS && Queue. The key is to also keep depth.
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
    # root.right = TreeNode(3)
    return root


class Solution(object):
    def rightSideView(self, root):
        return self.solve(root)
    
    def solve(self, root):
        queue = list()
        queue.append((root, 0)) # node and depth
        cur_depth = 0
        res = list()
        complete = False
        while len(queue)>0:
            node, depth = queue[0] #.pop(0)
            if depth == cur_depth:
                if node is not None:
                    queue.append((node.right, depth+1))
                    queue.append((node.left, depth+1))
                    if not complete:
                        res.append(node.val)
                        complete = True
                queue.pop(0)
            else:
                cur_depth = depth
                complete = False
        return res


def main():
    sol = Solution()
    root = build_tree()
    res = sol.rightSideView(root)
    print(res)


if __name__ == '__main__':
    main()
