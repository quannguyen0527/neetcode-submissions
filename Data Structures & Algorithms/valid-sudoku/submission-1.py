class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        #Row_Check
        for i in range(n):
            check = [False] * 10
            for j in range(n):
                if '1' <= board[i][j] <= '9':
                    if check[int(board[i][j])] is True:
                        return False
                    else:
                        check[int(board[i][j])] = True
        #Column_Check
        for i in range(n):
            check = [False] * 10
            for j in range(n):
                if '1' <= board[j][i] <= '9':
                    if check[int(board[j][i])] is True:
                        return False
                    else:
                        check[int(board[j][i])] = True
        #Box_Check
        for i in range(3):
            for j in range(3):
                x = 3*i
                y = 3*j
                check = [False] * 10
                for ii in range(3):
                    for jj in range(3):
                        print(x+ii, y+jj)
                        if '1' <= board[x+ii][y+jj] <= '9':
                            if check[int(board[x+ii][y+jj])] is True:
                                return False
                            else:
                                check[int(board[x+ii][y+jj])] = True
        return True      