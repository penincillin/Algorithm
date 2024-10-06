"""
Number of Islands, https://leetcode.com/problems/number-of-islands/
union set algorithm, use stack and DFS
"""

class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        elif len(grid[0]) == 0:
            return 0
        else:
            n = len(grid)
            m = len(grid[0])
            stack = list()
            record = [[-1 for j in range(m)] for i in range(n)]
            s_i = 0 # which line to start
            res = 0
            while True:
                find = False
                for i in range(s_i, n):
                    for j in range(m):
                        if grid[i][j] == '1' and record[i][j] == -1:
                            stack.append((i,j))
                            record[i][j] = 0
                            find = True
                            break
                    if find:
                        s_i = i
                        break
                if not find:
                    break
                else:
                    while(len(stack)>0):
                        x, y = stack.pop(0)
                        for i, j in [(0,1), (1,0), (0,-1), (-1,0)]:
                            x1 = x+i
                            y1 = y+j
                            if x1>=0 and x1<n and y1>=0 and y1<m and record[x1][y1]==-1:
                                if grid[x1][y1] == '1':
                                    stack.append((x1,y1))
                                    record[x1][y1] = 1
                    res += 1
            return res




def main():
    sol = Solution()
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    res = sol.numIslands(grid)
    print(res)

if __name__ == '__main__':
    main()
        
