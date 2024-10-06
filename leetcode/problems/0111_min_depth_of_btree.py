"""
Minimum Depth of Binary Tree, https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

class Solution(object):
    def minDepth(self, root):
        return self.solve_iter(root)
    
    def solve_iter(self, root):
        if root is None:
            return 0
        else:
            queue = list()
            queue.append( (root, 1) )
            res = 10000000000
            while len(queue)>0:
                node, depth = queue.pop(0)
                if node is not None:
                    if node.left is None and node.right is None:
                        res = min(res, depth)
                    else:
                        if depth < res:
                            queue.append((node.left, depth+1))
                            queue.append((node.right, depth+1))
            return res
