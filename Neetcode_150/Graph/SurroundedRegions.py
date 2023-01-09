"""Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped."""

#TC= O(m*n) SC=O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows=len(board)
        cols=len(board[0])
        visited=set()
        def check(i,j,visited,board):
            if (i<0 or j<0 or i>=rows or j>=cols or board[i][j]!="O" or (i,j) in visited):
                return
            board[i][j]="T"
            visited.add((i,j))
            check(i+1,j,visited,board)
            check(i-1,j,visited,board)
            check(i,j+1,visited,board)
            check(i,j-1,visited,board)
            return                   

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in [0,rows-1]) or (c in [0,cols-1]):
                    check(r,c,visited,board)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"