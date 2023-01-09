"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans."""
"""Complexity Analysis

Time complexity: O(M⋅N), where M is the number of rows and NNN is the number of columns.

Similar to approach 1. The dfs function runs exactly once for each cell accessible from an ocean.

Space complexity: O(M⋅N), where M is the number of rows and NNN is the number of columns.

Similar to approach 1. Space that was used by our queues is now occupied by dfs calls on the recursion stack.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific = set()
        atlantic = set()
        
        def DFS(i,j,heights,prevheights, ourset):
            if i<0 or j<0 or i>=rows or j >=cols or heights[i][j]<prevheights or (i,j) in ourset:
                return 
            else:
                ourset.add((i,j))
                DFS(i+1,j,heights,heights[i][j],ourset)
                DFS(i-1,j,heights,heights[i][j],ourset)
                DFS(i,j+1,heights,heights[i][j],ourset)
                DFS(i,j-1,heights,heights[i][j],ourset)
                return
        for r in range(rows): # we see the 0th column and cols-1th column
            DFS(r,0,heights,heights[r][0],pacific)
            DFS(r,cols-1,heights,heights[r][cols-1],atlantic)
        for c in range(cols):
            DFS(0,c,heights,heights[0][c],pacific)
            DFS(rows-1,c,heights,heights[rows-1][c],atlantic)
        final = []
        for i in range(rows):
            for c in range(cols):
                if (i,c) in pacific and (i,c) in atlantic:
                    final.append([i,c])
        return final


        
        
