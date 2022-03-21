"""
Valid Number, https://leetcode.com/problems/valid-number/
Solving use state machine, refer to this https://leetcode.com/problems/valid-number/discuss/936475/C%2B%2B-logical-easy-solution-faster-than-100
"""

import os, sys, shutil


class Solution(object):
    def isNumber(self, s):
        # remove head & tail blanks
        s = s.strip()
        digits = list(map(str, range(10)))
        symbols = ['+', '-']

        state, idx, N = 0, 0, len(s)
        while idx < N:
            c = s[idx]
            
            # state -1
            if state == -1:
                break

            # state 0
            if state == 0:
                if c in symbols:
                    state = 1
                elif c in digits:
                    state = 2
                elif c == '.':
                    state = 3
                else:
                    state = -1

            # state 1
            elif state == 1:
                if c in digits:
                    state = 2
                elif c == '.':
                    state = 3
                else:
                    state = -1

            # state 2
            elif state == 2:
                if c in digits:
                    state = 2
                elif c == '.':
                    state = 5
                elif c == 'e':
                    state = 6
                else:
                    state = -1

            # state 3
            elif state == 3:
                if c in digits:
                    state = 4
                else:
                    state = -1

            # state 4
            elif state == 4:
                if c in digits:
                    state = 4
                elif c == 'e':
                    state = 6
                else:
                    state = -1

            # state 5
            elif state == 5:
                if c in digits:
                    state = 4
                elif c == 'e':
                    state = 6
                else:
                    state = -1
            
            # state 6
            elif state == 6:
                if c in symbols:
                    state = 7
                elif c in digits:
                    state = 8
                else:
                    state = -1
            
            # state 7
            elif state == 7:
                if c in digits:
                    state = 8
                else: 
                    state = -1
            
            # state 8
            elif state == 8:
                if c in digits:
                    state = 8
                else: 
                    state = -1

            idx += 1

        return state in [2, 4, 5, 8]
        

def main():
    sol = Solution()
    s = "95e3e"
    res = sol.isNumber(s)
    print(res)


if __name__ == '__main__':
    main()
