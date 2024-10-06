"""
Basic Calculator, https://leetcode.com/problems/basic-calculator/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def calc(self, num_stack, op_stack, pop_more=False):
        # pop_more means the current op is ), then we should pop one more op, which is (
        op = op_stack.pop()
        if op in ['-',  '+']:
            val2 = num_stack.pop()
            val1 = num_stack.pop() if len(num_stack)>0 else 0
            if pop_more:
                op_stack.pop()
            if op == '-':
                return val1-val2
            elif op == '+':
                return val1+val2
        else:
            val = num_stack.pop()
            return val


    def calculate(self, s):
        num_stack = list()
        op_stack = list()
        i, N = 0, len(s)
        while i < N:
            c = s[i]
            if c == ' ':
                i += 1
            else:
                if c.isdigit():
                    num = 0
                    while i<N and c.isdigit():
                        num = num*10 + int(c)
                        i += 1
                        if i<N: 
                            c = s[i]
                    num_stack.append(num)
                else:
                    if c == '(':
                        op_stack.append(c)
                    elif c == ')':
                        val_new = self.calc(num_stack, op_stack, pop_more=True)
                        num_stack.append(val_new)
                    else:
                        if len(op_stack) == 0:
                            op_stack.append(c)
                        else:
                            if op_stack[-1] in ['+', '-']:
                                val_new = self.calc(num_stack, op_stack)
                                num_stack.append(val_new)
                                op_stack.append(c)
                            else:
                                op_stack.append(c)
                    i += 1
                
        # last operation
        if len(op_stack) == 1:
            val_new = self.calc(num_stack, op_stack)
            return val_new
        else:
            return num_stack.pop()
                

def main():
    sol = Solution()
    # s = "(1)"
    # s = "(1 - (1 + 2) + 3)"
    # s = "1-(5)"
    # s = "1212"
    s = "(1+(4+5+2)-3)+(6+8)"
    res = sol.calculate(s)
    print(res)


if __name__ == '__main__':
    main()
