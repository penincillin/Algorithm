"""
Reorder List, https://leetcode.com/problems/reorder-list/
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
    
    def reverse_list(self, head):
        if head is None:
            return head
        else:
            cur = head
            cur_next = head.next
            head.next = None
            while cur is not None and cur_next is not None:
                tmp_next = cur_next.next
                cur_next.next = cur
                cur = cur_next
                cur_next = tmp_next
            return cur

    def merge(self, head_prev, head_post):
        head = ListNode()
        head.next = head_prev
        prev_cur = head_prev
        post_cur = head_post

        while prev_cur is not None and post_cur is not None:
            prev_next = prev_cur.next
            post_next = post_cur.next
            prev_cur.next = post_cur
            post_cur.next = prev_next
            prev_cur = prev_next
            post_cur = post_next
        return head.next

    def reorderList(self, head):
        n = self.count_nodes(head) # number of nodes in total
        if n < 3:
            return head
        else:
            head_post = self.split_list(head, n//2)
            head_prev = head
            head_post = self.reverse_list(head_post)
            head = self.merge(head_prev, head_post)
            return head


def main():
    #nums = [1, 2, 3, 4, 5]
    nums = [1, 2, 3]
    root = build_linked_list(nums)

    sol = Solution()
    root = sol.reorderList(root)
    print_linked_list(root)


if __name__ == '__main__':
    main()
