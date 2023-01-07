"""The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true"""
#TC = for the for loop ( rows*cols) and for  DFS = since there are 4 or statement 4^ len(word) Overall: O(rows*cols*4^len(word))
#SC = for DFS O(N)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows= len(board)
        cols=len(board[0])
        storage = set()

        def DFS(r,c,i):
            if len(word)==i:
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or (r,c) in storage):
                return False
            storage.add((r,c))
            res= DFS(r+1,c,i+1) or DFS(r,c+1,i+1) or DFS(r-1,c,i+1) or DFS(r,c-1,i+1)
            storage.remove((r,c))
            return res
        for i in range(rows):
            for j in range(cols):
                if DFS(i,j,0):
                    return True
        return False