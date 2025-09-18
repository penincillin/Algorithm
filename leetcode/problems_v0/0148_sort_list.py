"""
Sort List, https://leetcode.com/problems/sort-list/
Merge Sort
"""

import os, sys, shutil
import pdb


class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


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


class Solution(object):
    def count_nodes(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def split_list(self, head, idx):
        cur = 0
        while cur<idx and head is not None:
            head = head.next
            cur += 1
        res = head.next
        head.next = None
        return res

    def merge(self, head_prev, head_post):
        head = ListNode()
        cur = head
        while head_prev is not None or head_post is not None:
            if head_prev is None: # indicates head_post is not None
                cur.next = head_post
                cur = cur.next
                head_post = head_post.next
            elif head_post is None: # indicates head_prev is not None
                cur.next = head_prev
                cur = cur.next
                head_prev = head_prev.next
            else: # head_prev and head_post are both not None
                if head_prev.val < head_post.val:
                    cur.next = head_prev
                    cur = cur.next
                    head_prev = head_prev.next
                else:
                    cur.next = head_post
                    cur = cur.next
                    head_post = head_post.next
        return head.next
                    
    def solve(self, head, n):
        if n < 2:
            return head
        else:
            # n is the number of nodes in list
            mid = self.split_list(head, n//2-1) # split_list means split the list at the (n//2)-th node
            head_prev = self.solve(head, n//2)
            head_post = self.solve(mid, n-n//2)
            head = self.merge(head_prev, head_post)
            return head

    def sortList(self, head):
        n = self.count_nodes(head) # number of nodes in total
        return self.solve(head, n)



def main():
    nums = [4, 2, 1, 3, 1, 2]
    # nums = [4, 2, 3]
    root = build_linked_list(nums)

    sol = Solution()
    root = sol.sortList(root)
    print_linked_list(root)


if __name__ == '__main__':
    main()
