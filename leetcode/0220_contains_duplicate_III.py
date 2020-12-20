"""
Contains Duplicate III, https://leetcode.com/problems/contains-duplicate-iii/
Suppose t = 9, then we put [0,1..9] into one bucket, [10,...20] into the second and ...
If two nums satisfy the condition of less than t, then they either in the same bucket or in the adjancent buckets.
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        record = dict()
        b_size = t + 1
        for i, num in enumerate(nums):
            bucket = num // b_size
            if bucket in record:
                print("here0")
                return True
            if bucket-1 in record and num-record[bucket-1] <= t:
                print("here1")
                return True
            if bucket+1 in record and record[bucket+1]-num <= t:
                print("here2")
                return True
            record[bucket] = num
            if i>=k: 
                del record[nums[i-k] // b_size]
        return False


def main():
    #nums = [1,2,3,1]; k = 3; t = 0
    # nums = [1,0,1,1]; k = 1; t = 2
    nums = [1,5,9,1,5,9]; k = 2; t = 3

    sol = Solution()
    res = sol.containsNearbyAlmostDuplicate(nums, k, t)
    print(res)


if __name__ == '__main__':
    main()
