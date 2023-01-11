"""You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #inorder to be a valid tree there shouldnot be a cycle and in order to check for cycle we can use union find
        p = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(v):
            par = p[v]
            while(par!=v):
                v=par
                par = p[v]
            return v
        def union(a,b):
            p1,p2 = find(a), find(b)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                p[p2]=p1
                rank[p1]+=rank[p2]
            else:
                p[p1]=p2
                rank[p2]+=rank[p1]
            return True
        count=n

        for a,b in edges:
            if union(a,b)==False:
                return False
            else:
                count-=1
        if count==1: #cause there i sone connected component only
            return True
        return False