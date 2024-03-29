"""You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]"""
#TC= O(m*n) SC=O(m*n)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rows=len(rooms)
        cols=len(rooms[0])
        gate=collections.deque()
        emptyRooms=0
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j]==2147483647:
                    emptyRooms+=1
                if rooms[i][j]==0:
                    gate.append((i,j))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        distance = 1
        while gate and emptyRooms>0:
            length=len(gate)
            for i in range(length):
                r,c = gate.popleft()
                for dr,dc in directions:
                    row= r+dr
                    col=c+dc
                    if row<0 or col<0 or row>=rows or col>=cols or rooms[row][col]!=2147483647:
                        continue
                    rooms[row][col]=distance
                    gate.append((row,col))
                    emptyRooms-=1
            distance+=1