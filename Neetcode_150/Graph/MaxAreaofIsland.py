"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally."""

#TC= O(M*n) SC=O(m*N)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        count=0
        visited=set()
        cols=len(grid[0])
        rows=len(grid)
        def DFS(i,j,grid,c):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0 or (i,j) in visited:
                return 0
            else:
                visited.add((i,j))
                val =1 +  DFS(i+1,j,grid,c+1) + DFS(i-1,j,grid,c+1) + DFS(i,j-1,grid,c+1) + DFS(i,j+1,grid,c+1)
                return val
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    val = DFS(i,j,grid,0)
                    count=max(count,val)
        return count