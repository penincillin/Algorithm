"""
Refer to this solution for idea: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
Draw a figure like, then add nums one-by-one, the idea will become easy to understand.
    1, 7, 11
   -----------
2  |
4  |
15 |
"""

import heapq


class Solution():
    def kSmallestPairs(self, nums1, nums2, k):
        heap = list()
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 or n2 == 0:
            return []
        for i in range(n1):
            heap.append((nums1[i]+nums2[0], i, 0))
        result = list()
        while k > 0 and len(heap)>0:
            _, i, j = heapq.heappop(heap)
            result.append((nums1[i], nums2[j]))
            if j+1 < n2:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
        return result


def main():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 15]
    k = 3

    sol = Solution()
    res = sol.kSmallestPairs(nums1, nums2, k)
    print(res)


if __name__ == '__main__':
    main()
