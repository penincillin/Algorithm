"""
Lowest Common Ancestor of a Binary Search Tree, https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Time complexity O(N), use the property of BST.
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
        # obtain val to node map
        self.val2node = dict()
        self.get_val_node_map(root)
        # init 
        self.an_info = dict()
        an_list = list() # list of ancestor
        p = p.val; q = q.val
        if p > q: # swap to make sure p < q
            p, q = q, p
        res_val = self.solve(root, p, q)
        res = self.val2node[res_val]
        return res

    def solve(self, root, p, q):
        val = root.val
        if p == val or q == val:
            return val
        elif p < val and q > val:
            return val
        elif p < val and q < val:
            return self.solve(root.left, p, q)
        else:
            # p > val and q > val
            return self.solve(root.right, p, q)
   

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
