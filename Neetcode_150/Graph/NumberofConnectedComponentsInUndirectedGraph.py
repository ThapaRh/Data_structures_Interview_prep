"""You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1"""
#TC = O(N) SC=O(N) Not exactly but somehow
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]
        count=n

        def find(val):
            p=parent[val]
            while(p!=val):
                val=p
                p=parent[val]
            return val
        
        def union(v1,v2):
            p1,p2 = find(v1), find(v2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                    parent[p2]=p1
                    rank[p1]+=rank[p2]
            else:
                    parent[p1]=p2
                    rank[p2]+=rank[p1]
            return True
                

        for a,b in edges:
            if union(a,b):
                count-=1
        
        return count