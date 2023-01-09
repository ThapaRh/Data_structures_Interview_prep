"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1"""
"""Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

Space complexity : worst case O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        if not grid:
            return 0
        dict={}

        def find_island(i,j,graph):
            if (i<0 or j<0 or i>=rows or j>=cols or graph[i][j]=="0" or (i,j) in dict):
                return 
            if graph[i][j]=="1" and (i,j) not in dict:
                dict[(i,j)]=True
                find_island(i-1,j,graph)
                find_island(i+1,j,graph) 
                find_island(i,j-1,graph) 
                find_island(i,j+1,graph)
                return
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in dict:
                    find_island(i,j,grid)
                    count+=1
                else:
                    continue
        return count

