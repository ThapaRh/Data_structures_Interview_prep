"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

"""

def validPath(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """

    dict = {}
    for edge in edges:
        a,b=edge
        if a in dict:
            dict[a].append(b)
        else:
            dict[a]=[b]
        if b in dict:
            dict[b].append(a)
        else:
            dict[b]=[a]
        
    visited=set()
  
    stack = [source]
    while(len(stack)!=0):
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for n in dict[node]:
            if n == destination:
                return True
            stack.append(n)
    return False

    
    # def pathexist(dict,source,destination):
        #"""This is recursive code"""
        # if source==destination:
        #     return True
        # if source in visited:
        #     return False
        # visited.add(source)
        # for node in dict[source]:
        #    if pathexist(dict,node,destination):
        #     return True
        # return False
       


    return pathexist(dict,source,destination)
print(validPath(3,[[0,1],[1,2],[2,0]],0,2))