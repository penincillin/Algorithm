"""
https://leetcode.com/problems/generate-schedule

Combination + greedy
The key idea is each time select the pair with least played times to balance
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


def gen_perms(nums: List[int], use_perm: bool = True) -> List[List[int]]:
    res = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            cond0 = use_perm and (i != j)
            cond1 = (not use_perm) and (i < j)
            if cond0 or cond1:
                res.append((nums[i], nums[j])) 
    return res


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4:
            return []
        else:
            return self.solve_valid(n)
    
    def find_next(self, comb, n, played, num_played):
        min_num, res_perm = 9999999999999, None

        for i in range(n):
            for j in range(n):
                if (i != j) and (i not in comb) and (j not in comb):
                    perm = (i, j)
                    if not played[perm]:
                        n0 = num_played[i]
                        n1 = num_played[j]
                        num = n0 + n1
                        if num < min_num:
                            min_num = num
                            res_perm = perm
        return res_perm

    def solve_valid(self, n: int) -> List[List[int]]:
        perms = gen_perms(list(range(n)))
        
        res = [[0, 1]]
        total = n * (n - 1)
        played = {perm : False for perm in perms}
        played[(0, 1)] = True
        num_played = {i : 0 for i in range(n)}
        num_played[0] = 1
        num_played[1] = 1

        while len(res) < total:
            last_perm = res[-1]
            i0, i1 = last_perm
            comb = (i0, i1) if i0 < i1 else (i1, i0)
            # sub_perms = all_perms[comb]

            select_perm = self.find_next(comb, n, played, num_played)
            t0, t1 = select_perm
            played[select_perm] = True
            num_played[t0] += 1
            num_played[t1] += 1
            
            res.append(list(select_perm))
        return res


def check_res(res: List[List[int]], n: int) -> bool:
    res = [tuple(comb) for comb in res]
    if n <= 4:
        return len(res) == 0
    else:
        # check length valid first
        cond = len(res) == n * (n -1)
        if cond:
            # check all combines exist and only exist once
            combs = gen_perms(list(range(n)))
            exists = {comb: 0 for comb in combs}
            for comb in res:
                exists[comb] += 1
            all_exists = all(val == 1 for val in exists.values())
            if all_exists:
                # check consecutive not overlapped
                for i in range(len(res)-1):
                    comb0 = res[i]
                    comb1 = res[i+1]
                    if comb0[0] in comb1 or comb0[1] in comb1:
                        print("invalid duplicate")
                        return False
                return True
            else:
                print("invalid exists")
                # print(exists)
                return False
        else:
            print("invalid length")
            return False


def main():
    sol = Solution()
    n = 5 
    res = sol.generateSchedule(n)
    print(res)
    valid = check_res(res, n)
    print(valid)


if __name__ == '__main__':
    main()
