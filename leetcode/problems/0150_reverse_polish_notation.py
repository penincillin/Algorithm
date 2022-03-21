"""
Evaluate Reverse Polish Notation, https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

from collections import defaultdict


class Solution(object):
    def evalRPN(self, tokens):
        stack = list()
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num1 - num2
                elif t == '*':
                    res = num1 * num2
                elif t == '/':
                    # res = num1 // num2
                    sign = 1  if (num1 * num2)>0 else -1
                    res = int(abs(num1)) // int(abs(num2))
                    res = res * sign
                #print(num1, num2, t, res)
                stack.append(res)
            else:
                num = int(t)
                stack.append(num)
        return res
        
            
def main():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    sol = Solution()
    res = sol.evalRPN(tokens)
    print(res)


if __name__ == '__main__':
    main()
