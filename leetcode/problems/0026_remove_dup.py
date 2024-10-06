"""
26. Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""
class Solution(object):
    def removeDuplicates(self, nums):
        start = 1
        end = 1
        tot = len(nums)

        while end < tot:
            while end < tot and nums[end] == nums[start-1]:
                end += 1
            
            if start < tot and end < tot:
                nums[start] = nums[end]
                start += 1
        
        return start


def main():
    sol = Solution()
    nums = [1,2,2,3,4,5,5,6]
    # nums = [1,2,2,3,4,5,5,6]
    # nums = [1,2,3,4,5,6,6,6,6,6,6,6,6,6,7,7,7,7]
    # nums = [1]

    k = sol.removeDuplicates(nums)
    print(k)
    print(nums[:k])


if __name__ == '__main__':
    main()
