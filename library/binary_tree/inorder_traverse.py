import os, sys, shutil


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    left.left = TreeNode(4)
    left.right = TreeNode(5)
    right.left = TreeNode(6)
    return root

class Solution():
    def inorder(self, root):
        #return self.solve_iter(root)
        return self.solve(root)
    
    def solve(self, node):
        if node is None:
            return []
        else:
            res = self.solve(node.left)
            res.append(node.val)
            res += self.solve(node.right)
            return res

    def solve_iter(self, node):
        stack = list()
        res = list()
        while node is not None or len(stack)>0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res


def main():
    sol = Solution()
    root = build_tree()
    res = sol.inorder(root)
    print(res)


if __name__ == '__main__':
    main()
