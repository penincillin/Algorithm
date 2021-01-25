"""
Populating Next Right Pointers in Each Node, https://leetcode.comc/populating-next-right-pointers-in-each-node/
BFS
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
            queue = [(root, 0)]
            complete = False
            cur_depth = 0
            cur_node = None
            while len(queue)>0:
                node, depth = queue.pop(0)
                if depth == cur_depth:
                    node.next = cur_node
                    cur_node = node
                else:
                    cur_node = node
                    cur_depth += 1
                if node.right is not None:
                    queue.append((node.right, depth+1))
                if node.left is not None:
                    queue.append((node.left, depth+1))
        
        return root
        

def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def main():
    sol = Solution()
    root = build_tree()
    res = sol.connect(root)
    pdb.set_trace()


if __name__ == '__main__':
    main()
