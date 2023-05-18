"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

#This one is tricky to identify the box, here TC=O(N^2) Sc=O(N*N) because in the worst-case scenario, 
# if the board is full, we need a hash set each with size N to store all seen numbers for each of the N rows, N columns, and N boxes, respectively.

#There is this bit manipulation way to do it, will do that later

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check= [set() for _ in range(9)]
        box_check =[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                
                if board[i][j] in row_check[i]:
                    return False
                row_check[i].add(board[i][j])

                if board[i][j] in col_check[j]:
                    return False
                col_check[j].add(board[i][j])

                box_num = (i//3)*3 + j//3
                if board[i][j] in box_check[box_num]:
                    return False
                box_check[box_num].add(board[i][j])
        return True

        #this is not efficient since we are using array and it increases complexity when searching for elements so we are using dictionary now: And for sudoku board stuff we are storing the tuple in dictionary as the key
    class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])
        rows = collections.defaultdict(set) 
        cols = collections.defaultdict(set) 
        sudo = collections.defaultdict(set) 

        for i in range(r):
            for j in range(c):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sudo[(i//3,j//3)]:
                    return False
                else:
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    sudo[(i//3,j//3)].add(board[i][j])
        return True
    
