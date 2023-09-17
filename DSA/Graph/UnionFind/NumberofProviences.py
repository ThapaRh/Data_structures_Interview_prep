#TC = O(n^2) SC = O(N)

from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        n = len(isConnected)
        dict = defaultdict(list)
        for i in range(n):
            dict[i]=[]
        rows = len(isConnected)
        cols = len(isConnected[0])
        for i in range(rows):
            for j in range(cols):
                if i!=j and isConnected[i][j] == 1:
                    dict[i].append(j)
        def checkProvience(vals):
            if vals in visited:
                return 
            visited.add(vals)
            for v in dict[vals]:
                checkProvience(v)
            return

        
        for vals in dict:
            if vals not in visited:
                checkProvience(vals)
                provinces+=1
        return provinces
    
    
    
class unionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]

    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x] 
    
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx!=ry:
            if self.rank[rx]>self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[rx]>self.rank[ry]:
                self.root[rx] = ry
            else:
                self.root[rx] = ry
                self.rank[ry]+=1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        rows = n
        cols = len(isConnected[0])
        graph = unionFind(n)
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j]==1 and graph.connected(i,j)==False:
                    graph.union(i,j)
                    n-=1
        return n

