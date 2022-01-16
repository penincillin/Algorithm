"""
Min Stack, https://leetcode.com/problems/min-stack/
Refer to https://leetcode.com/problems/min-stack/discuss/1007532/Two-stacks-wvideo-whiteboard-explanation for explanation.
The key idea is to keep two stacks, one stack is the normal stack, the other stack only push the monotonically decreasing elements.

Another idea is illustrated here:https://leetcode.com/problems/min-stack/discuss/49010/Clean-6ms-Java-solution.
The idea is to keep track of the current min values.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class MinStack(object):

    def __init__(self):
        self.stack = list()
        self.m_stack = list()
        

    def push(self, x):
        self.stack.append(x)
        if len(self.m_stack)==0 or x<=self.m_stack[-1] :
            self.m_stack.append(x)
        

    def pop(self):
        value = self.stack[-1]
        self.stack.pop()
        if value == self.m_stack[-1]:
            self.m_stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.m_stack[-1]
                

def main():
    ms = MinStack()
    ms.push(-2);
    ms.push(0);
    ms.push(-3);
    v1 = ms.getMin(); # return -3
    ms.pop();
    v2 = ms.top();    # return 0
    v3 = ms.getMin(); # return -2


if __name__ == '__main__':
    main()
