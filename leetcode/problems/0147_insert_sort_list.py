"""
Template for linked list
"""

import os, sys, shutil
import pdb


class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def insertionSortList(self, head):
        return self.solve_array(head)

    def solve_array(self, head)
        # use additional space to store the value
        nums = list()
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        for i in range(len(nums)):
            ii = i
            while ii > 0:
                if nums[ii] < nums[ii-1]:
                    nums[ii], nums[ii-1] = nums[ii-1], nums[ii]
                ii -= 1
        node = head
        for n in nums:
            node.val = n
            node = node.next
        return head


def build_linked_list(nums):
    root = ListNode(-1)
    node = root
    N, n = len(nums), 0
    while(n < N):
        node.next = ListNode(nums[n])
        node = node.next
        n += 1
    return root.next


def print_linked_list(root):
    nums = list()
    while(root):
        nums.append(root.val)
        root = root.next
    print(nums)


def main():
    #nums = [2,3,1,4]
    nums = [-1,5,3,4,0]
    root = build_linked_list(nums)
    print_linked_list(root)
    sol = Solution()
    root = sol.insertionSortList(root)
    print_linked_list(root)

if __name__ == '__main__':
    main()
