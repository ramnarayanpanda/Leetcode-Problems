# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        for row in range(9):
            lst1 = []
            for col in range(9):
                if board[row][col] != '.':
                    lst1.append(board[row][col])
            if len(lst1)!=len(set(lst1)):
                return False
            
            
        for col in range(9):
            lst1 = []
            for row in range(9):
                if board[row][col] != '.':
                    lst1.append(board[row][col])
            if len(lst1)!=len(set(lst1)):
                return False
            
            
        row = 0
        while row<9:
            col = 0
            while col<9:
                lst = []
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[i][j] != '.': lst.append(board[i][j])
                        
                if len(lst)!=len(set(lst)):
                    return False
                
                col+=3
            row+=3
            
            
        return True
            
            
            
            
            
            
            
        