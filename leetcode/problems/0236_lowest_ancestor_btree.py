"""
Lowest Common Ancestor of a Binary Tree, https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
The Lower bound time complexity is O(n), therefore, a straightforward depth-first search would be fine.
"""

import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    '''
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = TreeNode(1)
    left.right = TreeNode(3)
    right.right = TreeNode(6)
    '''
    root = TreeNode(6)
    left1 = TreeNode(2)
    right1 = TreeNode(8)
    left2 = TreeNode(0)
    right2 = TreeNode(4)
    left3 = TreeNode(7)
    right3 = TreeNode(9)
    left4 = TreeNode(3)
    right4 = TreeNode(5)
    root.left = left1
    root.right = right1
    left1.left = left2
    left1.right = right2
    right1.left = left3
    right1.right = right3
    right2.left = left4
    right2.right = right4
    return root


class Solution(object):

    def get_val_node_map(self, node):
        if node is not None:
            self.val2node[node.val] = node
            self.get_val_node_map(node.left)
            self.get_val_node_map(node.right)

    def lowestCommonAncestor(self, root, p, q):
        self.val2node = dict()
        self.get_val_node_map(root)
    
        self.an_info = dict()
        an_list = list() # list of ancestor
        p = p.val; q = q.val

        self.get_ancestor_info(root, p, q, an_list)
        an_p = self.an_info[p]
        an_q = self.an_info[q]
        n = min(len(an_p), len(an_q))
        res_val = None
        for i in range(n):
            if an_p[i]!=an_q[i]:
                res_val = an_p[i-1]
                break
        if res_val is None:
            res_val = an_p[n-1]
        return self.val2node[res_val]

    def get_ancestor_info(self, root, p, q, an_list):
        if root is not None:
            an_list_new = an_list + [root.val]
            self.an_info[root.val] = an_list_new
            if p in self.an_info and q in self.an_info:
                return
            else:
                self.get_ancestor_info(root.left, p, q, an_list_new)
                self.get_ancestor_info(root.right, p, q, an_list_new)


def main():
    root = build_tree()
    p=3; q=5

    sol = Solution()
    sol.val2node = dict()
    sol.get_val_node_map(root)
    p = sol.val2node[p]
    q = sol.val2node[q]

    res = sol.lowestCommonAncestor(root, p, q)
    print(res.val)


if __name__ == '__main__':
    main()
