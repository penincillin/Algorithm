"""
Remove Duplicates from Sorted Array II, https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

"""

from collections import defaultdict


class Solution(object):
    def removeDuplicates(self, nums):
        N = len(nums)
        p0, p1 = 0, 0
        cur = -1
        appear = 0
        #record = defaultdict(int)
        while(p0 < N):
            num = nums[p0]
            if num == cur:
                appear += 1
                if appear < 3:
                    nums[p1] = num
                    p1 += 1
            else:
                cur = num
                appear = 1
                nums[p1] = num
                p1 += 1
            p0 += 1
        return p1
        
            
def main():
    nums = [0,0,0,1,1,1,2,2,2,3]
    sol = Solution()
    res = sol.removeDuplicates(nums)
    print(res, nums[:res])


if __name__ == '__main__':
    main()
        
