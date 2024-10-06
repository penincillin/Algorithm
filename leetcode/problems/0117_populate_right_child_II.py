"""
Populating Next Right Pointers in Each Node II, https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Use BFS, the key here is to run from right to left, instead of left to right.
"""

import os, sys, shutil
import pdb


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        if root is None:
            return root
        else:
            queue = list()
            cur_node = None
            cur_depth = 0
            queue.append( (root, 0) )
            while len(queue) > 0:
                node, depth = queue.pop(0)
                if node is not None:
                    if node.right is not None:
                        queue.append( (node.right, depth+1) )
                    if node.left is not None:
                        queue.append( (node.left, depth+1) )
                    if depth == cur_depth:
                        node.next = cur_node
                        cur_node = node
                    else:
                        cur_depth = depth
                        cur_node = node
        return root
        

def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    '''
    return root


def main():
    sol = Solution()
    root = build_tree()
    root = sol.connect(root)

    left, right = root.left, root.right
    left0, right0 = left.left, left.right
    _, right1 = right.left, right.right
    print(left0.next, right0)
    print(right0.next, right1)


if __name__ == '__main__':
    main()
