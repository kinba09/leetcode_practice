class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # num_row = {}
        # num_col = {}
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if board[i][j] not in num_row:
        #                 num_row[board[i][j]] = 1
        #             else:
        #                  return False

        #         if board[j][i] != ".":
        #             if board[j][i] not in num_col:
        #                 num_col[board[j][i]] = 1
        #             else:
        #                  return False
        #     num_row = {}
        #     num_col = {}
        
        # num_box = {}
        # for i in range(3):
        #     for j in range(3):
        #         for k in range(3*i,3*i+3):
        #             for l in range(3*j,3*j+3):
        #                 if board[k][l] != ".":
        #                     if board[k][l] not in num_box:
        #                         num_box[board[k][l]] = 1
        #                     else:
        #                         return False
        #         num_box = {}
        # return True

        check = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
        
                if board[i][j] in check:
                    return False
                    
                check.add(board[i][j])
            check.clear()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue

                if board[j][i] in check:
                    return False
                    
                check.add(board[j][i])
            check.clear()
        
        for i in range(3):
            for j in range(3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        if board[k][l] == ".":
                            continue
                        if board[k][l] in check:
                            return False
                        
                        check.add(board[k][l])
                            
                check.clear()
        return True