"""
36. Valid Sudoku, https://leetcode.com/problems/valid-sudoku/
"""

class Solution(object):
    def check_rows(self, board):
        for i in range(9):
            exists = [False for j in range(9)]
            for j in range(9):
                if board[i][j].isdigit():
                    if exists[int(board[i][j])-1]:
                        return False
                    else:
                        exists[int(board[i][j])-1] = True
        return True

    def check_cols(self, board):
        for j in range(9):
            exists = [False for i in range(9)]
            for i in range(9):
                if board[i][j].isdigit():
                    if exists[int(board[i][j])-1]:
                        return False
                    else:
                        exists[int(board[i][j])-1] = True
        return True
    
    def check_subboxes(self, board):
        for i in range(3):
            for j in range(3):
                exists = [False for k in range(9)]
                for k in range(9):
                    x = i*3+k//3
                    y = j*3+k%3
                    if board[x][y].isdigit():
                        if exists[int(board[x][y])-1]:
                            return False
                        else:
                            exists[int(board[x][y])-1] = True
        return True

    def isValidSudoku(self, board):
        res = self.check_rows(board)
        if not res:
            return False
        else:
            res &= self.check_cols(board)
            if not res:
                return False
            else:
                return res & self.check_subboxes(board)


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
