import os, sys, shutil


class Solution(object):
    def myAtoi(self, str):
        input_str = str.lstrip()
        res_str = ''
        start = False
        for c in input_str:
            if start and not c.isdigit(): break
            if start and c.isdigit(): res_str += c
            if not start:
                if c=='+' or c=='-' or c.isdigit():
                    start=True
                    res_str += c
                else: break
        if(len(res_str)==0): return 0
        if(all(c=='+' or c=='-' for c in res_str)): return 0
        result = int(res_str)
        INT_MAX, INT_MIN = 2147483647, -2147483648
        return max(min(result, INT_MAX), INT_MIN)


        


if __name__ == '__main__':
    ss = Solution()
    print ss.myAtoi("2147483648")

