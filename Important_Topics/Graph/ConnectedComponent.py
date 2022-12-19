"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
"""

# everything else was quite easy to understand but since it gives edges and nodes, the single unconnected component count has to be added separately
"""

 if len(graph)!=n:
            count+=n-len(graph)
This code tells if the length of node is not equal to each nodes in graph then other nodes are single nodes with no edges in between them, we calculate this by the formula above

TC: O(e+v)==>e=edges v= vertices/nodes
cause we iterate over each edges to store it in graph O(e) and then perform dfsO(n) or O(v)

SC: O(e+v)
we create dictionary to store edges O(e) and perform dfs stack and visited = 2 * O(v)

"""

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph={}
        count = 0
        for edge in edges:
            a,b=edge
            if a in graph:
                graph[a].append(b)
            else:
                graph[a]=[b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b]=[a]
        if len(graph)!=n:
            count+=n-len(graph)
        print(graph)
        visited=set()
        def dfs(graph,e):
            if e in visited:
                return False
            visited.add(e)
            for node in graph[e]:
                dfs(graph,node)
            return True

            
        for elements in graph:
            print(elements)
            if elements in visited:
                continue
            else:
                if dfs(graph,elements):
                    count+=1
        return count

