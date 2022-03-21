"""
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def calc(self, num_stack, op_stack):
        op = op_stack.pop()
        val2 = num_stack.pop()
        val1 = num_stack.pop() if len(num_stack)>0 else 0
        if op == '-':
            return val1 - val2
        elif op == '+':
            return val1 + val2
        elif op == '*':
            return val1 * val2
        else:
            return val1 // val2

    def cmp_op(self, op1, op2):
        if op1 in ['+', '-'] and op2 in ['/', '*']:
            return False
        else:
            return True


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
                    while i<N and s[i].isdigit():
                        num = num*10 + int(s[i])
                        i += 1
                    num_stack.append(num)
                else:
                    if len(op_stack) == 0:
                        op_stack.append(c)
                    else:
                        while len(op_stack)>0 and self.cmp_op(op_stack[-1], c):
                            val_new = self.calc(num_stack, op_stack)
                            num_stack.append(val_new)
                        op_stack.append(c)
                    i += 1
                
        print(num_stack, op_stack)
        while(len(op_stack)) > 0:
            val_new = self.calc(num_stack, op_stack)
            num_stack.append(val_new)
        return num_stack.pop()
                

def main():
    sol = Solution()
    # s = "3+2*2"
    # s = "5 - 3/2"
    # s = "1*2-3/4+5*6-7*8+9/10"
    # s = "1*2-3/4+5*6"
    res = sol.calculate(s)
    print(res)


if __name__ == '__main__':
    main()
