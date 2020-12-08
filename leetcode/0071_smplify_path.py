"""
Simplify Path, https://leetcode.com/problems/simplify-path/
Use stack
"""

import os, sys, shutil


class Solution(object):
    def simplifyPath(self, path):
        record = path.split('/')
        stack = list()
        for r in record:
            if len(r) > 0:
                if r == '.':
                    pass
                elif r == '..':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(r)
            else:
                pass
        return '/' + '/'.join(stack)


def main():
    sol = Solution()
    path = "/abc/./ac/../c"
    res = sol.simplifyPath(path)
    print(res)


if __name__ == '__main__':
    main()
