from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) + len(nums2) == 0:
            return 0.0
        else:
            # return self.solve_linear(nums1, nums2)
            return self.solve_binary(nums1, nums2)
    
    def solve_linear(self, nums1, nums2) -> float:
        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            tgts = [(n+m)//2+1]
        else:
            tgts = [(n+m)//2, (n+m)//2+1]
        
        inf = 99999999
        
        i1, i2 = 0, 0
        res = list()
        while(len(tgts) > 0):
            if i1 < n:
                num1 = nums1[i1]
            else:
                num1 = inf

            if i2 < m:
                num2 = nums2[i2]
            else:
                num2 = inf
            
            if tgts[0] == (i1 + i2 + 1):
                tgts = tgts[1:]
                res.append(min(num1, num2))

            if num1 <= num2:
                i1 += 1
            else:
                i2 += 1
        
        return sum(res) / len(res)
    

    def findK(self, nums1, nums2, k):
        # we make sure len(nums1) <= len(nums2), otherwise, we swap them
        if len(nums1) >= len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        i1 = min(k//2, len(nums1))
        i2 = k - i1
        num1 = nums1[i1-1]
        num2 = nums2[i2-1]

        if num1 == num2:
            return num1
        elif num1 < num2:
            return self.findK(nums1[i1:], nums2, k-i1)
        else:
            return self.findK(nums1, nums2[i2:], k-i2)
        
    
    def solve_binary(self, nums1, nums2) -> float:
        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            return self.findK(nums1, nums2, (n+m)//2 + 1)
        else:
            res = (  
                self.findK(nums1, nums2, (n+m)//2) +
                self.findK(nums1, nums2, (n+m)//2+1)
            ) / 2
            return res
        

def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    res = sol.findMedianSortedArrays(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
        