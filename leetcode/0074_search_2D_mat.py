"""
Search a 2D Matrix, https://leetcode.com/problems/search-a-2d-matrix/
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False
        else:
            N = len(matrix)
            M = len(matrix[0])
            start, end = 0, M*N
            
            while(start < end):
                mid = (start + end) // 2
                i, j = divmod(mid, M)
                if matrix[i][j] < target:
                    start = mid+1
                elif matrix[i][j] == target:
                    return True
                else:
                    end = mid
            
            return False

    
def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 13
    
    sol = Solution()
    res = sol.searchMatrix(matrix, target)
    print(res)


if __name__ == '__main__':
    main()
