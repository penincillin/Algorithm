"""
Verify Preorder Serialization of a Binary Tree, https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
Use stack to record the existance of leaves
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def isValidSerialization(self, preorder):
        nodes = preorder.split(',')
        return self.solve(nodes)
    
    def solve(self, nodes):
        if len(nodes) == 1 and nodes[0] == '#': # special cases of ["#",]
            return True
        else:
            stack = list()
            for idx, node in enumerate(nodes):
                if node != '#':
                    stack.append( [node, 0] ) # node and number of leaves, at begining, we have no idea how many child each leave has
                else:
                    if len(stack) > 0:
                        stack[-1][1] += 1
                        while len(stack) > 0 and stack[-1][1] == 2:
                            stack.pop()
                            if len(stack) > 0:
                                stack[-1][1] += 1
                            else:
                                if idx != len(nodes)-1: # the empty of stack can only happens in the end
                                    return False
                    else:
                        # when we encounter "#", there must be a non-null node
                        return False
            return len(stack) == 0
            

def main():
    sol = Solution()

    # s = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    # s = "9,#,#,1"
    s = "1,#,#,#,#"
    res = sol.isValidSerialization(s)
    print(res)


if __name__ == '__main__':
    main()
