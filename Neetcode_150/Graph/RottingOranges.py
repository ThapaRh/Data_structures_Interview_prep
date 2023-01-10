"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0."""

#TC= O(m*n) same is SC
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols=len(grid[0])
        # we will be using BFS because we want to see the least time it takes to rott that oranges
        q= collections.deque()
        goodOranges = 0
        totalTime = 0
        #we will iterate through all of the grid and find the rotten and not rotten 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    goodOranges+=1
        
        #loop till we have bad oranges
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and goodOranges>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for ro,co in directions:
                    newrow = ro+r#get the position of new row on the row+1 in next loops we get col+1, row-1 and col-1 like we did in DFS
                    newcol = co+c
                    if (newrow<0 or newcol<0 or newrow>=len(grid) or newcol>=len(grid[0]) or grid[newrow][newcol]!=1):
                        continue
                    q.append([newrow,newcol])
                    grid[newrow][newcol]=2
                    goodOranges-=1
            totalTime+=1
        
        if goodOranges==0:
            return totalTime
        else:
            return -1
    

