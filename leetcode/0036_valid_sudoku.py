"""
36. Valid Sudoku, https://leetcode.com/problems/valid-sudoku/
"""

class Solution(object):
    def check_rows(self, board):
        for i in range(9):
            exist = [False for _ in range(9)]
            for j in range(9):
                value = board[i][j]
                if value.isdigit():
                    value = int(value)-1
                    if exist[value]:
                        return False
                    else:
                        exist[value] = True
        return True

    def check_cols(self, board):
        for j in range(9):
            exist = [False for _ in range(9)]
            for i in range(9):
                value = board[i][j]
                if value.isdigit():
                    value = int(value)-1
                    if exist[value]:
                        return False
                    else:
                        exist[value] = True
        return True
    

    def check_subboxes(self, board):
        for k in range(9):
            x0 = (k % 3) * 3
            y0 = (k // 3)*3
            exist = [False for _ in range(9)]
            for i in range(9):
                x = x0 + (i % 3)
                y = y0 + (i // 3)
                value = board[y][x]
                if value.isdigit():
                    value = int(value)-1
                    if exist[value]:
                        return False
                    else:
                        exist[value] = True
        return True


    def isValidSudoku(self, board):
        res = self.check_rows(board)
        if not res:
            return False
        else:
            res = self.check_cols(board)
            if not res:
                return False
            else:
                return self.check_subboxes(board)


if __name__ == '__main__':
    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"] ]
    solution = Solution()
    print(solution.isValidSudoku(board))
