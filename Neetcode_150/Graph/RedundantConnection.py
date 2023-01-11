"""In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]"""
#TC = O(vertices * edges) SC= O(vertices) for recursion and for dictionary
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #this is naive approach where we iterate through the hashset if the same vertices occur second time and if we can find connections between them then it is redundant
        dictionary = collections.defaultdict(set)#checking to see if we can find separate path for the same vertices
        def DFS(start,target,seen):
            if start not in seen:
                seen.add(start)
                if start==target:
                    return True
                for v in dictionary[start]:
                    if DFS(v,target,seen):
                        return True
            else:
                return False
            
        for start,target in edges: # we iterate through every edges 
            seen=set() #new seen set for every loop
            if start in dictionary and target in dictionary and DFS(start,target,seen): #if we have that in dictionary already and if we can find separate path for that within dictionary
                return [start, target]
            dictionary[start].add(target)
            dictionary[target].add(start)

####This is unionFind solution to the same problem
#TC = O(N) SC= O(N)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)] # the parents for every vertices so far is vertices itself
        rank =[1 for i in range(len(edges)+1)] #since the vertices has 1 parent only which is itself so it's rank is 1

        def find_topparents(value):
            parents = parent[value]

            while(parents!=value):
                value = parents
                parents = parent[value]
            return value
        
        def union(val1, val2):
            par1,par2 = find_topparents(val1), find_topparents(val2)
            if par1==par2:
                return True
            
            if rank[par1]>rank[par2]:
                parent[par2] = par1
                rank[par1]+=rank[par2]
            else:
                parent[par1] = par2
                rank[par2]+=rank[par1]
            return False

        for a,b in edges:
            if union(a,b):
                return [a,b]
        return []


        
